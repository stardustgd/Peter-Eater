import requests
import json

url = "https://zotmeal-backend.vercel.app/api"

# querystring = {"location":"brandywine"}

payload = ""
headers = {"User-Agent": "insomnia/8.6.0"}



def get_menu(querystring, fileSend):
    try:
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        data = response.text
        json_data = json.loads(data)
        with open(fileSend, 'w') as json_file:
            json.dump(json_data, json_file, indent=2)
            
    except:
        RuntimeError("could not retrieve data")

def format_data(fileOpen, fileSend):
    with open(fileOpen) as f:
        jsondata = json.load(f)
    
    completeMenu = []
    for location in jsondata['all']:
        station = location['station']
        allCategories = []
        allFoods = []
        for menu in location['menu']:
            category = menu['category']
            for items in menu['items']:
                foodName = items['name']
                foodDescription = items['description']
                if 'calories' in items['nutrition']:
                    cals = items['nutrition']['calories']
                else:
                    cals = 'N/A'
                foods = {'foodName': foodName, 'foodDescription': foodDescription, 'calories': cals, 'category': category}
            
                allFoods.append(foods)
        completeMenu.append({'station': station, 'foods': allFoods})
    with open(fileSend, 'w') as json_file:
            json.dump(completeMenu, json_file, indent=2)
    


get_menu({"location": 'anteatery'}, 'jsonFiles/anteateryUnformatted.json')
format_data('jsonFiles/anteateryUnformatted.json', 'jsonFiles/anteateryFormatted.json')
