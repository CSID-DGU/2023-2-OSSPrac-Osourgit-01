FROM tiangolo/uwsgi-nginx-flask:latest
COPY ./app /app
CMD [ "python", "./main.py" ]