FROM python:3.7-alpine

WORKDIR /app

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers
COPY ./backend/requirements /requirements
RUN pip install -r /requirements/requirements.txt

CMD ["flask", "run"]
