FROM python:3.9.13-slim

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY  app.py app.py
COPY similiarity.py similiarity.py

ENTRYPOINT ["streamlit", "run", "app.py"]

CMD ["--server.port=4321", "--server.address=0.0.0.0"]