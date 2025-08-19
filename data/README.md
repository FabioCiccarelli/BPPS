# BPPS Instance Data

This directory contains all the benchmark instances for the Bin Packing Problem with Setups (BPPS).

## 📁 Directory Contents

- **`instances/`**: All BPPS instance files (480 benchmark instances)
- **`instance_info.xlsx`**: Comprehensive spreadsheet with:
  - Overview of all instances
  - Best known values for each instance
  - Optimality status information
- **`toy_example.txt`**: Small example instance for testing and understanding the file format

<br>

## 🏷️ Instance Naming Convention

Instance files follow the structured naming pattern:
```
bpps_d{capacity}n{items}m{classes}w{min}_{max}s{min}_{max}f{flag}_seed{value}.txt
```

### Parameter Breakdown:
- **`d{capacity}`**: Bin capacity value
- **`n{items}`**: Number of items in the instance
- **`m{classes}`**: Number of item classes
- **`w{min}_{max}`**: Item weight range [min, max] as percentage of capacity
- **`s{min}_{max}`**: Setup weight range [min, max] as percentage of capacity
- **`f{flag}`**: Setup cost configuration
  - `f0` = no setup costs (only setup weights)
  - `f1` = with setup costs
- **`seed{value}`**: Random seed used for instance generation (0 or 1)

### Example:
`bpps_d10000n100m10w1500_3000s100_1000f0_seed0.txt`
- Bin capacity: 10000
- Items: 100
- Classes: 10
- Item weights: 15-30% of capacity (1500-3000)
- Setup weights: 1-10% of capacity (100-1000)
- No setup costs (f0)
- Random seed: 0

<br>

## 📄 Instance File Format

Each instance file contains tab-separated data in the following structure:

### Header Line
```
{no. of items} {no. of classes} {bin capacity} {bin cost}
```

### Class Definitions
One line per class containing:
```
{setup cost} {setup weight} {item count}
```
**Note**: Setup costs are represented as negative values

### Item Weights
One weight per line, with items ordered by class:
- All items from class 1
- All items from class 2
- And so on...

### Complete Example
```
75	10	200	10
-4	3	5
-4	2	11
-2	4	8
-3	1	7
-5	3	6
-2	2	9
-4	4	5
-3	3	8
-2	1	10
-4	2	6
27
12
29
18
25
...
```

In this example:
- 75 items total, 10 classes, bin capacity 200, bin cost 10
- First class: setup cost -4, setup weight 3, 5 items
- Second class: setup cost -4, setup weight 2, 11 items
- Item weights follow (first 5 weights belong to class 1, next 11 to class 2, etc.)

<br>

## 📊 Instance Overview

The benchmark includes **480 instances** with the following characteristics:

### Capacity Values
- 200, 1000, 10000

### Item Counts
- 25, 50, 75, 100, 200

### Class Counts
- 5, 10

### Weight Configurations
- **Item weights**: 5-15%, 15-30%, of bin capacity
- **Setup weights**: 1-10%, 10-20% of bin capacity

### Setup Cost Configurations
- **f0**: No setup costs (only setup weights matter)
- **f1**: With setup costs (both setup weights and costs matter)

### Seeds
- Each configuration is generated with 2 different random seeds (0 and 1)

<br>

## 📈 Best Known Values

For best known solutions and optimality status, refer to the `instance_info.xlsx` spreadsheet which contains:
- Instance names and parameters
- Best known objective values
- Solution status (optimal/best known)
- Additional information about the best known solutions
