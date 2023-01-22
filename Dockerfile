FROM python:3.10.8-slim

WORKDIR /user/app
COPY requirements-deploy.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

COPY data/images ./images/
COPY models/ ./models/
COPY src/request_sender.py ./src/request_sender.py
COPY ["predict.py", "kitchenware_app.py"]

EXPOSE 8502
CMD ["streamlit", "run", "kitchenware_app.py","--server.port=8502", "--server.address=0.0.0.0"]
