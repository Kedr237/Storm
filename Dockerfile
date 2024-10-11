FROM python:3.11.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip --no-cache-dir \
    && pip install -r requirements.txt --no-cache-dir

COPY . .

ENTRYPOINT ["python", "src/main.py"]