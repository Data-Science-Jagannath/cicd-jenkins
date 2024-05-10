FROM python:3.10-slim-buster
# Slim: The "slim" variant typically means that the image is stripped down to reduce its size by removing unnecessary packages and dependencies. It contains the minimal set of packages needed to run Python applications. This helps in reducing the image size, making it more lightweight and efficient.
# python:3.10-slim-buster is a Docker image that provides a lightweight environment for running Python 3.10 applications on the Debian 10 operating system

Run apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY . /code
#copy to code directory

RUN chmod +x /code/src
#set permissions

RUN pip install --no-cache-dir --upgrade -r code/src/requirements.txt
 
EXPOSE 8005

WORKDIR /code/src

ENV PYTHONPATH "${PYTHONPATH}:/code/src"
# this will help to access all the package that we required

CMD pip install -e .
# Inside this current working directory (/code/src) we will install this package under prediction_model

