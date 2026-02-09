import pandapower.networks as pn
import pandas as pd

# Load Case 57
net = pn.case57()

print("--- Network Summary ---")
print(net)

print("\n--- Available Tables (Keys) ---")
for key in net.keys():
    if isinstance(net[key], pd.DataFrame) and net[key].shape[0] > 0:
        print(f"Table: {key} | Shape: {net[key].shape}")

print("\n--- Bus Columns ---")
print(net.bus.columns.tolist())
print(net.bus.head(3))

print("\n--- Line Columns ---")
print(net.line.columns.tolist())
print(net.line.head(3))

print("\n--- Gen Columns ---")
print(net.gen.columns.tolist())
print(net.gen.head(3))

# Check for 'zone' or 'area' in bus data
if 'zone' in net.bus.columns:
    print("\n--- Zones Available ---")
    print(net.bus['zone'].unique())
else:
    print("\n--- No 'zone' column in bus data ---")

