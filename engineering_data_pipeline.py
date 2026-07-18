"""
Engineering Material Stress Analysis Pipeline
Author: Ovin Gamage
Track: Python Data Analytics & Project Management

Description:
    An end-to-end data pipeline that loads structural stress test data,
    cleans sensor anomalies, aggregates core engineering performance
    metrics across active projects, and generates visual analytical reports.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_and_clean_data(filepath):
    """
    Step 1: Ingest raw CSV data and handle structural anomalies.
    - Handles impossible negative sensor readings (-999.0).
    - Imputes missing load metrics using valid dataset averages.
    """
    print("--- Step 1: Loading & Cleaning Data ---")
    df = pd.read_csv(filepath)

    # If Max_Load_kN is less than 0, change that specific value to np.nan
    df.loc[df['Max_Load_kN'] < 0, 'Max_Load_kN'] = np.nan

    #Calculate the average of all VALID loads
    average_load=df['Max_Load_kN'].mean()
    
    

    #  Fill the missing NaN values with that average
    df=df.fillna({'Max_Load_kN':average_load})

    print("Data successfully cleaned.\n")
    return df


def aggregate_project_metrics(df):
    """
    Step 2: Group data to extract high-level engineering insights.
    - Summarizes material performance under stress.
    - Provides project managers with testing volume metrics.
    """
    print("--- Step 2: Aggregating Engineering Metrics ---")

    #  Group by 'Material_Type' and calculate mean load and total count
  

    summary_df =  df.groupby('Material_Type')['Max_Load_kN'].agg(['mean', 'count'])  

    print("Metrics compiled successfully.\n")
    return summary_df


def generate_performance_chart(summary_df):
    """
    Step 3: Transform tabular summaries into report-ready visualizations.
    - Generates a polished bar chart displaying failure profiles.
    - Applies standard engineering chart hygiene (labels, grids, limits).
    """
    print("--- Step 3: Generating Visual Reports ---")

    # Initialize the plot layout
    plt.figure(figsize=(8, 5))

    #  Create the bar chart using summary_df
    Material_type=summary_df.index
    Mean=summary_df['mean']
    plt.bar(Material_type,Mean,color="Blue")

    #  Add Title, X-label, Y-label, and a subtle grid
    plt.title("Material types and their maximum loads")
    plt.xlabel("Material")
    plt.ylabel("Maximum Load")
    plt.grid(axis='y', linestyle='--')
    


    # Save the output visualization
    output_filename = 'material_performance_report.png'
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"Chart saved successfully as '{output_filename}'.\n")
    plt.show()
    plt.close()


# The Main Execution Block
if __name__ == "__main__":
    # Define file paths
    csv_file = "material_stress_tests.csv"

    print("=== STARTING ENGINEERING DATA PIPELINE ===\n")

    # Run the pipeline sequentially
    cleaned_data = load_and_clean_data(csv_file)
    print("Cleaned Dataset preview:")
    print(cleaned_data.head(10), "\n")

    aggregated_data = aggregate_project_metrics(cleaned_data)
    print("Aggregated Material Summary:")
    print(aggregated_data, "\n")

    generate_performance_chart(aggregated_data)

    print("=== PIPELINE EXECUTION COMPLETE ===")
