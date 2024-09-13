FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requrements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
