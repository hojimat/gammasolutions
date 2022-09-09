FROM python:3.8
ENV PYTHONBUFFERED=1
WORKDIR /gamma
COPY requirements.txt /gamma/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /gamma/
