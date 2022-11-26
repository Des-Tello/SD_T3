FROM python:3.10.8-slim-buster

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install flask
RUN pip install requests

COPY . .

EXPOSE 8001


ENTRYPOINT [ "python" ]
CMD [ "app.py"]