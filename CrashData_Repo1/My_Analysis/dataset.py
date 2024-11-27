from pathlib import Path
import pandas as pd
import typer
from loguru import logger
from tqdm import tqdm

# Import your project configuration
from My_Analysis.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()

@app.command()
def filter_years(
    input_path: Path = RAW_DATA_DIR / "raw_data.csv",
    output_path: Path = INTERIM_DATA_DIR / "filtered_dataset.csv",
):
    """
    Filters out rows from years 2013–2016 and saves the result to the interim data folder.
    """
    logger.info("Starting the filtering process...")
    try:
        # Load the dataset
        logger.info(f"Loading data from {input_path}")
        df = pd.read_csv(input_path, parse_dates=["CRASH_DATE"])

        # Filter rows with CRASH_DATE.year > 2016
        logger.info("Filtering data for years after 2016...")
        df_filtered = df[df["CRASH_DATE"].dt.year > 2016]

        # Save to output path
        logger.info(f"Saving filtered data to {output_path}")
        df_filtered.to_csv(output_path, index=False)

        logger.success("Filtering complete. Data saved successfully.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    app()