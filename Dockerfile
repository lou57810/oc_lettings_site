# base image
# FROM python:3.11-bookworm
FROM python:3.12

# copy all content to work directory /app
COPY . /app

# copy just the requirements.txt first to leverage Docker cache
# install all dependencies for Python app
# COPY ./requirements.txt /app/requirements.txt
# COPY requirements.txt /app
COPY ./requirements.txt /app
# install dependencies in requirements.txt
# RUN pip install -r requirements.txt
RUN pip install -r /app/requirements.txt

ADD oc-lettings-site.sqlite3 /app

WORKDIR /app

# specify the port number the container should expose
EXPOSE 8000

# run the application
# CMD ["python", "/app/main.py"]
# CMD python manage.py runserver
# ENTRYPOINT ["python", app/manage.py"]
# CMD ["runserver", 0.0.0.0:8000"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

