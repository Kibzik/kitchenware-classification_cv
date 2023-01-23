FROM python:3.10.0

WORKDIR /user/app
COPY requirements-deploy.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

COPY ["./data/images/0000.jpg", "./data/images/0008.jpg", "./data/images/0015.jpg", "./data/images/2744.jpg", "./data/images/3242.jpg", "./data/images/3247.jpg", "./data/images/8170.jpg", "./data/images/"]
COPY ["./data/images/0022.jpg", "./data/images/1239.jpg", "./data/images/3168.jpg", "./data/images/2103.jpg", "./data/images/5788.jpg", "./data/images/7522.jpg", "./data/images/9374.jpg", "./data/images/"]
COPY ["./data/images/0019.jpg", "./data/images/0967.jpg", "./data/images/2724.jpg", "./data/images/3135.jpg", "./data/images/4673.jpg", "./data/images/7263.jpg", "./data/images/9168.jpg", "./data/images/"]
COPY ["./data/images/0190.jpg", "./data/images/0848.jpg", "./data/images/1739.jpg", "./data/images/3049.jpg", "./data/images/4366.jpg", "./data/images/6106.jpg", "./data/images/9085.jpg", "./data/images/"]
COPY ["./data/images/0136.jpg", "./data/images/1206.jpg", "./data/images/2113.jpg", "./data/images/3833.jpg", "./data/images/5565.jpg", "./data/images/7261.jpg", "./data/images/9271.jpg", "./data/images/"]
COPY ["./data/images/0018.jpg", "./data/images/0510.jpg", "./data/images/1742.jpg", "./data/images/2721.jpg", "./data/images/3277.jpg", "./data/images/4770.jpg", "./data/images/8204.jpg", "./data/images/"]
COPY src/request_sender.py ./src/request_sender.py
COPY ["predict.py", "kitchenware_app.py", "./"]

EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "kitchenware_app.py","--server.port=8501", "--server.address=0.0.0.0"]
