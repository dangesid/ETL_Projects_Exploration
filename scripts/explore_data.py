from pyspark.sql import SparkSession
from pyspark.sql.functions import col, countDistinct, min, avg, max

RAW_FILE = "data/raw/2018_Yellow_Taxi_Trip_Data_20250226.csv"

spark = SparkSession.builder.appName("Data Exploration").getOrCreate()

print("Loading dataset ...")
df = spark.read.csv(RAW_FILE, header=True, inferSchema=True)

print("\n Sample Data:")
df.show(5)