# BPPS Instance Generator

Python script for generating Bin Packing Problem with Setups (BPPS) benchmark instances.

## 🚀 Features

- **Configurable Parameters**: All generation parameters can be customized via JSON configuration files
- **Naming Convention Compliance**: Follows the BPPS naming convention described in [`../data/README.md`](../data/README.md)
- **Command-Line Interface**: Easy-to-use CLI with various options
- **Statistics Tracking**: Generates detailed statistics about the instance generation process

<br>

## ⚡ Quick Start

### 🔧 Using Default Configuration

```bash
python bpps_instance_generator.py
```

This will generate instances using the same parameters reported in the paper.

### ⚙️ Using Custom Configuration

1. **Create a configuration file** (or modify `example_config.json`):

```bash
python bpps_instance_generator.py --save-default-config my_config.json
```

2. **Edit the configuration file** to customize parameters:

```json
{
    "capacities": [200, 1000, 10000],
    "num_items": [75, 100],
    "num_classes": [5, 10, 15],
    "item_weight_ranges": [
        [0.05, 0.15],
        [0.15, 0.30],
        [0.30, 0.45]
    ],
    "setup_weight_ranges": [
        [0.01, 0.10],
        [0.10, 0.20],
        [0.20, 0.30]
    ],
    "setup_cost_flags": [0, 1],
    "seeds": [0, 1, 2],
    "min_items_per_class": 2,
    "output_directory": "./generated_instances"
}
```

3. **Generate instances**:

```bash
python bpps_instance_generator.py --config my_config.json
```

<br>

## 📋 Configuration Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `capacities` | List[int] | List of bin capacities (d values) |
| `num_items` | List[int] | List of item counts (n values) |
| `num_classes` | List[int] | List of class counts (m values) |
| `item_weight_ranges` | List[Tuple[float, float]] | Weight ranges for items as fractions of capacity (v1, v2) |
| `setup_weight_ranges` | List[Tuple[float, float]] | Setup weight ranges as fractions of capacity (s1, s2) |
| `setup_cost_flags` | List[int] | Setup cost flags (0 = no costs, 1 = with costs) |
| `seeds` | List[int] | Random seeds for reproducibility |
| `min_items_per_class` | int | Minimum items required per class |
| `output_directory` | str | Directory to save generated instances |

<br>

## 💻 Command Line Options

```bash
python bpps_instance_generator.py [OPTIONS]

Options:
    -c, --config FILE         Path to JSON configuration file
    --save-default-config FILE  Save default configuration to JSON file
    -o, --output-dir DIR      Output directory (default: ./generated_instances)
    -h, --help               Show help message
```

<br>

## 📁 Generated Files

### 📄 Instance Files

Files follow the naming convention described in [`../data/README.md`](../data/README.md):
```
bpps_d{capacity}n{items}m{classes}w{min}_{max}s{min}_{max}f{flag}_seed{value}.txt
```

For detailed information about the file format and naming convention, see the [data documentation](../data/README.md).

### 📊 Statistics File

`generation_statistics.json` contains:
- Total attempted instances
- Successful generations
- Failed generations
- Success rate
- Details of failed instances

<br>

## 💡 Example Usage

### 🎯 Generate with Custom Parameters

```python
from bpps_instance_generator import InstanceConfig, BPPSInstanceGenerator

# Create custom configuration
config = InstanceConfig(
        capacities=[100, 500],
        num_items=[20, 40],
        num_classes=[3, 6],
        item_weight_ranges=[(0.1, 0.2), (0.2, 0.4)],
        setup_weight_ranges=[(0.05, 0.15)],
        setup_cost_flags=[1],
        seeds=[0, 1, 2],
        output_directory="./my_instances"
)

# Generate instances
generator = BPPSInstanceGenerator(config)
stats = generator.generate_instances()
print(f"Generated {stats['successful']} instances successfully")
```

### 📥 Load Configuration from File

```python
from bpps_instance_generator import load_config_from_file, BPPSInstanceGenerator

config = load_config_from_file("my_config.json")
generator = BPPSInstanceGenerator(config)
generator.generate_instances()
```

<br>

## 📋 Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

<br>

## 📝 Notes

- The generator ensures all classes have at least `min_items_per_class` items
- Failed generations are logged and statistics are provided
- Output directory is created automatically if it doesn't exist
- Instance files use the BPPS format as specified in [`../data/README.md`](../data/README.md)

