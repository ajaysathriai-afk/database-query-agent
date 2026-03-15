import sqlite3
import pandas as pd
from pathlib import Path

class DatabaseManager:
    
    def __init__(self, db_path="data/sales.db"):
        self.db_path = db_path
        Path("data").mkdir(exist_ok=True)
        self.create_sample_database()
    
    def create_sample_database(self):
        """Create sample sales database"""
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create customers table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT,
            country TEXT,
            signup_date TEXT
        )
        """)
        
        # Create products table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT,
            price REAL
        )
        """)
        
        # Create orders table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            order_date TEXT,
            total_amount REAL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )
        """)
        
        # Insert sample data
        customers = [
            (1, 'John Doe', 'john@example.com', 'USA', '2024-01-15'),
            (2, 'Jane Smith', 'jane@example.com', 'UK', '2024-02-20'),
            (3, 'Mike Johnson', 'mike@example.com', 'Canada', '2024-03-10'),
            (4, 'Sarah Wilson', 'sarah@example.com', 'Australia', '2024-04-05'),
            (5, 'Tom Brown', 'tom@example.com', 'USA', '2024-05-12')
        ]
        
        products = [
            (1, 'Laptop', 'Electronics', 999.99),
            (2, 'Mouse', 'Electronics', 29.99),
            (3, 'Keyboard', 'Electronics', 79.99),
            (4, 'Monitor', 'Electronics', 299.99),
            (5, 'Desk', 'Furniture', 399.99)
        ]
        
        orders = [
            (1, 1, 1, 2, '2024-06-01', 1999.98),
            (2, 2, 2, 5, '2024-06-02', 149.95),
            (3, 1, 3, 1, '2024-06-03', 79.99),
            (4, 3, 4, 2, '2024-06-04', 599.98),
            (5, 4, 5, 1, '2024-06-05', 399.99),
            (6, 5, 1, 1, '2024-06-06', 999.99),
            (7, 2, 3, 2, '2024-06-07', 159.98),
            (8, 3, 2, 3, '2024-06-08', 89.97),
            (9, 1, 4, 1, '2024-06-09', 299.99),
            (10, 4, 1, 1, '2024-06-10', 999.99)
        ]
        
        cursor.executemany("INSERT OR IGNORE INTO customers VALUES (?,?,?,?,?)", customers)
        cursor.executemany("INSERT OR IGNORE INTO products VALUES (?,?,?,?)", products)
        cursor.executemany("INSERT OR IGNORE INTO orders VALUES (?,?,?,?,?,?)", orders)
        
        conn.commit()
        conn.close()
        
        print("✅ Sample database created!")
    
    def get_connection_string(self):
        """Get SQLite connection string"""
        return f"sqlite:///{self.db_path}"
    
    def execute_query(self, query):
        """Execute SQL query and return results"""
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
