# Final Project Task

This project involves creating a machine learning model to predict prices, saving the model in a web service, and containerizing the application using Docker. Below are the steps and instructions for this project.

## 1. Source Data and Statistics

### Source Data
The dataset used for this project includes the following features:
- `floor`
- `open_plan`
- `rooms`
- `studio`
- `area`
- `kitchen_area`
- `living_area`
- `renovation`

### Data Statistics
Below are some basic statistics and visualizations of the dataset.

**Example Statistics:**
- Mean, median, and standard deviation for each feature.
- Distribution plots for numerical features.
- Bar plots for categorical features.

(Add your data statistics and plots here)

## 2. Model Information

### Chosen Model and Framework
For this project, we used the `CatBoostRegressor` from the CatBoost framework due to its efficient handling of categorical features and overall performance.

### Hyperparameters
- `iterations`: 1500
- `learning_rate`: 0.08
- `depth`: 7

(Add any other relevant hyperparameters here)

## 3. Installation and Running the App

### Virtual Environment Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RUDIG0D/final_project
   cd final_project
2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. **Install the required packages**
   ```bash
   pip install -r requirements.txt
4. **Run app**
   ```bash
   python app.py
## 4. Dockerfile Information

### Dockerfile Content
The Dockerfile sets up the environment for running the web service with the trained model.
```
 FROM ubuntu:22.04
 MAINTAINER Ilia Smetanin 
 RUN apt-get update -y
 COPY . /apt/gsom_predictor
 WORKDIR /apt/gsom_predictor
 RUN apt install -y python3-pip
 RUN pip3 install -r requirements.txt
 CMD python3 app.py
 ```
 
### Building and Running the Docker Container
#### Build the Docker image

```bash
docker build -t rudig0d/e2e_project_new:v0.4 . 
```
#### Run the Docker container
```bash
docker run --network host rudig0d/e2e_project_new:v0.4 .
```
### Opening Ports on Remote VM
#### To open a port on your remote VM, you can use the following command
```bash
sudo ufw allow 7778
```

## Testing the Web Service
### Python Script for Testing to implement in app.py
```bash
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
        response.raise_for_status()  
        print(f'Response {i+1}:', response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except requests.exceptions.RequestException as err:
        print(f'Error occurred: {err}')
    except requests.exceptions.JSONDecodeError:
        print(f'Response {i+1} is not a valid JSON: {response.text}')
```
Ensure  that service is working

```bash
python test_requests.py
```
