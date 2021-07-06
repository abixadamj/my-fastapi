# FROM tiangolo/uvicorn-gunicorn-fastapi
FROM python:3.9-alpine

WORKDIR /app
COPY ./app /app
# RUN apt-get update 
RUN apk add py-gunicorn
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5501
CMD ["python", "main.py"]
# ENTRYPOINT ["/app/entrypoint.sh"]
