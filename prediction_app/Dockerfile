FROM python:3.10.0

WORKDIR /user/app
COPY requirements-deploy.txt ./requirements.txt
RUN pip install --no-cache-dir -r ./requirements.txt

COPY models/ ./models/
COPY predict.py ./

EXPOSE 5050
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:5050", "predict:app"]
# ENTRYPOINT ["gunicorn", "predict:app"]