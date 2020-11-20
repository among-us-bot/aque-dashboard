FROM python:3.8
COPY requirements.txt ./
RUN pip install -r requirements.txt
WORKDIR dashboard/
COPY . ./
CMD ["python", "main.py"]
