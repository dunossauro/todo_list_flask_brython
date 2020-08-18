FROM python:3

# UPDATE SYSTEM
RUN apt-get update -y && apt-get upgrade -y --allow-unauthenticated
RUN apt-get install -y vim nginx supervisor
RUN pip install poetry

# SYS PREP
RUN mkdir -p /deploy/app
COPY . /deploy/app/
WORKDIR /deploy/app/
RUN poetry export -f requirements.txt > requirements.txt
RUN pip install -r requirements.txt

#NGINX
RUN rm /etc/nginx/sites-enabled/default
COPY flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

#SUPERVISORD
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# START APPLICATION
RUN flask db upgrade
ENTRYPOINT ["/usr/bin/supervisord"]
