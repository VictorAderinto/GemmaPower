import pandas as pd

def region_to_text(region_data):
    """
    Converts a region data dictionary (from network_manager.get_region_data)
    into a Markdown string.
    """
    cluster_id = region_data['cluster_id']
    output = []
    output.append(f"# Analysis Region {cluster_id}\n")
    
    # Buses
    output.append("## Buses within Region")
    buses = region_data['buses']
    cols = ['vn_kv', 'type', 'zone', 'in_service', 'min_vm_pu', 'max_vm_pu'] # 'name' is index usually
    if 'name' in buses.columns:
        cols.insert(0, 'name')
    
    # Filter valid cols
    valid_cols = [c for c in cols if c in buses.columns]
    output.append(buses[valid_cols].to_markdown())
    output.append(f"\nTotal Buses: {len(buses)}\n")

    # Lines
    output.append("## Connected Lines")
    lines = region_data['lines']
    line_cols = ['from_bus', 'to_bus', 'length_km', 'loading_percent', 'max_i_ka', 'is_tieline', 'in_service']
    if 'name' in lines.columns:
        line_cols.insert(0, 'name')
    valid_cols = [c for c in line_cols if c in lines.columns]
    
    if not lines.empty:
        output.append(lines[valid_cols].to_markdown())
        # Summary
        tie_count = lines['is_tieline'].sum() if 'is_tieline' in lines.columns else 0
        output.append(f"\nTotal Lines: {len(lines)} (Tie-lines: {tie_count})\n")
    else:
        output.append("No lines connected.\n")

    # Aggregated Load/Gen
    output.append("## Power Balance")
    total_load_mw = region_data['loads']['p_mw'].sum() if not region_data['loads'].empty else 0
    total_gen_mw = region_data['gens']['p_mw'].sum() if not region_data['gens'].empty else 0
    # Add static Gen
    if not region_data['sgens'].empty:
        total_gen_mw += region_data['sgens']['p_mw'].sum()
        
    output.append(f"- Total Load: {total_load_mw:.2f} MW")
    output.append(f"- Total Generation: {total_gen_mw:.2f} MW")
    output.append(f"- Net Balance: {total_gen_mw - total_load_mw:.2f} MW (Positive = Exporting, Negative = Importing)")
    
    return "\n".join(output)
