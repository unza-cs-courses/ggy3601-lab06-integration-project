# GGY3601 Lab 6: Integration Project - Complete Data Pipeline

**Weight:** 25% of final grade
**Estimated Time:** 4-5 hours

## Purpose

This capstone lab integrates all the concepts you have learned throughout the course: Python fundamentals, control flow, data structures, file I/O, pandas analysis, and visualization. You will build a complete data analysis pipeline for geological prospect evaluation.

## Learning Outcomes

By completing this lab, you will be able to:
- LO6.1: Design modular code architecture with separate, reusable modules
- LO6.2: Integrate multiple data sources into a unified analysis workflow
- LO6.3: Build complete data analysis pipelines from raw data to insights
- LO6.4: Generate professional reports with visualizations and summary statistics

## Your Personalized Assignment

**See `ASSIGNMENT.md` for your unique parameters and project specifications.**

The ASSIGNMENT.md file contains your student-specific values including project name, number of drillholes, target grade thresholds, and sample counts. These values are unique to you and are used for automated testing.

## Repository Structure

```
.
├── src/
│   ├── data_loader.py      # Module 1: Data loading and validation
│   ├── data_processor.py   # Module 2: Data processing and calculations
│   ├── analyzer.py         # Module 3: Statistical analysis
│   ├── visualizer.py       # Module 4: Chart and plot generation
│   ├── reporter.py         # Module 5: Report generation
│   └── main.py             # Main pipeline script (integrates all modules)
├── data/
│   └── prospect_data.csv   # Input: Raw geological data
├── output/                 # Generated reports and visualizations
├── tests/
│   └── visible/            # Automated tests (visible to you)
├── ASSIGNMENT.md           # Your unique assignment parameters
└── README.md               # This file
```

## Pipeline Overview

Your pipeline will process geological prospect data through five stages:

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  DATA LOADER    │────▶│ DATA PROCESSOR  │────▶│    ANALYZER     │
│  - Load CSV     │     │ - Clean data    │     │ - Statistics    │
│  - Validate     │     │ - Calculate     │     │ - Groupby       │
│  - Report errors│     │ - Filter        │     │ - Correlations  │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
                    ┌─────────────────┐     ┌───────────▼───────┐
                    │    REPORTER     │◀────│   VISUALIZER      │
                    │  - Summary      │     │  - Histograms     │
                    │  - Markdown     │     │  - Scatter plots  │
                    │  - Export       │     │  - Box plots      │
                    └─────────────────┘     └───────────────────┘
```

## Getting Started

1. Clone this repository to your local machine
2. Read `ASSIGNMENT.md` for your unique project parameters
3. Examine the data in `data/prospect_data.csv`
4. Implement each module in the `src/` directory in order:
   - Start with `data_loader.py`
   - Then `data_processor.py`
   - Then `analyzer.py`
   - Then `visualizer.py`
   - Then `reporter.py`
   - Finally, integrate everything in `main.py`
5. Run tests locally: `pytest tests/visible/ -v`
6. Push your code to see automated test results

## Module Requirements

### Module 1: data_loader.py (15 marks)

Implement functions to load and validate geological data:

```python
def load_prospect_data(filepath: str) -> pd.DataFrame:
    """Load CSV data and return a DataFrame."""
    pass

def validate_data(df: pd.DataFrame) -> dict:
    """
    Validate data quality and return validation report.

    Returns dict with keys:
    - 'total_records': int
    - 'valid_records': int
    - 'missing_values': dict of column -> count
    - 'invalid_grades': int (negative or > 100)
    - 'invalid_depths': int (negative values)
    """
    pass

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove invalid records and handle missing values."""
    pass
```

### Module 2: data_processor.py (20 marks)

Implement functions for data processing and calculations:

```python
def calculate_density(df: pd.DataFrame) -> pd.DataFrame:
    """Add 'density' column calculated from mass/volume."""
    pass

def classify_grade(df: pd.DataFrame, cutoff: float) -> pd.DataFrame:
    """
    Add 'grade_class' column based on cutoff grade.
    Classes: 'High Grade' (>= 2x cutoff), 'Medium Grade' (>= cutoff), 'Low Grade' (< cutoff)
    """
    pass

def calculate_intervals(df: pd.DataFrame) -> pd.DataFrame:
    """Add 'interval' column as (to_depth - from_depth)."""
    pass

def filter_by_drillhole(df: pd.DataFrame, hole_ids: list) -> pd.DataFrame:
    """Filter DataFrame to include only specified drillholes."""
    pass
```

### Module 3: analyzer.py (20 marks)

Implement functions for statistical analysis:

```python
def summary_statistics(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Calculate mean, std, min, max, median for specified columns."""
    pass

def grade_by_drillhole(df: pd.DataFrame) -> pd.DataFrame:
    """Group by hole_id and calculate grade statistics."""
    pass

def correlation_analysis(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Calculate correlation matrix for specified numeric columns."""
    pass

def identify_high_grade_zones(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    """Return records where grade exceeds threshold."""
    pass
```

### Module 4: visualizer.py (20 marks)

Implement functions to create visualizations:

```python
def plot_grade_histogram(df: pd.DataFrame, output_path: str) -> None:
    """Create histogram of grade distribution and save to file."""
    pass

def plot_depth_vs_grade(df: pd.DataFrame, output_path: str) -> None:
    """Create scatter plot of depth vs grade and save to file."""
    pass

def plot_grade_by_drillhole(df: pd.DataFrame, output_path: str) -> None:
    """Create box plot of grade by drillhole and save to file."""
    pass

def plot_correlation_heatmap(corr_matrix: pd.DataFrame, output_path: str) -> None:
    """Create correlation heatmap and save to file."""
    pass
```

### Module 5: reporter.py (10 marks)

Implement functions to generate reports:

```python
def generate_summary_report(
    validation_report: dict,
    statistics: pd.DataFrame,
    high_grade_count: int,
    project_name: str
) -> str:
    """Generate a markdown summary report."""
    pass

def save_report(content: str, output_path: str) -> None:
    """Save report content to a file."""
    pass

def export_processed_data(df: pd.DataFrame, output_path: str) -> None:
    """Export processed DataFrame to CSV."""
    pass
```

### Module 6: main.py (15 marks)

Create the main pipeline that integrates all modules:

```python
def run_pipeline(config: dict) -> dict:
    """
    Execute the complete analysis pipeline.

    Args:
        config: dict with keys:
            - 'input_file': path to input CSV
            - 'output_dir': directory for outputs
            - 'project_name': project name
            - 'target_grade': economic cutoff grade
            - 'drillholes': list of drillhole IDs to analyze

    Returns:
        dict with pipeline results and statistics
    """
    pass

if __name__ == "__main__":
    # Run with default configuration
    config = {
        'input_file': 'data/prospect_data.csv',
        'output_dir': 'output',
        'project_name': 'Default Project',
        'target_grade': 2.0,
        'drillholes': None  # None means all drillholes
    }
    results = run_pipeline(config)
    print("Pipeline completed successfully!")
```

## Testing Your Code

Run the automated tests locally:

```bash
# Run all visible tests
pytest tests/visible/ -v

# Run tests for a specific module
pytest tests/visible/test_lab6.py::TestDataLoader -v
pytest tests/visible/test_lab6.py::TestDataProcessor -v
pytest tests/visible/test_lab6.py::TestAnalyzer -v
pytest tests/visible/test_lab6.py::TestVisualizer -v
pytest tests/visible/test_lab6.py::TestReporter -v
pytest tests/visible/test_lab6.py::TestPipeline -v
```

Push to GitHub to see your score on the Actions tab.

## Grading Breakdown

| Component | Marks |
|-----------|-------|
| data_loader.py | 15 |
| data_processor.py | 20 |
| analyzer.py | 20 |
| visualizer.py | 20 |
| reporter.py | 10 |
| main.py (pipeline integration) | 15 |
| **Total** | **100** |

## Tips for Success

1. **Start Early**: This is a substantial project - don't leave it until the last minute
2. **Test Incrementally**: Implement and test one module at a time
3. **Use Type Hints**: Include type hints for better code documentation
4. **Handle Edge Cases**: Consider what happens with empty DataFrames or missing columns
5. **Document Your Code**: Add docstrings explaining what each function does
6. **Check Output Formats**: Ensure your outputs match the expected formats exactly

## Submission

Push your completed code to this repository before the deadline. Your score is calculated from the automated tests.

## Academic Integrity

- **ALLOWED:** Lecture notes, official Python/pandas/matplotlib documentation, asking tutors
- **NOT ALLOWED:** Copying code, AI tools, sharing solutions

All submissions are checked with plagiarism detection software.
