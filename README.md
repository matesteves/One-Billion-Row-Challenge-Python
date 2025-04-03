# Project: [Your Project Name]

## Introduction
This project aims to efficiently process a large dataset containing temperature measurements from various weather stations. The main challenge is to compute statistics such as minimum, mean (rounded to one decimal place), and maximum temperature for each station, presenting the results in a table sorted by station name.

Each line of the input file follows the format:
```
<string: station name>;<double: measurement>
```
Example:
```
Hamburg;12.0
Bulawayo;8.9
Palembang;38.8
St. Johns;15.2
```

## Technologies Used
The project utilizes different approaches for data processing, leveraging various optimized libraries for efficiency:
- **Pure Python**
- **Pandas**
- **Dask**
- **Polars**
- **DuckDB**

## Dependencies
To run the project, install the following dependencies:
```
polars==0.20.3
duckdb==0.10.0
dask[complete]==2024.2.0
```

## How to Run
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repository.git
   cd your-repository
   ```
2. Set up the Python environment:
   ```sh
   pyenv local 3.12.1
   poetry env use 3.12.1
   poetry install --no-root
   poetry lock --no-update
   ```
3. Generate the test file:
   ```sh
   python src/create_measurements.py
   ```
   **Note:** This process may take a few minutes.
4. Run the different scripts to compare performance:
   ```sh
   python src/using_python.py
   python src/using_pandas.py
   python src/using_dask.py
   python src/using_polars.py
   python src/using_duckdb.py
   ```

## Results
Tests were conducted on a **Windows machine with a Ryzen 7 5800X processor and 32GB RAM**. Below are the execution times for processing a **1-billion-row (~16GB) file**:

| Implementation   | Time (seconds) |
|-----------------|---------------|
| Pure Python     | 1490.54       |
| Pandas          | 274.37        |
| Dask            | 163.44        |
| Polars          | 34.00         |
| DuckDB          | 15.21         |

## Conclusion
The project highlights the importance of selecting the right tool for large-scale data processing. While traditional approaches (Bash, Pure Python, and Pandas) require manual optimizations, modern libraries such as Dask, Polars, and DuckDB provide more efficient and scalable solutions.

**DuckDB** demonstrated the best performance, standing out as one of the top choices for this type of analysis.

## License
This project is licensed under the [MIT License](LICENSE).

