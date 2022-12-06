# syntax=docker/dockerfile:1
FROM python:3.10-alpine
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80
ENV NAME World
CMD ["python", "./main.py"]