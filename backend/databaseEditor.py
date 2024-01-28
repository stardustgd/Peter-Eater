import sqlite3
import requests
from datetime import date, timedelta

#tested
def populate_meals_database(names):
    conn = sqlite3.connect('eater_info.db')
    cursor = conn.cursor()
    insert_meal_query = 'INSERT INTO Meals (name) VALUES (?)'
  
    for name in names:
        cursor.execute(insert_meal_query, (name,))
        print(f'Inserted meal: {name} (ID: {cursor.lastrowid})')

        
def populate_cafeterias(cafeteria_names):
    db_name = 'eater_info.db'  
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()

            # Iterate over cafeteria names in the list
            for cafeteria_name in cafeteria_names:
                # Insert into Cafeterias table
                cursor.execute('''
                    INSERT OR IGNORE INTO Cafeterias (name)
                    VALUES (?)
                ''', (cafeteria_name,))

            conn.commit()
            print("Cafeterias populated successfully.")

    except sqlite3.Error as e:
        print(f"Error populating cafeterias: {e}")

def populate_stations(station_data):
    db_name = 'eater_info.db'
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()

            # Iterate over station data in the list
            for station_name, cafeteria_id in station_data:
                # Insert into Stations table
                cursor.execute('''
                    INSERT INTO Stations (name, cafeteria_id)
                    VALUES (?, ?)
                ''', (station_name, cafeteria_id))

            conn.commit()
            print("Stations populated successfully.")

    except sqlite3.Error as e:
        print(f"Error populating stations: {e}")

def populate_mealtimes(mealtime_names):
    db_name = 'eater_info.db'  
    try:
        with sqlite3.connect(db_name) as conn:
            cursor = conn.cursor()

            # Iterate over mealtime names in the list
            for mealtime_name in mealtime_names:
                # Insert into Meals table
                cursor.execute('''
                    INSERT INTO Meals (name)
                    VALUES (?)
                ''', (mealtime_name,))

            conn.commit()
            print("Mealtimes populated successfully.")

    except sqlite3.Error as e:
        print(f"Error populating mealtimes: {e}")

#tested
def get_average_rating_by_food_id(food_id):
    conn = sqlite3.connect('eater_info.db') 
    cursor = conn.cursor()

    try:
        # Execute the query to get the average rating for the specific food name
        query = """
        SELECT AVG(rating) FROM Ratings
        JOIN Foods ON Ratings.food_id = Foods.id
        WHERE Foods.id = ?
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

#tested
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

#tested
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

#tested
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

#tested
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

#tested
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

#tested
def get_average_mealtime_rating(cafeteria_id, meal_id):
    conn = sqlite3.connect('eater_info.db') 
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

#tested
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
    conn = sqlite3.connect('eater_info.db')  
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

#tested
def insert_rating(rating, comment, food_id, meal_id):
    conn = sqlite3.connect('eater_info.db') 
    cursor = conn.cursor()

    try:
        # Execute the query to insert a new rating
        query = """
        INSERT INTO Ratings (rating, comment, food_id, meal_id)
        VALUES (?, ?, ?, ?)
        """
        cursor.execute(query, (rating, comment, food_id, meal_id))

        # Commit the changes to the database
        conn.commit()
        print("Rating inserted successfully.")
    except sqlite3.Error as e:
        # Handle any potential errors
        print(f"Error inserting rating: {e}")
    finally:
        # Close the database connection
        conn.close()

#tested
def insert_daily_rating(cafeteria_id, avg_daily_rating):
    conn = sqlite3.connect('eater_info.db')  
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

#tested
def find_food_id_by_name(food_name):
    conn = sqlite3.connect('eater_id.db')  
    cursor = conn.cursor()

    try:
        # Execute the query to find the food_id based on the food name
        query = "SELECT id FROM Foods WHERE name = ?"
        cursor.execute(query, (food_name,))
        result = cursor.fetchone()

        if result:
            return result[0]
        else:
            print(f"No food found with the name '{food_name}'.")
            return None
    except sqlite3.Error as e:
        # Handle any potential errors
        print(f"Error finding food_id: {e}")
        return None
    finally:
        # Close the database connection
        conn.close()

#tested   
def delete_all_ratings():
    conn = sqlite3.connect('eater_info.db')
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


def populate_necessary():
    populate_cafeterias(['Brandywine', 'Anteatery'])
    populate_mealtimes(['Breakfast', 'Lunch', 'Dinner'])
    populate_stations([['Ember/Grill', 1], ['Grubb/Mainline',1],['Hearth/Pizza',1], ['Soups',1],['The Farm Stand/Salad Bar',1], ['Vegan',1], ['Crossroads',1], ['Compass',1], ['Honeycakes/Bakery',1],
                      ['Deli',2], ['Bakery',2], ['Home',2], ['Sizzle Grill',2], ['Fire and Ice Round Grill',2],['Oven',2], ['Farmer\'s Market',2], ['Fire and Ice Saute',2], ['Soups',2], ['Vegan',2]]
)
if __name__ == "__main__":
    # populate_mealtime()
    # populate_food()
    # for i in range(100):
    #     for j in range(1,5):
    #         insert_rating(j, 'good', 1, 1)
    # print(get_average_rating_by_food_id(1))
    # print(get_average_mealtime_rating(1, 1))
    # print(get_average_rating_by_cafeteria(1))
    # insert_daily_rating(1, 2.5)
    # print(get_average_daily_rating_past_days(1,1))
    populate_necessary()
    # delete_all_ratings()



