#!/usr/bin/env python3
"""
Variant Generator for GGY3601 GitHub Classroom Assignments
Generates deterministic, unique assignment parameters per student.
"""

import hashlib
import random
import json
import csv
from typing import Any, Dict, List, Optional, Callable
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class VariantConfig:
    """Configuration for variant generation."""
    assignment_id: str
    variant_strategy: str  # 'unique', 'grouped', 'hybrid'
    num_groups: int = 10   # For grouped/hybrid strategies
    seed_salt: str = "GGY3601_2025"  # Course-specific salt


@dataclass
class StudentVariant:
    """Generated variant for a student."""
    student_id: str
    variant_seed: int
    group_id: Optional[int]
    parameters: Dict[str, Any]


class VariantGenerator:
    """Generates unique, deterministic variants for students."""

    def __init__(self, config: VariantConfig):
        self.config = config

    def _compute_seed(self, student_id: str) -> int:
        """Compute deterministic seed from student identifier."""
        combined = f"{self.config.assignment_id}:{self.config.seed_salt}:{student_id}"
        hash_bytes = hashlib.sha256(combined.encode()).digest()
        return int.from_bytes(hash_bytes[:8], byteorder='big')

    def _compute_group(self, seed: int) -> int:
        """Assign student to a variant group."""
        return seed % self.config.num_groups

    def generate_variant(
        self,
        student_id: str,
        param_generators: Dict[str, Callable]
    ) -> StudentVariant:
        """
        Generate a variant for a student.

        Args:
            student_id: Student's ID or GitHub username
            param_generators: Dict of parameter names to generator functions
                             Each function takes (random_instance, group_id) and returns a value

        Returns:
            StudentVariant with all generated parameters
        """
        seed = self._compute_seed(student_id)
        group_id = self._compute_group(seed) if self.config.variant_strategy != 'unique' else None

        # Create seeded random instance for reproducibility
        rng = random.Random(seed)

        # Generate parameters
        parameters = {}
        for param_name, generator_func in param_generators.items():
            parameters[param_name] = generator_func(rng, group_id)

        return StudentVariant(
            student_id=student_id,
            variant_seed=seed,
            group_id=group_id,
            parameters=parameters
        )

    def generate_batch(
        self,
        student_ids: List[str],
        param_generators: Dict[str, Callable]
    ) -> List[StudentVariant]:
        """Generate variants for multiple students."""
        return [self.generate_variant(sid, param_generators) for sid in student_ids]


# ============================================================================
# GGY3601 ASSIGNMENT-SPECIFIC GENERATORS
# ============================================================================

def create_lab01_generators() -> Dict[str, Callable]:
    """Generators for Lab 1: Python Fundamentals."""

    def sample_depth(rng: random.Random, group_id: int) -> int:
        """Generate unique sample depth for calculations."""
        return rng.randint(150, 450)

    def sample_mass(rng: random.Random, group_id: int) -> float:
        """Generate unique sample mass."""
        return round(rng.uniform(10.0, 25.0), 1)

    def sample_volume(rng: random.Random, group_id: int) -> float:
        """Generate unique sample volume."""
        return round(rng.uniform(3.0, 8.0), 1)

    def rock_type(rng: random.Random, group_id: int) -> str:
        """Select rock type for examples."""
        return rng.choice(['Granite', 'Basalt', 'Sandstone', 'Schist', 'Gneiss'])

    def grade_value(rng: random.Random, group_id: int) -> float:
        """Generate grade value for classification."""
        return round(rng.uniform(0.5, 4.5), 2)

    return {
        'sample_depth': sample_depth,
        'sample_mass': sample_mass,
        'sample_volume': sample_volume,
        'rock_type': rock_type,
        'grade_value': grade_value,
    }


def create_lab02_generators() -> Dict[str, Callable]:
    """Generators for Lab 2: Control Flow & Functions."""

    def grade_thresholds(rng: random.Random, group_id: int) -> Dict[str, float]:
        """Generate unique grade thresholds for classification."""
        base_high = rng.uniform(2.8, 3.2)
        return {
            'high': round(base_high, 1),
            'medium': round(base_high - 1.0, 1),
            'low': round(base_high - 2.0, 1),
        }

    def test_samples(rng: random.Random, group_id: int) -> List[float]:
        """Generate unique test sample grades."""
        return [round(rng.uniform(-0.5, 5.0), 1) for _ in range(8)]

    def drilling_depths(rng: random.Random, group_id: int) -> List[int]:
        """Generate drilling depth test cases."""
        return [rng.randint(100, 1200) for _ in range(4)]

    def base_rate(rng: random.Random, group_id: int) -> int:
        """Generate base drilling rate."""
        return rng.choice([45, 50, 55, 60, 65, 70, 75])

    return {
        'grade_thresholds': grade_thresholds,
        'test_samples': test_samples,
        'drilling_depths': drilling_depths,
        'base_rate': base_rate,
    }


def create_lab03_generators() -> Dict[str, Callable]:
    """Generators for Lab 3: Data Structures."""

    def sample_count(rng: random.Random, group_id: int) -> int:
        """Number of samples to process."""
        return rng.randint(8, 15)

    def rock_types(rng: random.Random, group_id: int) -> List[str]:
        """Rock types for the dataset."""
        all_types = ['Granite', 'Basalt', 'Sandstone', 'Schist', 'Gneiss', 'Quartzite', 'Diorite']
        return rng.sample(all_types, k=rng.randint(3, 5))

    def grade_range(rng: random.Random, group_id: int) -> Dict[str, float]:
        """Grade range for generated samples."""
        min_val = round(rng.uniform(0.2, 0.8), 1)
        return {'min': min_val, 'max': round(min_val + rng.uniform(3.0, 5.0), 1)}

    return {
        'sample_count': sample_count,
        'rock_types': rock_types,
        'grade_range': grade_range,
    }


def create_lab04_generators() -> Dict[str, Callable]:
    """Generators for Lab 4: File I/O & CSV Processing."""

    def num_records(rng: random.Random, group_id: int) -> int:
        """Number of records in generated CSV."""
        return rng.randint(40, 60)

    def locations(rng: random.Random, group_id: int) -> List[str]:
        """Site locations for the data."""
        all_sites = ['Site-A', 'Site-B', 'Site-C', 'Site-D', 'Site-E']
        return rng.sample(all_sites, k=rng.randint(2, 4))

    def depth_range(rng: random.Random, group_id: int) -> Dict[str, int]:
        """Depth range for samples."""
        min_d = rng.randint(50, 150)
        return {'min': min_d, 'max': min_d + rng.randint(300, 500)}

    def include_errors(rng: random.Random, group_id: int) -> int:
        """Number of erroneous records to include."""
        return rng.randint(2, 5)

    return {
        'num_records': num_records,
        'locations': locations,
        'depth_range': depth_range,
        'include_errors': include_errors,
    }


def create_lab05_generators() -> Dict[str, Callable]:
    """Generators for Lab 5: pandas Analysis."""

    def analysis_columns(rng: random.Random, group_id: int) -> List[str]:
        """Columns to focus analysis on."""
        options = ['grade', 'depth', 'mass', 'volume', 'density']
        return rng.sample(options, k=3)

    def groupby_column(rng: random.Random, group_id: int) -> str:
        """Column to use for groupby analysis."""
        return rng.choice(['rock_type', 'location', 'analyst'])

    def filter_threshold(rng: random.Random, group_id: int) -> float:
        """Threshold value for filtering."""
        return round(rng.uniform(1.5, 3.5), 1)

    def num_records(rng: random.Random, group_id: int) -> int:
        """Number of records in dataset."""
        return rng.randint(150, 250)

    return {
        'analysis_columns': analysis_columns,
        'groupby_column': groupby_column,
        'filter_threshold': filter_threshold,
        'num_records': num_records,
    }


def create_lab06_generators() -> Dict[str, Callable]:
    """Generators for Lab 6: Integration Project."""

    def project_name(rng: random.Random, group_id: int) -> str:
        """Generate unique project name."""
        prefixes = ['Aurora', 'Copper', 'Golden', 'Silver', 'Iron', 'Zinc']
        suffixes = ['Ridge', 'Valley', 'Peak', 'Basin', 'Creek', 'Hill']
        return f"{rng.choice(prefixes)} {rng.choice(suffixes)} Project"

    def num_drillholes(rng: random.Random, group_id: int) -> int:
        """Number of drillholes in dataset."""
        return rng.randint(4, 8)

    def target_grade(rng: random.Random, group_id: int) -> float:
        """Economic cutoff grade."""
        return round(rng.uniform(1.5, 2.5), 2)

    def num_samples(rng: random.Random, group_id: int) -> int:
        """Total samples in dataset."""
        return rng.randint(250, 350)

    return {
        'project_name': project_name,
        'num_drillholes': num_drillholes,
        'target_grade': target_grade,
        'num_samples': num_samples,
    }


def create_ca01_generators() -> Dict[str, Callable]:
    """Generators for Coding Assignment 1: Geology Toolkit."""

    def commodity(rng: random.Random, group_id: int) -> str:
        """Primary commodity for ore classification."""
        return rng.choice(['gold', 'copper', 'iron'])

    def hardness_options(rng: random.Random, group_id: int) -> List[str]:
        """Rock hardness options available."""
        return rng.sample(['soft', 'medium', 'hard', 'very_hard'], k=3)

    def base_drilling_rate(rng: random.Random, group_id: int) -> int:
        """Base drilling cost per meter."""
        return rng.choice([65, 70, 75, 80, 85])

    def depth_bonus_threshold(rng: random.Random, group_id: int) -> int:
        """Depth at which bonus rate applies."""
        return rng.choice([400, 500, 600])

    def num_test_samples(rng: random.Random, group_id: int) -> int:
        """Number of test samples to process."""
        return rng.randint(45, 55)

    return {
        'commodity': commodity,
        'hardness_options': hardness_options,
        'base_drilling_rate': base_drilling_rate,
        'depth_bonus_threshold': depth_bonus_threshold,
        'num_test_samples': num_test_samples,
    }


def create_ca02_generators() -> Dict[str, Callable]:
    """Generators for Coding Assignment 2: Geochemical Analysis."""

    def primary_element(rng: random.Random, group_id: int) -> str:
        """Primary element to analyze."""
        return rng.choice(['Au', 'Cu', 'Ag', 'Fe'])

    def secondary_elements(rng: random.Random, group_id: int) -> List[str]:
        """Secondary elements to include."""
        options = ['Au', 'Cu', 'Ag', 'Fe', 'S', 'As', 'Pb', 'Zn']
        return rng.sample(options, k=3)

    def quality_filter(rng: random.Random, group_id: int) -> str:
        """Quality level to filter."""
        return rng.choice(['Good', 'Fair'])

    def anomaly_threshold_multiplier(rng: random.Random, group_id: int) -> float:
        """Multiplier for anomaly detection threshold."""
        return round(rng.uniform(2.0, 3.0), 1)

    def num_assays(rng: random.Random, group_id: int) -> int:
        """Number of assay records."""
        return rng.randint(450, 550)

    return {
        'primary_element': primary_element,
        'secondary_elements': secondary_elements,
        'quality_filter': quality_filter,
        'anomaly_threshold_multiplier': anomaly_threshold_multiplier,
        'num_assays': num_assays,
    }


def create_miniproject_generators() -> Dict[str, Callable]:
    """Generators for Mini-Project: Field Sample Pipeline."""

    def study_area(rng: random.Random, group_id: int) -> str:
        """Study area name."""
        areas = ['Northern Zone', 'Eastern Block', 'Western Prospect',
                 'Central Basin', 'Southern Ridge']
        return rng.choice(areas)

    def target_elements(rng: random.Random, group_id: int) -> List[str]:
        """Elements to analyze."""
        return rng.sample(['Au', 'Cu', 'Pb', 'Zn', 'As'], k=3)

    def collector_filter(rng: random.Random, group_id: int) -> str:
        """Collector to filter for analysis."""
        return rng.choice(['A. Smith', 'B. Johnson', 'C. Williams', 'D. Brown'])

    def elevation_range(rng: random.Random, group_id: int) -> Dict[str, int]:
        """Elevation range for analysis."""
        base = rng.randint(1200, 1400)
        return {'min': base, 'max': base + rng.randint(300, 500)}

    def anomaly_percentile(rng: random.Random, group_id: int) -> int:
        """Percentile threshold for anomalies."""
        return rng.choice([90, 95])

    def num_samples(rng: random.Random, group_id: int) -> int:
        """Number of field samples."""
        return rng.randint(750, 850)

    return {
        'study_area': study_area,
        'target_elements': target_elements,
        'collector_filter': collector_filter,
        'elevation_range': elevation_range,
        'anomaly_percentile': anomaly_percentile,
        'num_samples': num_samples,
    }


# ============================================================================
# DATA GENERATION
# ============================================================================

def generate_sample_data(variant: StudentVariant, output_path: Path, assignment_type: str):
    """Generate student-specific CSV data files based on variant parameters."""
    rng = random.Random(variant.variant_seed)

    if assignment_type in ['lab04', 'lab05', 'ca01']:
        # Generate samples.csv style data
        num_records = variant.parameters.get('num_records', 50)
        locations = variant.parameters.get('locations', ['Site-A', 'Site-B'])
        depth_range = variant.parameters.get('depth_range', {'min': 50, 'max': 500})

        rock_types = ['Granite', 'Basalt', 'Sandstone', 'Schist', 'Gneiss']

        with open(output_path / 'samples.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['sample_id', 'rock_type', 'grade', 'depth', 'mass', 'location'])

            for i in range(1, num_records + 1):
                sample_id = f"GEO-{i:03d}"
                rock = rng.choice(rock_types)
                grade = round(rng.uniform(0.3, 5.0), 2)
                depth = rng.randint(depth_range['min'], depth_range['max'])
                mass = round(rng.uniform(8.0, 20.0), 1)
                location = rng.choice(locations)

                writer.writerow([sample_id, rock, grade, depth, mass, location])

    elif assignment_type == 'ca02':
        # Generate geochemical assay data
        num_assays = variant.parameters.get('num_assays', 500)

        lithologies = ['Granite', 'Basalt', 'Schist', 'Quartzite', 'Gneiss']
        qualities = ['Good', 'Fair', 'Rejected']

        with open(output_path / 'geochemical_assays.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['sample_id', 'hole_id', 'from_depth', 'to_depth', 'lithology',
                           'Au_ppm', 'Cu_pct', 'Ag_ppm', 'Fe_pct', 'S_pct', 'sample_quality', 'assay_date'])

            for i in range(1, num_assays + 1):
                sample_id = f"ASY-{i:04d}"
                hole_id = f"DH-{rng.randint(1, 5):02d}"
                from_depth = rng.randint(10, 450)
                to_depth = from_depth + rng.randint(1, 4)
                lithology = rng.choice(lithologies)

                # Some missing values
                au = round(rng.uniform(0.01, 6.0), 3) if rng.random() > 0.05 else ''
                cu = round(rng.uniform(0.1, 3.0), 3) if rng.random() > 0.05 else ''
                ag = round(rng.uniform(1.0, 15.0), 2) if rng.random() > 0.05 else ''
                fe = round(rng.uniform(3.0, 12.0), 2)
                s = round(rng.uniform(0.2, 4.5), 2)
                quality = rng.choice(qualities)
                date = f"2024-{rng.randint(1,12):02d}-{rng.randint(1,28):02d}"

                writer.writerow([sample_id, hole_id, from_depth, to_depth, lithology,
                               au, cu, ag, fe, s, quality, date])


def generate_variant_config_file(variant: StudentVariant) -> str:
    """Generate a JSON config file for tests to read."""
    return json.dumps(asdict(variant), indent=2)


def generate_student_readme(variant: StudentVariant, template: str) -> str:
    """Generate personalized README for a student."""
    content = template
    for param_name, param_value in variant.parameters.items():
        placeholder = f"{{{param_name}}}"
        if isinstance(param_value, list):
            value_str = ", ".join(str(v) for v in param_value)
        elif isinstance(param_value, dict):
            value_str = json.dumps(param_value)
        else:
            value_str = str(param_value)
        content = content.replace(placeholder, value_str)

    # Add variant metadata as HTML comment
    metadata = f"""<!--
VARIANT_METADATA
Student: {variant.student_id}
Seed: {variant.variant_seed}
Group: {variant.group_id}
Generated: AUTO
DO NOT MODIFY THIS COMMENT
-->"""
    return metadata + "\n\n" + content


# ============================================================================
# ASSIGNMENT MAPPING
# ============================================================================

ASSIGNMENT_GENERATORS = {
    'lab01': create_lab01_generators,
    'lab02': create_lab02_generators,
    'lab03': create_lab03_generators,
    'lab04': create_lab04_generators,
    'lab05': create_lab05_generators,
    'lab06': create_lab06_generators,
    'ca01': create_ca01_generators,
    'ca02': create_ca02_generators,
    'miniproject': create_miniproject_generators,
}


# ============================================================================
# CLI INTERFACE
# ============================================================================

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate GGY3601 assignment variants")
    parser.add_argument("--assignment", required=True,
                        choices=list(ASSIGNMENT_GENERATORS.keys()),
                        help="Assignment ID")
    parser.add_argument("--student", required=True,
                        help="Student ID or GitHub username")
    parser.add_argument("--strategy", default="grouped",
                        choices=['unique', 'grouped', 'hybrid'])
    parser.add_argument("--groups", type=int, default=10,
                        help="Number of variant groups")
    parser.add_argument("--output", default="json",
                        choices=['json', 'config'])
    parser.add_argument("--output-dir", type=Path, default=None,
                        help="Directory to write generated data files")

    args = parser.parse_args()

    config = VariantConfig(
        assignment_id=args.assignment,
        variant_strategy=args.strategy,
        num_groups=args.groups,
    )

    generator = VariantGenerator(config)
    param_generators = ASSIGNMENT_GENERATORS[args.assignment]()
    variant = generator.generate_variant(args.student, param_generators)

    if args.output == 'json':
        print(json.dumps(asdict(variant), indent=2))
    elif args.output == 'config':
        print(generate_variant_config_file(variant))

    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        generate_sample_data(variant, args.output_dir, args.assignment)
        with open(args.output_dir / '.variant_config.json', 'w') as f:
            f.write(generate_variant_config_file(variant))
        print(f"Data files generated in: {args.output_dir}")
