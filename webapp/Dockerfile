FROM python:3.9.15-alpine

RUN pip install fastapi uvicorn[standard]

WORKDIR /tmp/

CMD uvicorn src.main:app --reload --host 0.0.0.0
