# 使用 Ubuntu 作為基礎映像
FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    python3-venv \
    build-essential \
    wget \
    unzip \
    libssl-dev \
    libffi-dev \
    && apt-get clean

# 创建并激活虚拟环境
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"


# 複製所需的程式碼到容器內的工作目錄
COPY . /app

# 在容器內建立工作目錄
WORKDIR /app

# 安裝所需的 Python 套件
RUN pip3 install -r requirements.txt


EXPOSE 5000

# 指定 Flask 應用程式運行的指令
CMD ["python3", "app.py"]