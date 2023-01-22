FROM python:3.10.0

WORKDIR /user/app
COPY requirements-deploy.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

COPY data/images .data/images/
COPY models/ ./models/
COPY src/request_sender.py ./src/request_sender.py
COPY ["predict.py", "kitchenware_app.py"]

EXPOSE 8501
CMD ["streamlit", "run", "kitchenware_app.py","--server.port=8501", "--server.address=0.0.0.0"]
