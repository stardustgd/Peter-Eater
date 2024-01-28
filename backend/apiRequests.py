# import requests
# from flask import Flask, request, jsonify
# import json

# app = Flask(__name__)

# def get_and_send_menu(querystring, url):
#     try:
#         response = requests.get(url, headers=headers, params=querystring)
#         data = response.text
#         json_data = json.loads(data)
#         send_data_to_flask(json_data)
#     except Exception as e:
#         print('Error:', e)

# def send_data_to_flask(json_data):
#     completeMenu = []

#     for location in json_data['all']:
#         station = location['station']
#         allFoods = []

#         for menu in location['menu']:
#             category = menu['category']

#             for items in menu['items']:
#                 foodName = items['name']
#                 foodDescription = items['description']

#                 cals = items['nutrition'].get('calories', 'N/A')

#                 foods = {'foodName': foodName, 'foodDescription': foodDescription, 'calories': cals, 'category': category}
#                 allFoods.append(foods)

#         completeMenu.append({'station': station, 'foods': allFoods})

#     try:
#         return jsonify(completeMenu)
#         # flask_url = 'http://127.0.0.1:5000/upload_data'
#         # headers = {'Content-Type': 'application/json'}
#         # response = requests.post(flask_url, data=json.dumps(completeMenu), headers=headers)

#         if response.status_code == 200:
#             print("Data sent successfully to Flask.")
#         else:
#             print(f"Failed to send data. Status code: {response.status_code}")
#     except Exception as e:
#         print('Error:', e)

# @app.route('/upload_data', methods=['POST'])
# def upload_data():
#     try:
#         data = request.get_json()
#         print("Received data:")
#         print(json.dumps(data, indent=2))
#         return jsonify(send_data_to_flask(data))
#         # return jsonify({"message": "Data received successfully"}), 200
#     except Exception as e:
#         print('Error:', e)
#         return jsonify({"message": "Error processing data"}), 500

# if __name__ == '__main__':
#     # Example usage
#     querystring = {"location": "brandywine"}
#     url = "https://zotmeal-backend.vercel.app/api"
#     headers = {"User-Agent": "insomnia/8.6.0"}

#     get_and_send_menu(querystring, url)
#     app.run(debug=True, host='0.0.0.0', port=5000)

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

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
