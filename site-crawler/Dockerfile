FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Playwright / Chromiumに必要なライブラリをインストール
RUN apt-get update && apt-get install -y \
  wget \
  curl \
  ca-certificates \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Chromiumをインストール
RUN playwright install --with-deps chromium

COPY src ./src

RUN mkdir -p /app/screenshots /app/downloads

CMD ["python", "src/main.py"]