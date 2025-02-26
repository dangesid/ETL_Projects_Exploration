from pyspark.sql import SparkSession, Row
from pyspark.sql.functions import avg, col
import os 

RAW_FILE = "data/raw/2018_Yellow_Taxi_Trip_Data_20250226.csv"
PROCESSED_DIR = "data/processed"
OUTPUT_FILE = f"{PROCESSED_DIR}/summary.csv"

def process_data():
    spark = SparkSession.builder.appName("ETL Pipeline").getOrCreate()

    print("Loading raw data... ")
    df = spark.read.csv(RAW_FILE, header=True, inferSchema=True)

    print("Processing data... ")
    df_filtered = df.filter(col("fare_amount") > 0)
    avg_fare = df_filtered.select(avg("fare_amount")).first()[0]
    print(f"Average fare amount: ${avg_fare:.2f}")

    # ✅ Convert avg_fare (float) into a Spark DataFrame
    avg_fare_df = spark.createDataFrame([Row(average_fare=avg_fare)])

    # ✅ Corrected `.write.csv()` method
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    avg_fare_df.coalesce(1).write.mode("overwrite").option("header", "true").csv(PROCESSED_DIR)

    print(f"Processed data saved to {PROCESSED_DIR}")

if __name__ == "__main__":
    process_data()
