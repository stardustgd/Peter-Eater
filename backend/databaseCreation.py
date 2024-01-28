import sqlite3
import os

def create_database():
    # Connect to the SQLite database
    db = sqlite3.connect('eater_info.db')
    cursor = db.cursor()

    # Enable foreign key support
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Create Cafeterias table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cafeterias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
    ''')

    # Create Stations table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Stations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            cafeteria_id INTEGER,
            FOREIGN KEY (cafeteria_id) REFERENCES Cafeterias(id)
        )
    ''')

    # Create Meals table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Meals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
    ''')

    # Create Foods table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Foods (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            description TEXT,
            calories INTEGER,
            current_cafeteria_id INTEGER,
            current_station_id INTEGER,
            previous_rating REAL,
            FOREIGN KEY (current_cafeteria_id) REFERENCES Cafeterias(id),
            FOREIGN KEY (current_station_id) REFERENCES Stations(id)
        )
    ''')

    # Create Ratings table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Ratings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rating REAL,
            comment TEXT,
            food_id INTEGER,
            meal_id INTEGER,
            FOREIGN KEY (meal_id) REFERENCES Meals(id),
            FOREIGN KEY (food_id) REFERENCES Foods(id)
        )
    ''')

    # Create DailyRatings table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS DailyRatings (
            cafeteria_id INTEGER,
            rating_date DATE PRIMARY KEY,
            avgDailyRating FLOAT NOT NULL,
            FOREIGN KEY (cafeteria_id) REFERENCES Cafeterias(id)
        )
    ''')

    # Commit changes and close the database connection
    db.commit()
    db.close()

def delete_database(database_name):
    try:
        os.remove(database_name)
        print(f"Database '{database_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"Database '{database_name}' not found.")
    except Exception as e:
        print(f"Error deleting database '{database_name}': {e}")

if __name__ == '__main__':
    delete_database('eater_info.db')
    create_database()
