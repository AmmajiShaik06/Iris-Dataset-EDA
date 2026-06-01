# Exploratory Data Analysis (EDA) on Iris Dataset

This project demonstrates how to perform automated Exploratory Data Analysis (EDA) using Python. It utilizes the Iris dataset, leveraging Pandas for data manipulation and "ydata-profiling" to generate an interactive, comprehensive HTML analysis report.

## Features

- Automated Reporting: Generates a complete EDA report with one line of code.
- Dataset Insights: Highlights missing values, duplicate rows, and data types.
- Visualizations: Includes distribution plots, correlation matrices, and interaction charts.
- Descriptive Statistics: Calculates mean, median, mode, variance, and standard deviation automatically.

## Prerequisites

Ensure you have Python installed on your system. You will need to install the following libraries:

```bash 
 pip install pandas ydata-profiling

## Dataset

The project uses the classic "Iris Dataset". It contains 150 samples from three species of Iris flowers (Iris setosa, Iris virginica, and Iris versicolor). Four features were measured from each sample:
- Sepal length (cm)
- Sepal width (cm)
- Petal length (cm)
- Petal width (cm)


## Usage

Save the following code as `eda_script.py` and run it in your Python/Jupyter notebook


## Output

Running the script creates a file named `iris_eda_report.html` in your working directory. Open this file in any web browser to explore:
      Overview: High-level dataset statistics.
      Variables: Detailed analysis of each feature (distributions, missing values).
      Interactions & Correlations: Visual charts showing how features relate to one another.
      Missing Values & Samples: Insights into data completeness and a preview of raw rows.

