FROM python:3.9-alpine

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt; \
    adduser --disabled-password --gecos "" --home /home/app --shell /bin/bash app; \
    chown -R app:app /home/app /app;

USER app
ENV HOME /home/app

CMD ["gunicorn", "--keep-alive", "10", "--bind", "0.0.0.0:5000", "app:app"]
EXPOSE 5000
