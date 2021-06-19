FROM python-3.9.5-slim-buster

ARG SERVER_HOST=0.0.0.0
ARG SERVER_PORT=8080

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ="Europe/Moscow"
ENV SERVER_HOST=${SERVER_HOST}
ENV SERVER_PORT=${SERVER_PORT}

WORKDIR app
COPY . /app

RUN pip3 install --upgrade pip \
    && apt-get update \
    && apt-get install gcc g++ tini python3-dev -y \
    && apt-get clean \
    && pip install --upgrade -r /app/requirements.txt

ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["sh", "-c", "uvicorn server_configs.asgi:app --host ${SERVER_HOST} --port ${SERVER_PORT}"]
