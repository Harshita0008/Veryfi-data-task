import json
import psycopg2
from psycopg2.extras import execute_batch

def read_data(file_path):
    """
    Reads a JSON file and returns the data.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error reading data from file: {e}")
        return None

def connect_database():
    """
    Establishes a connection to the PostgreSQL database.
    """
    try:
        conn = psycopg2.connect(
            host="",
            port="",
            database="",
            user="",  # Ensure these credentials are correct
            password=""
        )
        print("Database connection successful.")
        return conn
    except Exception as e:
        print(f"Failed to connect to the database: {e}")
        return None

def insert_data(conn, data):
    """
    Inserts data into the products table.
    """
    if not data:
        print("No data provided for insertion.")
        return

    cursor = conn.cursor()
    insert_query = """
        INSERT INTO products (code, url, product_name, brands, categories, countries, ingredients_text, nutrients, other_fields)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (code) DO NOTHING;
    """
    try:
        # Prepare data for insertion
        tuple_data = [
            (
                item.get('code'), 
                item.get('url'),
                item.get('product_name'),
                item.get('brands'),
                item.get('categories'),
                item.get('countries'),
                item.get('ingredients_text'),
                json.dumps({key: item[key] for key in item if key.endswith('_100g')}, default=str),  # Nutrient data
                json.dumps({key: item[key] for key in item if not key.endswith('_100g') and key not in ['code', 'url', 'product_name', 'brands', 'categories', 'countries', 'ingredients_text']}, default=str)  # Other fields
            ) for item in data
        ]

        # Batch insert data
        execute_batch(cursor, insert_query, tuple_data, page_size=100)
        conn.commit()
        print(f"Inserted {len(tuple_data)} records successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
    finally:
        cursor.close()

def main():
    # Configuration
    file_path = 'veryfi_off_dataset.json'

    # ETL Process
    data = read_data(file_path)
    if data is None:
        print("Failed to read data, exiting...")
        return

    conn = connect_database()
    if conn is not None:
        insert_data(conn, data)
        conn.close()
    else:
        print("Failed to establish a database connection, exiting...")

if __name__ == '__main__':
    main()
