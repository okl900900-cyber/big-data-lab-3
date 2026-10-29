# Lab Work 3 — Introduction to Spark and PySpark DataFrames

**Name:** [Your name]  
**Group / variant:** [Your group or variant]  
**Environment:** GitHub Codespaces, Python 3.11, Java 17, PySpark 3.5.0

## Goal
Study the basics of distributed data processing with Apache Spark and PySpark DataFrames by loading, transforming, aggregating, and querying a CSV dataset.

## Task 1 — Initialize Spark and create a session
- Spark version printed by the program: [paste value]
- Application name: `SparkBasics`
- Spark master: [paste value]
- Evidence: [insert screenshot]

## Task 2 — Load the dataset into a DataFrame
- Input file: `data/sales.csv`
- CSV options: `header=True`, `inferSchema=True`
- Schema observed: `Product` (string), `Quantity` (integer), `Price` (double)
- Evidence: [insert screenshot of `show(5)` and `printSchema()`]

## Task 3 — Basic DataFrame operations
- Selected columns: `Product`, `Quantity`, `Price`
- Filter condition: `Quantity > 10`
- Computed column: `Total = Quantity * Price`
- Number of rows after filtering: [paste value]
- Evidence: [insert screenshot]

## Task 4 — Group and aggregate
The transformed DataFrame was grouped by `Product`. `TotalSales` was calculated as the sum of `Total`, and `AveragePrice` as the average of `Price`.

- Evidence / output: [insert screenshot]

## Task 5 — Spark SQL
The transformed DataFrame was registered as the temporary view `sales_table`. The SQL query grouped by product, calculated `SUM(Total)` and `AVG(Price)`, and sorted by `TotalSales` descending.

- Evidence / output: [insert screenshot]

## Save the results and stop Spark
The SQL result was written as CSV to `output/sales_summary/`. Spark's output is a directory that contains a part CSV file and `_SUCCESS`. The program then stopped the Spark session.

- Evidence of output files: [insert screenshot]

## Conclusion
In this lab, I initialized a Spark session, loaded a CSV into a DataFrame, inspected its schema, selected and filtered rows, created a computed column, performed grouped aggregation, ran an equivalent Spark SQL query, and saved the aggregated result to CSV.
