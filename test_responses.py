import requests

url = 'http://84.201.162.198:7778/predict_price'

payloads = [
    {'open_plan': 1, 'rooms': 3, 'area': 50, 'renovation': 1},
    {'open_plan': 0, 'rooms': 2, 'area': 45, 'renovation': 0},
    {'open_plan': 1, 'rooms': 4, 'area': 70, 'renovation': 1},
    {'open_plan': 0, 'rooms': 1, 'area': 30, 'renovation': 0},
    {'open_plan': 1, 'rooms': 3, 'area': 55, 'renovation': 1},
    {'open_plan': 1, 'rooms': 2, 'area': 48, 'renovation': 1},
    {'open_plan': 0, 'rooms': 3, 'area': 60, 'renovation': 0},
    {'open_plan': 0, 'rooms': 2, 'area': 50, 'renovation': 1},
    {'open_plan': 1, 'rooms': 3, 'area': 52, 'renovation': 1},
    {'open_plan': 0, 'rooms': 1, 'area': 35, 'renovation': 0}
]

for i, payload in enumerate(payloads):
    response = requests.post(url, json=payload)
    try:
        response.raise_for_status()  # Проверка на успешный статус
        print(f'Response {i+1}:', response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.RequestException as err:
        print(f'Error occurred: {err}')
    except requests.exceptions.JSONDecodeError:
        print(f'Response {i+1} is not a valid JSON: {response.text}')