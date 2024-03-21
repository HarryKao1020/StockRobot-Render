# 使用 Python 官方提供的 Python 鏡像作為基礎映像
# FROM python:3.11-slim

# # 設置工作目錄
# WORKDIR /app

# # 複製應用程式依賴項清單
# COPY requirements.txt .

# # 安裝依賴項
# RUN pip install --no-cache-dir -r requirements.txt

# # 複製應用程式代碼到映像中
# COPY . .

# # 開放容器的端口
# EXPOSE 5000

# # 定義執行命令，啟動 Flask 應用程式
# CMD ["python", "app.py"]

# ======== For ubuntu
# 使用 Ubuntu 作為基礎映像
FROM ubuntu:latest

# 設定環境變量，避免一些安裝時的警告訊息
ENV DEBIAN_FRONTEND=noninteractive

# 更新 Ubuntu 軟體源，安裝必要的套件和工具
RUN apt-get update && apt-get install -y python3.11 python3-pip net-tools htop  && apt-get clean && rm -rf /var/lib/apt/lists/*

# net-tools：這是一個 Linux 網路工具集合，提供了一系列用於管理和診斷網路的命令，如 ifconfig、netstat、route 等。它允許你檢視網路接口、查詢路由表、檢視網路連接狀態等。在容器中安裝 net-tools 可以方便地查看和調試容器內部的網路配置。
# htop：這是一個互動式的系統監視器和流程管理器，類似於 Linux 上的 top 命令，但提供了更多的功能和更直觀的界面。它顯示了系統資源使用情況的即時資訊，如 CPU、記憶體、交換空間、進程等。安裝 htop 可以幫助你更好地監視容器內的系統資源使用情況，以及進程的運行狀態。

# 在容器內建立工作目錄
WORKDIR /app

# 複製所需的程式碼到容器內的工作目錄
COPY . /app

# 安裝所需的 Python 套件
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

# 指定 Flask 應用程式運行的指令
CMD ["python3", "app.py"]