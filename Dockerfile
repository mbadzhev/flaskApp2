FROM python:3.9

RUN pip install --upgrade pip

WORKDIR /flaskapp

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

EXPOSE 5000

EXPOSE 80

ENTRYPOINT ["python"]

CMD ["./app/main.py"]
