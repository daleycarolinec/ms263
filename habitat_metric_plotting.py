# habitat_metric_plotting.py
# ChatGPT was used to assist with formatting and annotation of below functions:

import os
import matplotlib.pyplot as plt
import pandas as pd

# FUNCTIONS WITHIN SITES
def plot_site_metrics(df: pd.DataFrame, location: str, output_dir: str = None):
    """
    Create boxplots comparing habitat metrics for MPA vs REF sites at a specific location.

    Parameters:
    - df (pd.DataFrame): Input data frame containing a 'Location', 'Site', and habitat metric columns.
    - location (str): The name of the location to where you'd like to plot habitat metrics 
    - output_dir (str, optional): Directory to save the figure. If None, the figure is not saved.

    Returns:
    - None
    """
    location_data = df[df['Location'] == location]

    # List of numeric columns (assumed to be habitat metrics)
    numeric_columns = location_data.select_dtypes(include=['number']).columns

    n_metrics = len(numeric_columns)
    ncols = 3  # Number of columns in subplot grid
    nrows = (n_metrics // ncols) + (1 if n_metrics % ncols > 0 else 0)

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(5 * ncols, 5 * nrows))
    axes = axes.flatten()

    for i, metric in enumerate(numeric_columns):
        mpa = location_data[location_data['Site'] == 'MPA'][metric].dropna()
        ref = location_data[location_data['Site'] == 'REF'][metric].dropna()

        axes[i].boxplot([mpa, ref],
                        labels=['MPA', 'REF'],
                        showmeans=True,
                        notch=True)
        axes[i].set_title(f"{metric}")
        axes[i].set_ylabel(metric)
        axes[i].set_xlabel("Site")

    # Hide unused subplots
    for j in range(i + 1, len(axes)):
        axes[j].axis('off')

    fig.suptitle(f"DEM Derived Benthic Habitat Metrics at {location}", fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])  # Make space for suptitle

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"habitat_metrics_{location}_plot.png")
        plt.savefig(output_path, dpi=300)
        print(f"Figure saved to: {output_path}")

    plt.show()