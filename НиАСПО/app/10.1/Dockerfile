FROM python:3.9-slim

WORKDIR /app

COPY con1.py .

RUN pip install --no-cache-dir flask

EXPOSE 5000

CMD ["python", "con1.py"]
