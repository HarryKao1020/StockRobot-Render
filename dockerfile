# 使用 Ubuntu 作為基礎映像
FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    build-essential \
    wget \
    unzip \
    libssl-dev \
    libffi-dev \
    && apt-get clean

# 在容器內建立工作目錄
WORKDIR /app

# 複製所需的程式碼到容器內的工作目錄
COPY . /app


# 安裝所需的 Python 套件
RUN pip3 install --no-cache-dir -r requirements.txt

# # 設定環境變量，避免一些安裝時的警告訊息
# ENV DEBIAN_FRONTEND=noninteractive

EXPOSE 5000

# 指定 Flask 應用程式運行的指令
CMD ["python3", "app.py"]