from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, FloatType

# Initialize a Spark session for streaming ride data
spark = SparkSession.builder \
    .appName("Ride Data Streaming Processor") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Define the expected schema for ride data events
ride_schema = StructType() \
    .add("trip_id", StringType()) \
    .add("driver_id", StringType()) \
    .add("distance_km", FloatType()) \
    .add("fare_amount", FloatType()) \
    .add("timestamp", StringType())

# Establish a streaming source from a socket connection
incoming_stream = spark.readStream \
    .format("socket") \
    .option("host", "localhost") \
    .option("port", 9999) \
    .load()

# Transform the raw JSON data into structured format
structured_stream = incoming_stream \
    .select(from_json(col("value"), ride_schema).alias("ride")) \
    .select("ride.*")

# Write the structured ride data to a CSV output with checkpointing
output_query = structured_stream.writeStream \
    .format("csv") \
    .outputMode("append") \
    .option("path", "output/ride_data") \
    .option("checkpointLocation", "checkpoints/ride_data") \
    .option("header", "true") \
    .start()

output_query.awaitTermination()
