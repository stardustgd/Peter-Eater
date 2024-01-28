from flask import Flask, jsonify, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/receive_data', methods=['GET'])
def receive_data():
    try:
        # Make a request to get JSON data
        # url = 'your_api_url_here'
        # headers = {'Content-Type': 'application/json'}
        # querystring = {}  # Add any necessary query parameters
        querystring = {"location": "brandywine"}
        url = "https://zotmeal-backend.vercel.app/api"
        headers = {"User-Agent": "insomnia/8.6.0"}

        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()  # Assuming the response is JSON

        # Your parsing logic
        completeMenu = []
        for location in data['all']:
            station = location['station']
            allFoods = []

            for menu in location['menu']:
                category = menu['category']

                for items in menu['items']:
                    foodName = items['name']
                    foodDescription = items['description']

                    cals = items['nutrition'].get('calories', 'N/A')

                    foods = {'foodName': foodName, 'foodDescription': foodDescription, 'calories': cals, 'category': category}
                    allFoods.append(foods)

            completeMenu.append({'foods': allFoods,'station': station})

        # Send the parsed data as a response
        return jsonify(completeMenu)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
