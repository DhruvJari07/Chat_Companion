FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY app_test.py ./

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "app_test.py", "--server.port=8501", "--server.address=0.0.0.0"]



