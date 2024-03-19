# 使用 Python 官方提供的 Python 鏡像作為基礎映像
FROM python:3.11-slim

# 設置工作目錄
WORKDIR /app

# 複製應用程式依賴項清單
COPY requirements.txt .

# 安裝依賴項
RUN pip install --no-cache-dir -r requirements.txt

# 複製應用程式代碼到映像中
COPY . .

# 開放容器的端口
EXPOSE 5000

# 定義執行命令，啟動 Flask 應用程式
CMD ["python", "app.py"]