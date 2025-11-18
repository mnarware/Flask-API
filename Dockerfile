FROM python:3.14.0-slim
WORKDIR /mydocker

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt 

COPY . .

CMD ["python3", "-m", "flask", "--app", "loan", "run", "--host", "0.0.0.0", "--port", "5000"]