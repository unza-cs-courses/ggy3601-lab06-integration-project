# Your Assignment Parameters

These are your unique values for Lab 6: Integration Project. Use these exact values in your code.

## Project Configuration

| Parameter | Your Value |
|-----------|------------|
| Project Name | {project_name} |
| Number of Drillholes | {num_drillholes} |
| Target Grade (Economic Cutoff) | {target_grade} g/t |
| Total Samples in Dataset | {num_samples} |

## Project Overview

You are building a complete data analysis pipeline for the **{project_name}** prospect. Your pipeline will process geological drilling data to identify economic mineralization zones.

## Pipeline Configuration

Use these configuration values in your `main.py`:

```python
config = {
    'input_file': 'data/prospect_data.csv',
    'output_dir': 'output',
    'project_name': '{project_name}',
    'target_grade': {target_grade},
    'drillholes': None  # Analyze all {num_drillholes} drillholes
}
```

## Module 1: Data Loading (15 marks)

Create `src/data_loader.py` with functions to load and validate the prospect data:

```python
"""
Data Loader Module for {project_name}
Handles CSV loading, validation, and cleaning.
"""
import pandas as pd


def load_prospect_data(filepath: str) -> pd.DataFrame:
    """
    Load CSV data and return a DataFrame.

    Args:
        filepath: Path to the CSV file

    Returns:
        DataFrame containing the raw data
    """
    # TODO: Implement this function
    pass


def validate_data(df: pd.DataFrame) -> dict:
    """
    Validate data quality and return validation report.

    Expected dataset size: approximately {num_samples} samples
    across {num_drillholes} drillholes.

    Returns dict with keys:
    - 'total_records': int - total number of records
    - 'valid_records': int - records with no issues
    - 'missing_values': dict of column -> count of missing values
    - 'invalid_grades': int - count of negative or > 100 grade values
    - 'invalid_depths': int - count of negative depth values
    """
    # TODO: Implement validation logic
    pass


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove invalid records and handle missing values.

    Cleaning steps:
    1. Remove rows with negative grades
    2. Remove rows with negative depths
    3. Fill missing numeric values with column median
    4. Remove duplicate sample_ids

    Returns:
        Cleaned DataFrame
    """
    # TODO: Implement cleaning logic
    pass
```

## Module 2: Data Processing (20 marks)

Create `src/data_processor.py` with functions for calculations:

```python
"""
Data Processor Module for {project_name}
Handles calculations and data transformations.
"""
import pandas as pd


def calculate_density(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add 'density' column calculated from mass/volume.

    Formula: density = mass / volume

    Returns:
        DataFrame with new 'density' column
    """
    # TODO: Implement calculation
    pass


def classify_grade(df: pd.DataFrame, cutoff: float) -> pd.DataFrame:
    """
    Add 'grade_class' column based on cutoff grade.

    Your cutoff grade: {target_grade} g/t

    Classification rules:
    - 'High Grade': grade >= 2 * cutoff
    - 'Medium Grade': cutoff <= grade < 2 * cutoff
    - 'Low Grade': grade < cutoff

    Returns:
        DataFrame with new 'grade_class' column
    """
    # TODO: Implement classification
    pass


def calculate_intervals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add 'interval' column as (to_depth - from_depth).

    Returns:
        DataFrame with new 'interval' column
    """
    # TODO: Implement calculation
    pass


def filter_by_drillhole(df: pd.DataFrame, hole_ids: list) -> pd.DataFrame:
    """
    Filter DataFrame to include only specified drillholes.

    Your project has {num_drillholes} drillholes.

    Returns:
        Filtered DataFrame
    """
    # TODO: Implement filtering
    pass
```

## Module 3: Statistical Analysis (20 marks)

Create `src/analyzer.py` with functions for analysis:

```python
"""
Analyzer Module for {project_name}
Handles statistical analysis and grouping operations.
"""
import pandas as pd


def summary_statistics(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Calculate mean, std, min, max, median for specified columns.

    Returns:
        DataFrame with statistics as index and columns as columns
    """
    # TODO: Implement statistics calculation
    pass


def grade_by_drillhole(df: pd.DataFrame) -> pd.DataFrame:
    """
    Group by hole_id and calculate grade statistics.

    Your project has {num_drillholes} drillholes to analyze.

    Returns:
        DataFrame with drillhole statistics (mean, std, min, max, count)
    """
    # TODO: Implement groupby analysis
    pass


def correlation_analysis(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Calculate correlation matrix for specified numeric columns.

    Returns:
        Correlation matrix as DataFrame
    """
    # TODO: Implement correlation analysis
    pass


def identify_high_grade_zones(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """
    Return records where grade exceeds threshold.

    Your target grade threshold: {target_grade} g/t

    Returns:
        DataFrame containing only high-grade samples
    """
    # TODO: Implement filtering
    pass
```

## Module 4: Visualization (20 marks)

Create `src/visualizer.py` with functions to create charts:

```python
"""
Visualizer Module for {project_name}
Creates charts and plots for analysis results.
"""
import pandas as pd
import matplotlib.pyplot as plt


def plot_grade_histogram(df: pd.DataFrame, output_path: str) -> None:
    """
    Create histogram of grade distribution and save to file.

    Args:
        df: DataFrame with 'grade' column
        output_path: Path to save the figure (e.g., 'output/grade_histogram.png')
    """
    # TODO: Implement histogram
    pass


def plot_depth_vs_grade(df: pd.DataFrame, output_path: str) -> None:
    """
    Create scatter plot of depth vs grade and save to file.

    Args:
        df: DataFrame with 'from_depth' and 'grade' columns
        output_path: Path to save the figure
    """
    # TODO: Implement scatter plot
    pass


def plot_grade_by_drillhole(df: pd.DataFrame, output_path: str) -> None:
    """
    Create box plot of grade by drillhole and save to file.

    Your project has {num_drillholes} drillholes to visualize.

    Args:
        df: DataFrame with 'hole_id' and 'grade' columns
        output_path: Path to save the figure
    """
    # TODO: Implement box plot
    pass


def plot_correlation_heatmap(corr_matrix: pd.DataFrame, output_path: str) -> None:
    """
    Create correlation heatmap and save to file.

    Args:
        corr_matrix: Correlation matrix DataFrame
        output_path: Path to save the figure
    """
    # TODO: Implement heatmap
    pass
```

## Module 5: Reporting (10 marks)

Create `src/reporter.py` with functions to generate reports:

```python
"""
Reporter Module for {project_name}
Generates summary reports and exports data.
"""
import pandas as pd


def generate_summary_report(
    validation_report: dict,
    statistics: pd.DataFrame,
    high_grade_count: int,
    project_name: str
) -> str:
    """
    Generate a markdown summary report.

    Project: {project_name}

    Returns:
        Markdown-formatted report string
    """
    # TODO: Implement report generation
    pass


def save_report(content: str, output_path: str) -> None:
    """
    Save report content to a file.

    Args:
        content: Report content string
        output_path: Path to save the report
    """
    # TODO: Implement file writing
    pass


def export_processed_data(df: pd.DataFrame, output_path: str) -> None:
    """
    Export processed DataFrame to CSV.

    Args:
        df: Processed DataFrame
        output_path: Path to save the CSV
    """
    # TODO: Implement CSV export
    pass
```

## Module 6: Main Pipeline (15 marks)

Create `src/main.py` that integrates all modules:

```python
"""
Main Pipeline for {project_name}
Integrates all modules into a complete analysis workflow.
"""
import os
from data_loader import load_prospect_data, validate_data, clean_data
from data_processor import calculate_density, classify_grade, calculate_intervals
from analyzer import summary_statistics, grade_by_drillhole, correlation_analysis, identify_high_grade_zones
from visualizer import plot_grade_histogram, plot_depth_vs_grade, plot_grade_by_drillhole, plot_correlation_heatmap
from reporter import generate_summary_report, save_report, export_processed_data


def run_pipeline(config: dict) -> dict:
    """
    Execute the complete analysis pipeline for {project_name}.

    Pipeline steps:
    1. Load and validate data
    2. Clean data
    3. Process and calculate derived columns
    4. Perform statistical analysis
    5. Generate visualizations
    6. Create summary report

    Args:
        config: dict with keys:
            - 'input_file': path to input CSV
            - 'output_dir': directory for outputs
            - 'project_name': project name ('{project_name}')
            - 'target_grade': economic cutoff grade ({target_grade})
            - 'drillholes': list of drillhole IDs to analyze (None = all)

    Returns:
        dict with pipeline results including:
        - 'validation': validation report
        - 'statistics': summary statistics
        - 'high_grade_count': number of high-grade samples
        - 'output_files': list of generated files
    """
    # TODO: Implement the complete pipeline
    pass


if __name__ == "__main__":
    # Configuration for {project_name}
    config = {
        'input_file': 'data/prospect_data.csv',
        'output_dir': 'output',
        'project_name': '{project_name}',
        'target_grade': {target_grade},
        'drillholes': None  # Analyze all {num_drillholes} drillholes
    }

    print(f"Starting analysis pipeline for {config['project_name']}...")
    results = run_pipeline(config)
    print("Pipeline completed successfully!")
    print(f"Processed {results['validation']['valid_records']} valid records")
    print(f"Found {results['high_grade_count']} high-grade samples")
```

## Expected Output Files

When your pipeline runs successfully, it should generate:

```
output/
├── prospect_report.md        # Summary report
├── processed_data.csv        # Cleaned and processed data
├── grade_histogram.png       # Grade distribution
├── depth_vs_grade.png        # Depth-grade scatter plot
├── grade_by_drillhole.png    # Box plot by drillhole
└── correlation_heatmap.png   # Correlation matrix visualization
```

## Testing Your Code

Run the automated tests locally:

```bash
# Run all tests
pytest tests/visible/ -v

# Run tests for specific modules
pytest tests/visible/test_lab6.py::TestDataLoader -v
pytest tests/visible/test_lab6.py::TestDataProcessor -v
pytest tests/visible/test_lab6.py::TestAnalyzer -v
pytest tests/visible/test_lab6.py::TestVisualizer -v
pytest tests/visible/test_lab6.py::TestReporter -v
pytest tests/visible/test_lab6.py::TestPipeline -v
```

## Submission Checklist

Before submitting, ensure:

- [ ] All six modules are implemented (`data_loader.py`, `data_processor.py`, `analyzer.py`, `visualizer.py`, `reporter.py`, `main.py`)
- [ ] All functions have proper docstrings
- [ ] Pipeline runs without errors
- [ ] All visible tests pass
- [ ] Output files are generated correctly
- [ ] Code uses your assigned values: Project=`{project_name}`, Target Grade=`{target_grade}`
