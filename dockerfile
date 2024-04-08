# 使用 Ubuntu 作為基礎映像
FROM ubuntu:latest

# 設定環境變量，避免一些安裝時的警告訊息
ENV DEBIAN_FRONTEND=noninteractive

# 更新 Ubuntu 軟體源，安裝必要的套件和工具
RUN apt-get update && apt-get install -y python3.11 python3-pip net-tools htop wget gnupg && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
# 下載並安裝 Google Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb && \
    apt-get -f install -y && \
    rm google-chrome-stable_current_amd64.deb




# 设置 Chrome 无头模式标志
ENV CHROME_PATH="/usr/bin/google-chrome-stable"
ENV CHROME_DRIVER_PATH="/usr/bin/chromedriver"
ENV CHROME_FLAGS="--headless --disable-gpu --no-sandbox"

# 在容器內建立工作目錄
WORKDIR /app

# 複製所需的程式碼到容器內的工作目錄
COPY . /app

# 安裝所需的 Python 套件
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

# 指定 Flask 應用程式運行的指令
CMD ["python3", "app.py"]