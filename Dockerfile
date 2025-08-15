FROM python:3.11-slim
RUN apt-get update && apt-get install -y python3-tk
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["phyton", "final_project.py"]
