#Dockerfile
FROM python:3.8

WORKDIR /main
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./app/main.py ./app/main.py
COPY ./model ./model

# RUN pytest

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
