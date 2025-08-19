#!/usr/bin/env python3
"""
Example usage of the BPPS Instance Generator

This script demonstrates different ways to use the BPPS instance generator.
"""

from bpps_instance_generator import InstanceConfig, BPPSInstanceGenerator, create_default_config


def example_basic_usage():
    """Example 1: Basic usage with default configuration."""
    print("=" * 60)
    print("Example 1: Basic usage with default configuration")
    print("=" * 60)
    
    config = create_default_config()
    # Modify to generate fewer instances for demo
    config.capacities = [200]
    config.num_items = [25]
    config.num_classes = [5]
    config.seeds = [0]
    config.output_directory = "./demo_instances_basic"
    
    generator = BPPSInstanceGenerator(config)
    stats = generator.generate_instances()
    
    print(f"Generated {stats['successful']} out of {stats['total_attempted']} instances")


def example_custom_configuration():
    """Example 2: Custom configuration with specific parameters."""
    print("\n" + "=" * 60)
    print("Example 2: Custom configuration")
    print("=" * 60)
    
    # Create custom configuration
    config = InstanceConfig(
        capacities=[100, 500],
        num_items=[20, 40],
        num_classes=[3, 6],
        item_weight_ranges=[(0.1, 0.2), (0.3, 0.5)],  # Light and heavy items
        setup_weight_ranges=[(0.05, 0.15), (0.2, 0.3)],  # Small and large setups
        setup_fee_flags=[0, 1],  # Both with and without setup costs
        seeds=[0, 1],
        min_items_per_class=2,
        output_directory="./demo_instances_custom"
    )
    
    generator = BPPSInstanceGenerator(config)
    stats = generator.generate_instances()
    
    print(f"Generated {stats['successful']} out of {stats['total_attempted']} instances")
    if stats['failed'] > 0:
        print(f"Failed to generate {stats['failed']} instances")


def example_single_configuration():
    """Example 3: Generate instances for a specific scenario."""
    print("\n" + "=" * 60)
    print("Example 3: Single scenario with multiple seeds")
    print("=" * 60)
    
    config = InstanceConfig(
        capacities=[1000],  # Medium capacity
        num_items=[50],     # Medium number of items
        num_classes=[8],    # Medium number of classes
        item_weight_ranges=[(0.1, 0.25)],  # Medium-sized items
        setup_weight_ranges=[(0.05, 0.12)],  # Small setup weights
        setup_fee_flags=[1],  # With setup costs
        seeds=list(range(5)),  # Multiple seeds for variation
        min_items_per_class=3,  # Slightly higher minimum
        output_directory="./demo_instances_single"
    )
    
    generator = BPPSInstanceGenerator(config)
    stats = generator.generate_instances()
    
    print(f"Generated {stats['successful']} out of {stats['total_attempted']} instances")
    print(f"Success rate: {stats['success_rate']:.1f}%")


def main():
    """Run all examples."""
    print("BPPS Instance Generator - Usage Examples")
    print("This script demonstrates various ways to use the generator.\n")
    
    try:
        example_basic_usage()
        example_custom_configuration()
        example_single_configuration()
        
        print("\n" + "=" * 60)
        print("All examples completed successfully!")
        print("Check the demo_instances_* directories for generated instances.")
        print("=" * 60)
        
    except Exception as e:
        print(f"Error during generation: {e}")


if __name__ == "__main__":
    main()
