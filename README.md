
# BPPS Instances Repository

This repository contains benchmark instances for the Bin Packing Problem with Setups (BPPS).

The instance set is associated with the research paper:

**"The Bin Packing Problem with Setups: Formulations, Structural Properties, and Computational Insights"**  
by R. Baldacci, F. Ciccarelli, S. Coniglio, V. Dose and F. Furini.


## 🎯 Problem Overview

The Bin Packing Problem with Setups (BPPS) is a generalization of the classical Bin Packing Problem where items are partitioned into classes. When at least one item from a given class is packed into a bin, both a setup weight (reducing available capacity) and a setup cost are incurred. The objective is to determine a minimum-cost partition of items into bins such that:

- The total weight of items plus setup weights of active classes does not exceed bin capacity in any bin;
- The total cost — including bin costs and class-specific setup costs — is minimized.

This problem naturally arises in production planning and logistics applications where different item types require specific preparation or configuration steps.

In the referenced paper, we:

- Introduce a novel Integer Linear Programming formulation for this problem and analyze its LP relaxation properties;
- Propose a family of valid inequalities that strengthen the LP relaxation and improve the optimal worst-case performance;
- Derive theoretical upper bounds on the number of bins required, enabling significant problem size reduction;
- Establish a comprehensive benchmark of 480 instances and demonstrate substantial computational improvements through the integration of MCI and bin-number bounds.

<br>

## 📁 Repository Structure

- [`instances/`](https://github.com/FabioCiccarelli/BPPS_instances/tree/main/instances): Directory containing all BPPS instance files
- [`instance_info.xlsx`](https://github.com/FabioCiccarelli/BPPS_instances/tree/main/instance_info.xlsx): Spreadsheet with overview of all instances, their best known values and the optimality status for each instance
- [`toy_example.txt`](https://github.com/FabioCiccarelli/BPPS_instances/tree/main/toy_example.txt): Small example instance for testing

<br>

## 🏷️ Instance Naming Convention

Instance files follow the naming pattern:
```
bpps_d{capacity}n{items}m{classes}w{min}_{max}s{min}_{max}f{flag}_seed{value}.txt
```

Where:
- `capacity`: Bin capacity value
- `items`: Number of items
- `classes`: Number of item classes
- `w{min}_{max}`: Weight range for items [min, max]
- `s{min}_{max}`: Setup weight range [min, max]
- `f{flag}`: Setup costs (0 = no setup costs, 1 = with setup costs)
- `seed{value}`: Random seed used for instance generation (0 or 1)

<br>

## 📄 Instance File Format

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

<br>

## 📖 Citation

If you use this dataset in academic work, please cite:

```bibtex
@article{Baldacci2025BPPS,
    title={The Bin Packing Problem with Setups: Formulations, Structural Properties, and Computational Insights},
    author={Baldacci, R. and Ciccarelli, F. and Coniglio, S. and Dose, V. and Furini, F.},
    year={2025}
}
```


