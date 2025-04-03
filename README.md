# ride-sharing-spark-streaming
Spark structured streaming example
# Streaming Data Processing with Apache Spark

## Overview
This project demonstrates real-time data ingestion, parsing, and aggregation using Apache Spark Structured Streaming. The tasks include ingesting streaming data from a socket, parsing JSON messages, performing real-time aggregations, and implementing windowed time-based analytics.



## Task 1: Basic Streaming Ingestion and Parsing
### Steps:
1. Create a Spark session.
2. Read data from a socket stream (localhost:9999).
3. Define a schema for the incoming JSON data.
4. Parse the incoming JSON messages.
5. Print the parsed data to the console.
6. Start the streaming query and await termination.

## Task 2: Real-Time Aggregations (Driver-Level)
### Steps:
1. Reuse the parsed DataFrame from Task 1.
2. Group data by `driver_id`.
3. Compute the total fare amount for each driver.
4. Compute the average distance traveled for each driver.
5. Store the aggregated results in a CSV file.
6. Start the streaming query and await termination.

## Task 3: Windowed Time-Based Analytics
### Steps:
1. Convert the `timestamp` column to a proper `TimestampType`.
2. Perform a 5-minute windowed aggregation on `fare_amount` with a 1-minute slide.
3. Store the windowed results in a CSV file.
4. Start the streaming query and await termination.

## Running the Application
1. Start a socket server in the terminal.
2. Run the Spark Streaming script.
3. Input sample JSON messages into the terminal.

## Output
- Task 1: Parsed JSON data is printed to the console.
- Task 2: Aggregated results are stored in `output/driver_aggregations/`.
- Task 3: Windowed analytics are stored in `output/windowed_analytics/`.

