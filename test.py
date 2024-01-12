import psycopg2

# Database connection parameters
host = "connectify-db.postgres.database.azure.com"
database_name = "connectify"
user = "connectifyadmin"
password = "Eden258eden"
table_name = "events"

try:
    # Connection to the PostgreSQL database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        dbname=database_name,
        port=5432,
        sslmode="require"  # or "disable" if SSL is not required
    )

    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Query to select all data from the "events" table
    query = f"SELECT * FROM {table_name};"

    # Execute the query
    cursor.execute(query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Print or process the fetched data
    for row in rows:
        # Assuming the table has columns with names like "column1", "column2", etc.
        column1_value = row[0]
        column2_value = row[1]
        # Add more columns as needed

        # Process or print the data
        print(f"Column1: {column1_value}, Column2: {column2_value}")

except psycopg2.Error as e:
    print(f"Error: {e}")
finally:
    # Close the cursor and connection in the finally block to ensure it happens even if an exception occurs
    if cursor:
        cursor.close()
    if connection:
        connection.close()
