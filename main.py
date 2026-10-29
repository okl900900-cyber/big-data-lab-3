"""Lab Work 3: Introduction to Spark and PySpark DataFrames.

Run from the project root with: python main.py
"""
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, expr, sum as spark_sum, round as spark_round


PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = PROJECT_DIR / "data" / "Ecommerce.csv"
OUTPUT_PATH = PROJECT_DIR / "output" / "sales_summary"


def main() -> None:
    if not DATA_PATH.is_file():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_PATH}. Place the CSV at data/Eccommerce.csv."
        )

    # Task 1: Initialize Spark and create a session.
    spark = (
        SparkSession.builder
        .appName("SparkBasics")
        .master("local[*]")
        .getOrCreate()
    )

    try:
        spark.sparkContext.setLogLevel("ERROR")
        print("\n=== Task 1: Spark session ===")
        print("Spark version:", spark.version)
        print("Application name:", spark.sparkContext.appName)
        print("Spark master:", spark.sparkContext.master)

        # Task 2: Load the dataset, show five rows, and print its schema.
        print("\n=== Task 2: Load CSV into a DataFrame ===")
        df = spark.read.csv(
            str(DATA_PATH),
            header=True,
            inferSchema=True,
        )
        df = df.withColumn(
            "Price",
            col("Price").cast("decimal(12,2)")
        )
        df.show(5, truncate=False)
        df.printSchema()

        # Task 3: Select columns, filter rows, and add a computed column.
        print("\n=== Task 3: DataFrame operations ===")
        df_selected = df.select("Category", "Price", "Quantity")
        df_filtered = df_selected.filter(col("Quantity") > 6)
        df_new = df_filtered.withColumn("Total", (col("Quantity") * col("Price")))
        df_new.show(5, truncate=False)
        print("Rows where Quantity > 6:", df_filtered.count())

        # Task 4: Group and aggregate the transformed data.
        print("\n=== Task 4: Group and aggregate ===")
        df_agg = (
            df_new.groupBy("Category")
            .agg(
                spark_sum("Total").alias("TotalSales"),
                spark_round(avg("Price"), 2).alias("AveragePrice")
            )
        )
        df_agg.orderBy(col("TotalSales").desc()).show(truncate=False)

        # Task 5: Register a temporary view and run a Spark SQL query.
        print("\n=== Task 5: Spark SQL query ===")
        df_new.createOrReplaceTempView("sales_table")
        query = """
            SELECT
                Category,
                SUM(Total) AS TotalSales,
                ROUND(AVG(Price), 2) AS AveragePrice
            FROM sales_table
            GROUP BY Category
            ORDER BY TotalSales DESC
        """
        result = spark.sql(query)
        result.show(truncate=False)

        # Additional note in the lab: save the aggregated result as CSV.
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        result.write.mode("overwrite").option("header", True).csv(str(OUTPUT_PATH))
        print(f"\nCSV output directory: {OUTPUT_PATH.relative_to(PROJECT_DIR)}")
        print("Spark writes CSV output to a directory containing part files and _SUCCESS.")

    finally:
        # Always stop the Spark session, including if an earlier task fails.
        spark.stop()
        print("\nSpark session stopped.")


if __name__ == "__main__":
    main()
