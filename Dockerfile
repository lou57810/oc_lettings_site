# base image
FROM python:3.12

# Maintenance dockerfile:
# MAINTAINER lou57810 <lou57810@foo.com>	deprecated
ENV PYTHONBUFFERED 1
# Eviter les fichiers .pyc dans les containers --> ralentissements
ENV PYTHONDONTWRITEBYTECODE 1

# RUN apt-get update
# copy just the requirements.txt first to leverage Docker cache
# install all dependencies for Python app
# COPY ./requirements.txt /app/requirements.txt
# COPY requirements.txt /app
# COPY ./requirements.txt /app
RUN mkdir /app


# RUN python manage.py migrate --noinput
# RUN python manage.py collectstatic --noinput

# copy all content to work directory /app
COPY . /app
WORKDIR /app

# install dependencies in requirements.txt
RUN pip3 install -r /app/requirements.txt
RUN python manage.py collectstatic --noinput
# RUN gunicorn -w 4 
ADD oc-lettings-site.sqlite3 /app

# volume:
# 	- static: /static

# specify the port number the container should expose
EXPOSE 8000

# run the application
# CMD ["python", "/app/main.py"]
# CMD python manage.py runserver
# ENTRYPOINT ["python", app/manage.py"]
# CMD ["runserver", 0.0.0.0:8000"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
