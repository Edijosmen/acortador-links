FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
COPY requeriments.txt /code/
RUN pip install -r requeriments.txt
RUN pip install pyshorteners
RUN pip install pymysql
