# Kitchenware Classification
![kitchenware-classification](https://raw.githubusercontent.com/Kibzik/kitchenware-classification_cv/main/imgs/header.png)
---
This repo is served with purpose of presenting what and how transfer learning can indentify
kitchen items with machine learning engineering practices.
## Table of Contents
 * [Problem Description](#problem-description)
   * [About the Data](#about-the-data)
 * [Tech Stack and concepts](#tech-stack-and-concepts)
 * [Setup](#setup)
   * [Virtual Environment](#virtual-environment)
   * [Run Service Locally](#run-service-locally)
   * [Docker Container](#docker-container)
   * [Deploying to Cloud](#deploying-to-cloudheroku-docker-deployment)

## Problem description
The problem we will study was introduced by [DataTalksCLub](https://datatalks.club/) in Kaggle platform [Kaggle Competition](https://www.kaggle.com/competitions/kitchenware-classification/).

In this competition we need to classify images of different kitchenware items into 6 classes:cups, glasses,
plates, spoons, forks and knives.

### About the Data
The training data is structured as follows (numbers of observations in brackets):
- cups (923)
- glasses (583)
- plates (986)
- spoons (798)
- forks (436)
- knives (721)

## Tech Stack and concepts

- Python
- Tensorflow
- Keras
- Machine Learning Pipeline
- Flask
- Virtual environment
- Docker
- Streamlit

## Setup
Clone the project repo and open it.

If you want to reproduce results by running [notebooks](notebooks/) or [`train.py`](src/train.py), 
you need to download data, create a virtual environment and install the dependencies.

### Download data
Download data from the [Kaggle competition](https://www.kaggle.com/competitions/kitchenware-classification/data) and move to [data folder](data/) unzipped folder with .csv files.

![Data folder structure](https://raw.githubusercontent.com/Kibzik/kitchenware-classification_cv/main/imgs/data_folder_strcture.png)

### Virtual Environment
In case of `conda`(you feel free to choose any other tools (`pipenv`, `venv`, etc.)), just follow the steps below:
1. Open the terminal and choose the project directory.
2. Create new virtual environment by command `conda create -n test-env python=3.10`.
3. Activate this virtual environment with `conda activate test-env`.
4. Install all packages using `pip install -r requirements.txt`.

### Run service locally
To run the service locally in your environment, simply use the following commands:
- Windows
```bash
waitress-serve --listen=0.0.0.0:5050 predict:app
```
- Ubuntu
```bash
gunicorn --bind=0.0.0.0:5050 predict:app
```

### Containerization
Be sure that you have already installed the Docker, and it's running on your machine now.
1. Open the terminal and choose the project directory.
2. Build docker image from [`Dockerfile`](Dockerfile) using `docker build --no-cache -t classify-kitchenware .`.
With `-t` parameter we're specifying the tag name of our docker image. 
3. Now use `docker run -it -p 8501:8501 classify-kitchenware` command to launch the docker container with your app. 
Parameter `-p` is used to map the docker container port to our real machine port.

### Deploying to Cloud(Heroku docker deployment)
Follow this steps to deploy the app to Heroku
1. Register on [Heroku](https://signup.heroku.com/) and install Heroku CLI.
2. Open the terminal in project of the app
3. Terminal: rung the `heroku login` command to log in to Heroku.
4. Terminal: login to Heroku container registry using `heroku container:login` command.
5. Terminal: create a new app in Heroku with the following command `heroku create classify-kitchenware-docker`.
6. Make small changes in [`Dockerfile`](Dockerfile): uncomment the last line and comment out the line above. 
Heroku automatically assigns porn number from the dynamic pool. So, there is no need to specify it manually.
7. Terminal: run the `heroku container:push web -a classify-kitchenware-docker` command to push docker image to Heroku.
8. Terminal: release the container using the command `heroku container:release web -a classify-kitchenware-docker`.
9. Launch your app by clicking on generated URL in 5th step. In our case the link - [Heroku app](https://classify-kitchenware-docker.herokuapp.com/).
If we have successfully deployed the app, the link opens without problems.

Now we can move on to the next step - service testing.
### Service testing
* [prediction endpoint](https://parking-slots-docker.herokuapp.com/predict) serves for the model scoring.

To test the prediction endpoint we can use handmade script  [request sender](src/request_sender.py) that takes data from a specified directory and sends requests to the service.
In case of using a script, just follow the rule:

To test the service that is **running locally**
- Just run the  [request sender](src/request_sender.py) without any changes

To test the service that is **running locally** with Streamlit visualisation
- Just use the following command in bash
```bash
streamlit run kitchenware_app.py
```

To test our **Streamlit deployment**, we should type:
- Set host parameter in 27 line to 'classify-kitchenware-docker.herokuapp.com' and run [request sender](src/request_sender.py)
along with an external interface for sharing