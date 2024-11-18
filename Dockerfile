FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 9000

ENTRYPOINT ["fastapi", "run", "app.py", "--port", "9000"]

