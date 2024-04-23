# Product Database ETL Pipeline
This project aims to ingest product data from JSON files obtained from openfoodfacts.com into a PostgreSQL database. The pipeline follows the ETL (Extract, Transform, Load) process to read, process, and load the data into the database.

### Dataset
The dataset consists of product information in JSON format and is obtained from openfoodfacts.com. It contains a sample of 50,000 products. Similar datasets are expected to be received from this source approximately weekly.

### Pipeline Workflow
Extract: Read data from the JSON file.
Transform: Process the data to fit a unified internal schema that can merge with other data sources. The primary key used is the "code" field.
Load: Insert the transformed data into a PostgreSQL database.

### Use Case:

The project is ideal for scenarios where periodic data ingestion is necessary from structured files into a relational database.
Common applications include business intelligence, analytics, and reporting where data from diverse sources needs to be consolidated and analyzed.

### Company Setting Operation:

In a company setting, the pipeline would be configured to run automatically at scheduled intervals (e.g., daily, weekly).
Upon execution, it would fetch the latest data from the designated JSON file, perform necessary transformations, and load it into the PostgreSQL database.
Monitoring mechanisms would be implemented to track pipeline performance, detect errors, and ensure successful data ingestion.
The pipeline's scalability and robustness would be tested and optimized to handle large volumes of data efficiently.

### Conceptual Operation in a Company Setting:
1. Scheduled Execution:
- The pipeline is scheduled to run at specific intervals, such as daily or weekly, depending on the frequency of data updates.
- Scheduled execution ensures timely ingestion of fresh data into the database, enabling up-to-date analysis and decision-making.
2. Data Source Integration:
- The pipeline seamlessly integrates with various data sources within the company's ecosystem, including internal systems, third-party platforms, or external APIs.
- This integration enables comprehensive data collection from diverse sources, facilitating comprehensive analysis and insights generation.
3. Scalability and Performance:
- The pipeline is designed to handle large volumes of data efficiently, ensuring scalability to accommodate growing datasets.
- Performance optimizations, such as parallel processing and batch operations, enhance the speed and responsiveness of data ingestion, even under high load conditions.
4. Error Handling and Monitoring:
- Robust error handling mechanisms are implemented to detect and handle data anomalies, ensuring data integrity throughout the pipeline.
- Comprehensive monitoring tools track the execution status, performance metrics, and error logs, enabling timely intervention and troubleshooting as needed.

### Setup
1. Clone this repository to your local machine.
2. Install PostgreSQL if not already installed.
3. Create a new database in PostgreSQL for the product data.
4. Update the config.json file with your PostgreSQL database connection details.
5. Install the required Python dependencies using pip install -r requirements.txt.

### Usage
1. Place the JSON file containing the product data in the data directory.
2. Run the pipeline script using python pipeline.py.
3. Monitor the console output for any errors or logs.
4. Verify the data has been successfully loaded into the PostgreSQL database

### Dependencies
1. Python 3.x
2. psycopg2 (for PostgreSQL interaction)
3. json (for JSON parsing)
