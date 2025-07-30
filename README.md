
# BPPS Instances Repository

This repository contains benchmark instances for the Bin Packing Problem with item-class Setups (BPPS).

The instance set is associated with the research paper:

**"The Bin Packing Problem with item-class Setups"**  
by R. Baldacci, F. Ciccarelli, S. Coniglio, V. Dose and F. Furini.


## Repository Structure

- `instances/`: Directory containing all BPPS instance files
- `instance_info.xlsx`: Spreadsheet with overview of all instances
- `instance_status.xlsx`: Spreadsheet with best known values and optimality status for each instance
- `instance_list.txt`: Text file listing all instance names
- `toy_example.txt`: Small example instance for testing

## Instance Naming Convention

Instance files follow the naming pattern:
```
bpps_d{capacity}n{items}m{classes}w{min}_{max}s{min}_{max}f{flag}_seed{value}.txt
```

Where:
- `capacity`: Bin capacity value
- `items`: Number of items
- `classes`: Number of item classes
- `v{min}_{max}`: Weight range for items [min, max]
- `s{min}_{max}`: Setup weight range [min, max]
- `f{flag}`: Setup costs (0 = no setup costs, 1 = with setup costs)
- `seed{value}`: Random seed used for instance generation (0 or 1)

## Instance File Format

Each instance file contains:

1. **Header line**: `{no. of items} {no. of classes} {bin capacity} {bin cost}`
2. **Class definitions** (one per class): `{setup cost} {setup weight} {item count}`
    - Setup costs are represented as negative values
3. **Item weights** (one per line): Items are ordered by class (all class 1 items, then class 2, etc.)

### Example Structure
```
75	10	200	10
-4	3	5
-4	2	11
...
27
12
29
...
```
