FROM python:3.9.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN pip install --upgrade pip

COPY requirements.txt /code/   

RUN python -m pip install -r requirements.txt

COPY . /code/