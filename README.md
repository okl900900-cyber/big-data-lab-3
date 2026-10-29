# Big Data, Processing Methods — Lab Work 3

A ready-to-run implementation of the five tasks in **Introduction to Spark and PySpark DataFrames**. It uses PySpark 3.5.0, matching the Spark 3.5.x generation referenced in the lab sheet, and Java 17 in GitHub Codespaces. Spark runs in `local[*]` mode here, meaning it uses the Codespace machine rather than a multi-machine cluster; this is sufficient for the DataFrame and SQL exercises in the handout.

## What's included

- `main.py` — all five tasks plus CSV export.
- `data/sales.csv` — a small sample sales dataset with `Product`, `Quantity`, and `Price` columns.
- `requirements.txt` — pinned PySpark dependency.
- `.devcontainer/devcontainer.json` — Codespaces environment with Python 3.11 and Java 17.

> **Dataset note:** this project uses the `sales.csv` example from the lab sheet. If your teacher assigned a different dataset/variant, replace `data/sales.csv` and update the column names and operations in `main.py` to match that variant.

## Part A — Put this project in a GitHub repository

1. Download `lab3-pyspark-codespaces.zip` from this chat.
2. On GitHub, create a new repository, for example `big-data-lab-3`.
3. In the repository, choose **Add file → Upload files**, upload the ZIP, and commit it to the `main` branch.
4. Open the repository, choose **Code → Codespaces → Create codespace on main**.
5. In the Codespaces terminal, extract the archive into the repository root:

   ```bash
   python -m zipfile -e lab3-pyspark-codespaces.zip .
   ```

6. Commit the extracted project files. In the terminal you can run:

   ```bash
   git add .devcontainer data main.py requirements.txt README.md .gitignore LAB_REPORT_TEMPLATE.md
   git commit -m "Add PySpark Lab 3 project"
   git push
   ```

7. Because the `.devcontainer` configuration was inside the archive, rebuild the Codespace container so it installs Java 17 and the Python dependencies. Press `Ctrl+Shift+P`, choose **Codespaces: Rebuild Container** (or the available **Rebuild Container** command), and confirm.

The rebuild runs the `postCreateCommand` from `.devcontainer/devcontainer.json`. That creates `.venv` and installs `pyspark==3.5.0`.

## Part B — Run the lab

After the rebuild finishes, open a terminal and run:

```bash
source .venv/bin/activate
java -version
python --version
python -c "import pyspark; print('PySpark version:', pyspark.__version__)"
python main.py
```

Expected version checks include Java 17 and PySpark 3.5.0. The program prints the Spark version/application name, reads the CSV, displays the schema, filters `Quantity > 10`, adds `Total = Quantity * Price`, groups and aggregates by product, runs the equivalent SQL query, saves the query result, and stops Spark.

## Part C — Find the saved output

After running the program, open `output/sales_summary/`. Spark writes CSV output as a **directory**, not as one file. It should contain a `part-....csv` file and `_SUCCESS`. Open the `part-....csv` file to view the aggregated results.

The sample data should give these nine groups, ordered by `TotalSales` descending:

| Product | TotalSales | AveragePrice |
|---|---:|---:|
| Laptop | 9680.0 | 880.0 |
| Monitor | 6168.0 | 172.0 |
| Mouse | 1550.0 | 20.0 |
| Keyboard | 1340.0 | 42.5 |
| External SSD | 1320.0 | 110.0 |
| Webcam | 960.0 | 60.0 |
| Headphones | 825.0 | 75.0 |
| Laptop Stand | 455.0 | 35.0 |
| USB-C Cable | 400.0 | 8.0 |

`AveragePrice` is calculated only from rows that passed the `Quantity > 10` filter, because Tasks 4 and 5 use `df_new` as specified in the lab sheet.

## If something goes wrong

- **`JAVA_GATEWAY_EXITED` / Java not found:** check `java -version`; then rebuild the Codespace container and confirm the Java feature ran.
- **`ModuleNotFoundError: pyspark`:** activate `.venv` with `source .venv/bin/activate`, or reinstall with `.venv/bin/python -m pip install -r requirements.txt`.
- **Dataset not found:** run `pwd` from the repository root and check that `data/sales.csv` exists.
- **Output folder already exists:** the script uses Spark's `mode("overwrite")`, so rerunning replaces the previous result.

## Submit / capture evidence

Use `LAB_REPORT_TEMPLATE.md` as a concise report structure. Capture screenshots from the Codespaces terminal showing the version/session, schema and sample rows, filtered DataFrame, aggregate output, SQL output, and saved CSV directory. Do not claim a task succeeded until the relevant output is visible in your own Codespace.
