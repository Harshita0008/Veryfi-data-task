# Product Database ETL Pipeline
This project aims to ingest product data from JSON files obtained from openfoodfacts.com into a PostgreSQL database. The pipeline follows the ETL (Extract, Transform, Load) process to read, process, and load the data into the database.

### Dataset
The dataset consists of product information in JSON format and is obtained from openfoodfacts.com. It contains a sample of 50,000 products. Similar datasets are expected to be received from this source approximately weekly.

### Pipeline Workflow
Extract: Read data from the JSON file.
Transform: Process the data to fit a unified internal schema that can merge with other data sources. The primary key used is the "code" field.
Load: Insert the transformed data into a PostgreSQL database.

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
