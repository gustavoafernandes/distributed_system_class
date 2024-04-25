# Instructions for Docker on how to build the Flask 
# application's image, including setting up the Python 
# environment, installing dependencies, and starting 
# the application.

FROM python:3.10-slim

WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /app

CMD ["python3", "src/app.py"]
