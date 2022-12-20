FROM  tiangolo/uwsgi-nginx-flask:latest

RUN pip install tweepy
COPY . ./

ENV PORT 8080

CMD ["python", "main.py"]
