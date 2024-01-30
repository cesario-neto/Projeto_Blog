FROM python:3.12.1-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY app ./app
COPY scripts ./scripts
WORKDIR /app

EXPOSE 8000

RUN python -m venv /venv &&\
    /venv/bin/pip install --upgrade pip &&\
    /venv/bin/pip install -r /app/requirements.txt &&\
    chmod -R +x /scripts

ENV PATH="/scripts:/venv/bin:$PATH"

CMD [ "commands.sh" ]
