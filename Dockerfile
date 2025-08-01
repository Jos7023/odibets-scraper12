FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN playwright install
CMD ["python", "main.py"]