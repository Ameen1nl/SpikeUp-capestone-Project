from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from pyspark.sql import SparkSession, DataFrame, functions as sf

GCS_BUCKET = "ecommerce-customer"

def read_data(spark: SparkSession, file_path: str) -> DataFrame:
    """
    Reads a CSV file from the specified Google Cloud Storage path into a PySpark DataFrame.
    
    Args:
        spark (SparkSession): An active SparkSession object.
        file_path (str): The Google Cloud Storage path to the CSV file.
    
    Returns:
        DataFrame: A PySpark DataFrame containing the data from the CSV file.
    """
    return spark.read.csv(file_path, header=True, inferSchema=True)

def calculate_highest_spend(df: DataFrame) -> DataFrame:
    """
    Calculates the average age, average items purchased, average spend and sun spend grouped by city
    and sorts the results by the average spend in descending order.
    
    Args:
        df (DataFrame): A PySpark DataFrame containing customer data with columns such as City, Gender, Membership Type,
                        Age, Items Purchased, and Total Spend.
    
    Returns:
        DataFrame: A PySpark DataFrame containing aggregated statistics, sorted by Average_spend in descending order.
    """

    Spend_by_City = (
        df.groupBy("City", "SpendingCategory")
          .agg(
              # Age calculations
              sf.round(sf.mean("age"), 1).alias("Average_age"),
             
              # Items Purchased calculations
              sf.round(sf.mean("Items Purchased"), 0).alias("Average_items_purchased"),
              
              # Total Spend calculations
              sf.round(sf.mean("Total Spend"), 2).alias("Average_spend"),
              sf.round(sf.sum("Total Spend"), 2).alias("Sum_spend")
          )
        .sort("Average_spend", ascending=False)
    )
    return Spend_by_City


def write_to_gcs(df: DataFrame, filepath: str):
    """
    Writes the given PySpark DataFrame to a CSV file in Google Cloud Storage.
    
    Args:
        df (DataFrame): A PySpark DataFrame to be written to Google Cloud Storage.
        filepath (str): The destination Google Cloud Storage path for the CSV file.
    
    Returns:
        None
    """
    df.toPandas().to_csv(filepath, index=False)

def etl_with_spark():
    """
    Executes the ETL process using PySpark:
    1. Reads customer data from a CSV file in Google Cloud Storage.
    2. Performs data transformations to calculate average statistics by city, gender, and membership type.
    3. Writes the transformed data back to Google Cloud Storage.
    
    The function initializes a Spark session, processes the data, and ensures proper resource cleanup.
    """
    spark = None
    try:
        # Initialize Spark session with GCS connector
        spark = SparkSession.builder \
            .appName('data-engineering-capstone') \
            .config("spark.jars", "https://storage.googleapis.com/hadoop-lib/gcs/gcs-connector-hadoop3-latest.jar") \
            .config("spark.sql.repl.eagerEval.enabled", True) \
            .getOrCreate()

        file_path = f"gs://{GCS_BUCKET}/customers/*.csv"
        
        # Read data from GCS
        customer_df = read_data(spark=spark, file_path=file_path)

        # Perform data transformations
        insights_df = calculate_highest_spend(df=customer_df)

        # Write insights to GCS
        datetime_now = datetime.now().strftime("%m%d%Y%H%M%S")
        write_path = f"gs://{GCS_BUCKET}/insights/{datetime_now}.csv"
        write_to_gcs(df=insights_df, filepath=write_path)

    except Exception as e:
        print(f"Error during ETL with Spark: {e}")
        raise

    finally:
        if spark:
            spark.stop()

# Default arguments for the DAG
default_args = {
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Define the DAG
with DAG(
    dag_id="insights_dag_11",
    start_date=datetime(2024, 7, 14),
    schedule_interval="0 10 * * *",  # Daily interval at 10am
    catchup=False,
    tags=[
        "Orchestration",
        "Customer Insights",
        "Ecommerce"
    ],
) as dag:
    
    # Define the ETL task
    etl_with_spark_task = PythonOperator(
        task_id="etl_with_spark", 
        python_callable=etl_with_spark
    )

    # Define an empty task
    does_nothing = EmptyOperator(task_id="does_nothing")

    # Set task dependencies
    etl_with_spark_task >> does_nothing
