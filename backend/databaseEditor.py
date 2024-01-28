import sqlite3
import requests
from datetime import date, timedelta

def create_connection():
    # Connect to the existing SQLite database file
    db = sqlite3.connect('eater_info.db')
    cursor = db.cursor()
    print('Connected to the existing database')
    return db, cursor

def close_connection(db):
    # Close the database connection when done
    db.close()
    print('Closed the database connection')

def populate_meals_database(names, cursor):
    insert_meal_query = 'INSERT INTO Meals (name) VALUES (?)'
  
    for name in names:
        cursor.execute(insert_meal_query, (name,))
        print(f'Inserted meal: {name} (ID: {cursor.lastrowid})')

def populate_cafeteria_database(cafeterias, cursor):
    insert_cafeteria_query = 'INSERT INTO Cafeterias (name) VALUES (?)'
    insert_station_query = 'INSERT INTO Stations (name, cafeteria_id) VALUES (?, ?)'
  
    for cafeteria in cafeterias:
        # Insert cafeteria
        cursor.execute(insert_cafeteria_query, (cafeteria['name'],))
        cafeteria_id = cursor.lastrowid
        print(f'Inserted cafeteria: {cafeteria["name"]} (ID: {cafeteria_id})')
  
        # Insert foods for each station
        for station in cafeteria['stations']:
            cursor.execute(insert_station_query, (station, cafeteria_id))
            print(f'Inserted food: {station} for cafeteria {cafeteria["name"]} (ID: {cursor.lastrowid})')

def get_average_rating_by_food_name(food_id):
    conn = sqlite3.connect('eater_id.db')  # Replace 'your_database_name.db' with your actual database name
    cursor = conn.cursor()

    try:
        # Execute the query to get the average rating for the specific food name
        query = """
        SELECT AVG(rating) FROM Ratings
        JOIN Foods ON Ratings.food_id = Foods.id
        WHERE Foods.name = ?
        """
        cursor.execute(query, (food_id,))
        result = cursor.fetchone()[0]

        if result is not None:
            return result
        else:
            print(f"No ratings found for the food '{food_id}'.")
            return None
    except sqlite3.Error as e:
        # Handle any potential errors
        print(f"Error getting average rating for the food '{food_id}': {e}")
        return None
    finally:
        # Close the database connection
        conn.close()

def populate_food():

    url = "http://127.0.0.1:5000/receive_data"

    payload = ""
    headers = {"User-Agent": "insomnia/8.6.0"}
    # response = requests.get(url, headers=headers, params=querystring)
    

    response = requests.request("GET", url, data=payload, headers=headers)
    data = response.json() 
    for station in data:
        for food in station['foods']:
            if not is_food_exists(food['foodName']):
                #currently hardcoded cafeteria id, need to change
                insert_food(food['foodName'], food['foodDescription'], food['calories'], 1, station['station'], 0)
            else:
                update_food_station_and_cafeteria(food['foodName'], 1, station['station'])
        # if is_food_exists(station)
        # print(station['station'])
    # print(response.text)

def get_station_id_by_name(station_name):
    conn = sqlite3.connect('eater_info.db')
    cursor = conn.cursor()

    try:
        query = "SELECT id FROM Stations WHERE name = ?"
        cursor.execute(query, (station_name,))
        result = cursor.fetchone()

        if result:
            return result[0]
        else:
            print(f"Station '{station_name}' not found.")
            return None
    except sqlite3.Error as e:
        print(f"Error getting station ID: {e}")
        return None
    finally:
        conn.close()

def update_food_station_and_cafeteria(food_name, new_cafeteria_id, new_station_name):
    conn = sqlite3.connect('eater_info.db')
    cursor = conn.cursor()

    try:
        # Get the new station ID based on the station name
        new_station_id = get_station_id_by_name(new_station_name)
        if new_station_id is None:
            return

        # Execute the query to update the food
        query = """
        UPDATE Foods
        SET current_cafeteria_id = ?, current_station_id = ?
        WHERE name = ?
        """
        cursor.execute(query, (new_cafeteria_id, new_station_id, food_name))

        # Commit the changes to the database
        conn.commit()
        print(f"Food '{food_name}' updated successfully.")
    except sqlite3.Error as e:
        # Handle any potential errors
        print(f"Error updating food: {e}")
    finally:
        # Close the database connection
        conn.close()


def insert_food(name, description, calories, current_cafeteria_id, current_station_id, previous_rating=None):
    # Connect to the SQLite database
    conn = sqlite3.connect('eater_info.db')  
    cursor = conn.cursor()

    try:
        # Execute the query to insert a new food
        query = """
        INSERT INTO Foods (name, description, calories, current_cafeteria_id, current_station_id, previous_rating)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (name, description, calories, current_cafeteria_id, current_station_id, previous_rating))

        # Commit the changes to the database
        conn.commit()
        print(f"Food '{name}' inserted successfully.")
    except sqlite3.Error as e:
        # Handle any potential errors
        print(f"Error inserting food: {e}")
    finally:
        # Close the database connection
        conn.close()


def is_food_exists(food_name):
    # Connect to the SQLite database
    conn = sqlite3.connect('eater_info.db')  
    cursor = conn.cursor()

    # Execute the query to check if the food exists
    query = "SELECT COUNT(*) FROM Foods WHERE name = ?"
    cursor.execute(query, (food_name,))
    result = cursor.fetchone()[0]

    # Close the database connection
    conn.close()

    # Return True if the food exists, False otherwise
    return result > 0

def populate_new():
    #Create a connection
    db, cursor = create_connection()

    # Populate Meals database
    meals = ['Breakfast', 'Lunch', 'Dinner']
    populate_meals_database(meals, cursor)

    # Populate Cafeteria database
    cafeterias = [
        {'name': 'Brandywine', 'stations': ['Ember/Grill', 'Grubb/Mainline', 'Hearth/Pizza', 'Soups',
                                             'The Farm Stand/Salad Bar', 'Vegan', 'Crossroads', 'Compass', 'Honeycakes/Bakery']},
        {'name': 'Ateatery', 'stations': ['Deli', 'Bakery', 'Home', 'Sizzle Grill', 'Fire and Ice Round Grill',
                                          'Oven', 'Farmer\'s Market', 'Fire and Ice Saute', 'Soups', 'Vegan']}
    ]
    populate_cafeteria_database(cafeterias, cursor)

    # Commit changes and close the connection
    db.commit()
    close_connection(db)

def get_average_mealtime_rating(cafeteria_id, meal_id):
    conn = sqlite3.connect('eater_info.db')  # Replace 'your_database_name.db' with your actual database name
    cursor = conn.cursor()

    try:
        query = """
        SELECT AVG(rating) FROM Ratings
        JOIN Foods ON Ratings.food_id = Foods.id
        WHERE Foods.current_cafeteria_id = ? AND Ratings.meal_id = ?
        """
        cursor.execute(query, (cafeteria_id, meal_id))
        result = cursor.fetchone()[0]

        if result is not None:
            return result
        else:
            print("No ratings found for the given cafeteria and meal.")
            return None
    except sqlite3.Error as e:
        print(f"Error getting average rating: {e}")
        return None
    finally:
        conn.close()

def get_average_rating_by_cafeteria(cafeteria_id):
    conn = sqlite3.connect('eater_info.db')
    cursor = conn.cursor()

    try:
        query = """
        SELECT AVG(rating) FROM Ratings
        JOIN Foods ON Ratings.food_id = Foods.id
        WHERE Foods.current_cafeteria_id = ?
        """
        cursor.execute(query, (cafeteria_id,))
        result = cursor.fetchone()[0]

        if result is not None:
            return result
        else:
            print("No ratings found for the given cafeteria.")
            return None
    except sqlite3.Error as e:
        print(f"Error getting average rating: {e}")
        return None
    finally:
        conn.close()


def get_average_daily_rating_past_days(cafeteria_id, past_days):
    conn = sqlite3.connect('eater_info.db')  # Replace 'your_database_name.db' with your actual database name
    cursor = conn.cursor()

    try:
        # Get the end date (today)
        end_date = date.today()

        # Calculate the start date by subtracting past_days from the end date
        start_date = end_date - timedelta(days=past_days)

        # Execute the query to get the average daily rating for the specified days
        query = """
        SELECT AVG(avgDailyRating) FROM DailyRatings
        WHERE cafeteria_id = ? AND rating_date BETWEEN ? AND ?
        """
        cursor.execute(query, (cafeteria_id, start_date.isoformat(), end_date.isoformat()))
        result = cursor.fetchone()[0]

        if result is not None:
            return result
        else:
            print(f"No daily ratings found for the past {past_days} days for cafeteria {cafeteria_id}.")
            return None
    except sqlite3.Error as e:
        # Handle any potential errors
        print(f"Error getting average daily rating: {e}")
        return None
    finally:
        # Close the database connection
        conn.close()

    
def insert_daily_rating(cafeteria_id, avg_daily_rating):
    conn = sqlite3.connect('eater_info.db')  # Replace 'your_database_name.db' with your actual database name
    cursor = conn.cursor()

    try:
        # Get the current date
        today = date.today()
        rating_date = today.isoformat()

        # Execute the query to insert the daily rating
        query = """
        INSERT OR REPLACE INTO DailyRatings (cafeteria_id, rating_date, avgDailyRating)
        VALUES (?, ?, ?)
        """
        cursor.execute(query, (cafeteria_id, rating_date, avg_daily_rating))

        # Commit the changes to the database
        conn.commit()
        print(f"Daily rating for cafeteria {cafeteria_id} inserted successfully for {rating_date}.")
    except sqlite3.Error as e:
        # Handle any potential errors
        print(f"Error inserting daily rating: {e}")
    finally:
        # Close the database connection
        conn.close()

def delete_all_ratings():
    conn = sqlite3.connect('eater_info.db')  # Replace 'your_database_name.db' with your actual database name
    cursor = conn.cursor()

    try:
        # Execute the query to delete all records from the Ratings table
        query = "DELETE FROM Ratings"
        cursor.execute(query)

        # Commit the changes to the database
        conn.commit()
        print("All records from Ratings table deleted successfully.")
    except sqlite3.Error as e:
        # Handle any potential errors
        print(f"Error deleting records from Ratings table: {e}")
    finally:
        # Close the database connection
        conn.close()

if __name__ == "__main__":
    # populate_new()
    populate_food()



