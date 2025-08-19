#!/usr/bin/env python3
"""
BPPS Instance Generator

This module generates benchmark instances for the Bin Packing Problem with Setups (BPPS).

Instance files follow the naming pattern:
bpps_d{capacity}n{items}m{classes}w{min}_{max}s{min}_{max}f{flag}_seed{value}.txt

Author: Fabio Ciccarelli
Date: August 19, 2025
"""

import random
import argparse
import json
from pathlib import Path
from typing import List, Tuple, Dict, Any
from math import floor, ceil
from dataclasses import dataclass, asdict


@dataclass
class InstanceConfig:
    """Configuration class for BPPS instance generation parameters."""
    
    capacities: List[int]
    num_items: List[int]
    num_classes: List[int]
    item_weight_ranges: List[Tuple[float, float]]  # (v1, v2) as fractions of capacity
    setup_weight_ranges: List[Tuple[float, float]]  # (s1, s2) as fractions of capacity
    setup_cost_flags: List[int]  # 0 = no setup costs, 1 = with setup costs
    seeds: List[int]
    min_items_per_class: int = 2
    output_directory: str = "./generated_instances"
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
        return asdict(self)
    
    @classmethod
    def from_dict(cls, config_dict: Dict[str, Any]) -> 'InstanceConfig':
        """Create configuration from dictionary."""
        return cls(**config_dict)


class BPPSInstanceGenerator:
    """Generator for Bin Packing Problem with Setups (BPPS) instances."""
    
    def __init__(self, config: InstanceConfig):
        """
        Initialize the BPPS instance generator.
        
        Args:
            config: Instance generation configuration
        """
        self.config = config
        self._ensure_output_directory()
    
    def _ensure_output_directory(self) -> None:
        """Create output directory if it doesn't exist."""
        Path(self.config.output_directory).mkdir(parents=True, exist_ok=True)
    
    def _generate_filename(self, d: int, n: int, m: int, w_min: int, w_max: int, 
                          s_min: int, s_max: int, f: int, seed: int) -> str:
        """
        Generate filename following the BPPS naming convention.
        
        Args:
            d: Bin capacity
            n: Number of items
            m: Number of classes
            w_min: Minimum item weight
            w_max: Maximum item weight
            s_min: Minimum setup weight
            s_max: Maximum setup weight
            f: Setup cost flag (0 or 1)
            seed: Random seed
            
        Returns:
            Generated filename
        """
        return f"bpps_d{d}n{n}m{m}w{w_min}_{w_max}s{s_min}_{s_max}f{f}_seed{seed}.txt"
    
    def _generate_single_instance(self, d: int, n: int, m: int, v1: float, v2: float,
                                 s1: float, s2: float, f: int, seed: int) -> bool:
        """
        Generate a single BPPS instance.
        
        Args:
            d: Bin capacity
            n: Number of items
            m: Number of classes
            v1: Minimum item weight fraction of capacity
            v2: Maximum item weight fraction of capacity
            s1: Minimum setup weight fraction of capacity
            s2: Maximum setup weight fraction of capacity
            f: Setup cost flag (0 or 1)
            seed: Random seed
            
        Returns:
            True if instance was successfully generated, False otherwise
        """
        # Calculate weight ranges
        w_min = floor(d * v1)
        w_max = ceil(d * v2)
        s_min = floor(d * s1)
        s_max = ceil(d * s2)
        
        # Attempt to generate valid instance
        found = False
        k = 0
        max_attempts = 1000  # Prevent infinite loops
        
        while not found and k < max_attempts:
            random.seed(seed + k)

            # Initialize data structures
            items = []
            classes = {cl: [] for cl in range(m)}
            setups = {cl: 0 for cl in range(m)}
            
            # Generate setup costs and bin cost
            if f == 0:
                setup_costs = {cl: 0 for cl in range(m)}
                bin_cost = 1
            else:
                setup_costs = {cl: random.randint(1, 5) for cl in range(m)}
                bin_cost = 10
            
            # Assign items to classes
            for j in range(n):
                class_id = random.randint(0, m - 1)
                item_weight = random.randint(w_min, w_max)
                classes[class_id].append(item_weight)
            
            # Flatten items list (ordered by class)
            for cl in classes:
                for item_weight in classes[cl]:
                    items.append(item_weight)
            
            # Generate setup weights
            for cl in classes:
                setup_weight = random.randint(s_min, s_max)
                setups[cl] = setup_weight
            
            # Check if all classes have at least min_items_per_class items
            if min([len(classes[i]) for i in range(m)]) >= self.config.min_items_per_class:
                found = True
                self._write_instance_file(
                    d, n, m, w_min, w_max, s_min, s_max, f, seed,
                    bin_cost, classes, setup_costs, setups, items
                )
            
            k += 1
        
        return found
    
    def _write_instance_file(self, d: int, n: int, m: int, w_min: int, w_max: int,
                           s_min: int, s_max: int, f: int, seed: int,
                           bin_cost: int, classes: Dict[int, List[int]],
                           setup_costs: Dict[int, int], setups: Dict[int, int],
                           items: List[int]) -> None:
        """
        Write instance data to file.
        
        Args:
            d: Bin capacity
            n: Number of items
            m: Number of classes
            w_min: Minimum item weight
            w_max: Maximum item weight
            s_min: Minimum setup weight
            s_max: Maximum setup weight
            f: Setup cost flag
            seed: Random seed
            bin_cost: Cost of using a bin
            classes: Dictionary mapping class IDs to item weights
            setup_costs: Dictionary mapping class IDs to setup costs
            setups: Dictionary mapping class IDs to setup weights
            items: List of all item weights
        """
        filename = self._generate_filename(d, n, m, w_min, w_max, s_min, s_max, f, seed)
        filepath = Path(self.config.output_directory) / filename
        
        with open(filepath, 'w') as file:
            # Write header: number of items, number of classes, bin capacity, bin cost
            file.write(f'{n}\t{m}\t{d}\t{bin_cost}\n')
            
            # Write class definitions: setup cost (negative), setup weight, item count
            for cl in range(m):
                if classes[cl]:  # Only write non-empty classes
                    file.write(f'{-setup_costs[cl]}\t{setups[cl]}\t{len(classes[cl])}\n')
            
            # Write item weights (one per line)
            for item_weight in items:
                file.write(f'{item_weight}\n')
    
    def generate_instances(self) -> Dict[str, Any]:
        """
        Generate all instances based on the configuration.
        
        Returns:
            Dictionary containing generation statistics
        """
        total_instances = 0
        successful_instances = 0
        failed_instances = []
        
        print("Starting BPPS instance generation...")
        print(f"Output directory: {self.config.output_directory}")
        
        for m in self.config.num_classes:
            for n in self.config.num_items:
                for d in self.config.capacities:
                    for v1, v2 in self.config.item_weight_ranges:
                        for s1, s2 in self.config.setup_weight_ranges:
                            for f in self.config.setup_cost_flags:
                                for seed in self.config.seeds:
                                    total_instances += 1
                                    
                                    success = self._generate_single_instance(
                                        d, n, m, v1, v2, s1, s2, f, seed
                                    )
                                    
                                    if success:
                                        successful_instances += 1
                                        filename = self._generate_filename(
                                            d, n, m, 
                                            floor(d * v1), ceil(d * v2),
                                            floor(d * s1), ceil(d * s2),
                                            f, seed
                                        )
                                        print(f"✓ Generated: {filename}")
                                    else:
                                        failed_instances.append({
                                            'd': d, 'n': n, 'm': m,
                                            'v1': v1, 'v2': v2, 's1': s1, 's2': s2,
                                            'f': f, 'seed': seed
                                        })
                                        print(f"✗ Failed to generate instance with parameters: "
                                              f"d={d}, n={n}, m={m}, v1={v1}, v2={v2}, "
                                              f"s1={s1}, s2={s2}, f={f}, seed={seed}")
        
        statistics = {
            'total_attempted': total_instances,
            'successful': successful_instances,
            'failed': len(failed_instances),
            'success_rate': successful_instances / total_instances * 100 if total_instances > 0 else 0,
            'failed_instances': failed_instances
        }
        
        print(f"\nGeneration completed!")
        print(f"Total attempted: {total_instances}")
        print(f"Successful: {successful_instances}")
        print(f"Failed: {len(failed_instances)}")
        print(f"Success rate: {statistics['success_rate']:.2f}%")
        
        return statistics


def create_default_config() -> InstanceConfig:
    """Create default configuration matching the original notebook parameters."""
    return InstanceConfig(
        capacities=[200, 1000, 10000],
        num_items=[25, 50, 75, 100, 200],
        num_classes=[5, 10],
        item_weight_ranges=[(0.05, 0.15), (0.15, 0.30)],  # small_items, big_items
        setup_weight_ranges=[(0.01, 0.10), (0.10, 0.20)],  # small_classes, big_classes
        setup_cost_flags=[0, 1],
        seeds=[0, 1],
        min_items_per_class=2,
        output_directory="./generated_instances"
    )


def load_config_from_file(config_path: str) -> InstanceConfig:
    """
    Load configuration from JSON file.
    
    Args:
        config_path: Path to JSON configuration file
        
    Returns:
        Instance configuration
    """
    with open(config_path, 'r') as file:
        config_dict = json.load(file)
    return InstanceConfig.from_dict(config_dict)


def save_config_to_file(config: InstanceConfig, config_path: str) -> None:
    """
    Save configuration to JSON file.
    
    Args:
        config: Instance configuration
        config_path: Path to save JSON configuration file
    """
    with open(config_path, 'w') as file:
        json.dump(config.to_dict(), file, indent=2)


def main():
    """Main function for command-line interface."""
    parser = argparse.ArgumentParser(
        description="Generate BPPS (Bin Packing Problem with Setups) instances"
    )
    parser.add_argument(
        '--config', '-c',
        type=str,
        help='Path to JSON configuration file'
    )
    parser.add_argument(
        '--save-default-config',
        type=str,
        help='Save default configuration to specified JSON file and exit'
    )
    parser.add_argument(
        '--output-dir', '-o',
        type=str,
        help='Output directory for generated instances (overrides config file)'
    )
    
    args = parser.parse_args()
    
    # Handle saving default configuration
    if args.save_default_config:
        default_config = create_default_config()
        save_config_to_file(default_config, args.save_default_config)
        print(f"Default configuration saved to {args.save_default_config}")
        return
    
    # Load configuration
    if args.config:
        config = load_config_from_file(args.config)
        print(f"Loaded configuration from {args.config}")
    else:
        config = create_default_config()
        print("Using default configuration")
    
    # Override output directory only if explicitly specified
    if args.output_dir is not None:
        config.output_directory = args.output_dir
        print(f"Output directory overridden to: {args.output_dir}")
    
    # Generate instances
    generator = BPPSInstanceGenerator(config)
    statistics = generator.generate_instances()
    
    # Save generation statistics
    stats_path = Path(config.output_directory) / "generation_statistics.json"
    with open(stats_path, 'w') as file:
        json.dump(statistics, file, indent=2)
    print(f"Generation statistics saved to {stats_path}")


if __name__ == "__main__":
    main()
