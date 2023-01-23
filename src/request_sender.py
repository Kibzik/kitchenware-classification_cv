import requests
import pandas as pd

from time import sleep


def send_requests(host: str = "localhost:5050", dataset_path=None) -> None:
    """
    Generates requests from the file and sends it to the host.
    :param host: hostname:port or URL address
    :param dataset_path: dataset_path to data to generate request

    :return: none

    """
    # !/usr/bin/env python
    # coding: utf-8
    data = pd.read_csv(dataset_path, dtype = {'Id': str})
    data["img_name"] = 'data/images/' + data['Id'] + '.jpg'
    for request_data in data.to_dict("records"):
        print(f"Request to service: {request_data['Id']}")
        response = requests.post(url=f"http://{host}/classify_img", json=request_data).json()
        max_label = max(response, key=response.get)
        print(f"Model tells that it is a {max_label.upper()}")
        sleep(1)


def streamlit_request(img="data/images/0000.jpg"):
    # url = 'http://localhost:5050/classify_img'
    url = 'http://supermac7.pythonanywhere.com/classifier'
    img = img[12:]
    response = requests.post(url, json={"im": img}).json()
    print(f'Predictions: {response}')
    return response


if __name__ == "__main__":
    dataset_path = "../data/request.csv"
    send_requests(host="localhost:5050", dataset_path=dataset_path)
