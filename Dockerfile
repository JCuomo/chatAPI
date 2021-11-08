FROM python:3


WORKDIR /chat-app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./chatapi ./chatapi
COPY run.py .

EXPOSE 8080

CMD ["python","./run.py"]
