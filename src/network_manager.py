import pandapower as pp
import pandapower.networks as pn
import pandas as pd
import json
import numpy as np
from sklearn.cluster import KMeans

def load_network(name="case57"):
    """
    Loads a sample network from pandapower.
    """
    print(f"Loading {name}...")
    if name == "case57":
        net = pn.case57()
    elif name == "case118":
        net = pn.case118()
    else:
        raise ValueError(f"Unknown network name: {name}")
    return net

def _extract_coordinates(geo_str):
    """
    Helper to parse the 'geo' column JSON string or dictionary.
    Returns (x, y) or (lon, lat).
    """
    if isinstance(geo_str, str):
        try:
            data = json.loads(geo_str)
        except:
            return None, None
    elif isinstance(geo_str, dict):
        data = geo_str
    else:
        return None, None

    if 'coordinates' in data:
        return data['coordinates'][0], data['coordinates'][1]
    return None, None

def cluster_spatially(net, n_clusters=4):
    """
    Clusters the network buses into 'n_clusters' regions based on their geographical coordinates.
    Adds a 'cluster' column to net.bus.
    """
    # 1. Extract coordinates
    coords = []
    valid_indices = []
    
    # Check if 'geo' column exists
    if 'geo' not in net.bus.columns:
        print("Warning: No 'geo' column found. Assigning all to Cluster 0.")
        net.bus['cluster'] = 0
        return net

    for idx, row in net.bus.iterrows():
        x, y = _extract_coordinates(row['geo'])
        if x is not None and y is not None:
            coords.append([x, y])
            valid_indices.append(idx)
    
    if not coords:
        print("Warning: No valid coordinates found. Assigning all to Cluster 0.")
        net.bus['cluster'] = 0
        return net

    # 2. Perform K-Means Clustering
    X = np.array(coords)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X)

    # 3. Assign labels back to buses
    net.bus['cluster'] = -1 # Default for missing coords
    for i, bus_idx in enumerate(valid_indices):
        net.bus.at[bus_idx, 'cluster'] = labels[i]
        
    # Fill any remaining -1 with the nearest cluster or 0 (simplified: 0)
    net.bus.loc[net.bus['cluster'] == -1, 'cluster'] = 0
    
    print(f"Clustering complete. Assigned {n_clusters} clusters.")
    return net

def get_region_data(net, cluster_id):
    """
    Returns a dictionary containing the subset of data for a specific cluster.
    Includes buses, connected lines, loads, and gens in that region.
    """
    # Filter Buses
    buses = net.bus[net.bus['cluster'] == cluster_id]
    bus_indices = buses.index.tolist()
    
    # Filter Lines (Internal + Tienlines originating from this region)
    # We include lines if EITHER from or to bus is in the region, 
    # but to avoid duplicates in a global sense, agents usually handle "their" half.
    # For simplicity, we give them all lines connected to their buses.
    lines = net.line[
        net.line['from_bus'].isin(bus_indices) | 
        net.line['to_bus'].isin(bus_indices)
    ].copy()
    
    # Mark tie-lines
    lines['is_tieline'] = ~ (lines['from_bus'].isin(bus_indices) & lines['to_bus'].isin(bus_indices))

    # Filter Loads
    loads = net.load[net.load['bus'].isin(bus_indices)]
    
    # Filter Generators
    gens = net.gen[net.gen['bus'].isin(bus_indices)]
    sgens = net.sgen[net.sgen['bus'].isin(bus_indices)]
    
    return {
        "cluster_id": cluster_id,
        "buses": buses,
        "lines": lines,
        "loads": loads,
        "gens": gens,
        "sgens": sgens
    }
