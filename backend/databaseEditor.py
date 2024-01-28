import sqlite3
import requests

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

def populate_food():

    url = "http://127.0.0.1:5000/receive_data"

    payload = ""
    headers = {"User-Agent": "insomnia/8.6.0"}
    # response = requests.get(url, headers=headers, params=querystring)
    

    response = requests.request("GET", url, data=payload, headers=headers)
    data = response.json() 
    for station in data:
        print(station['station'])
    # print(response.text)

if __name__ == "__main__":
    # Create a connection
    # db, cursor = create_connection()

    # # Populate Meals database
    # meals = ['Breakfast', 'Lunch', 'Dinner']
    # populate_meals_database(meals, cursor)

    # # Populate Cafeteria database
    # cafeterias = [
    #     {'name': 'Brandywine', 'stations': ['Ember/Grill', 'Grubb/Mainline', 'Hearth/Pizza', 'Soups',
    #                                          'The Farm Stand/Salad Bar', 'Vegan', 'Crossroads', 'Compass', 'Honeycakes/Bakery']},
    #     {'name': 'Ateatery', 'stations': ['Deli', 'Bakery', 'Home', 'Sizzle Grill', 'Fire and Ice Round Grill',
    #                                       'Oven', 'Farmer\'s Market', 'Fire and Ice Saute', 'Soups', 'Vegan']}
    # ]
    # populate_cafeteria_database(cafeterias, cursor)

    # # Commit changes and close the connection
    # db.commit()
    # close_connection(db)
    populate_food()



