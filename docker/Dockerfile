FROM python:3.10-slim
RUN apt-get update && apt-get install -y gnupg ipfs tor curl && rm -rf /var/lib/apt/lists/*
RUN useradd -ms /bin/bash certmagicc
USER certmagicc
WORKDIR /home/certmagicc
COPY scripts/ ./scripts/
COPY certs/ ./certs/
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "bash" ]
