## 本機安裝程式

pip install Flask line-bot-sdk
pip install selenium beautifulsoup4 matplotlib numpy requests pandas datetime selenium python-dotenv

## sever 安裝套件

看 requirements.txt

---

# 本機上 ngrok 測試

### 步驟

1. 將程式包成 image
   `docker build -t {image名稱} .`
2. 啟動 image，產生 container
   `docker run -p {container端口:flask端口} --name {container name} {image名稱}`
3. 開新的 cmd ，將 ngrok 的壓縮檔從 window copy 到 container 的 root 底下
   `docker cp {.tgz的路徑}  {container name}:/root`
4. 進入 container
   `docker exec -u 0 -it {容器名稱或ID} /bin/bash `

5. 切到 root 底下
   `cd .. cd root `
6. 將 ngrok 檔案解壓縮
   `tar -xzvf {xxxx.tgz}`
7. 設定 ngrok 的 token
   `./ngrok authtoken {your_authtoken}`
8. 啟動 ngrok 的 http 端口，並配對到 flask 的 EXPOSE
   `./ngrok http {Linux本地端口}`
9. 將 forwarding URL 複製貼到 LINE DEV

---

# 佈署到 Render

### 步驟

1. 將程式打包成 image
   `docker build -t {image名稱} .`

2. 登入 docker(可以確認有沒有登入)
   `docker login`
3. 創立 repository 並把 image 加進去
   `docker tag {image name} {帳號名稱}/{repository name}:{tag}`
4. 將 image push 到 docker hub 的 repository
   `docker push {帳號名稱}/{repository name}:{tag}`
5. 到 Render 網站 Create Web Service
6. 選擇連接 docker hub
7. 設定 CHANNEL_ACCESS_TOKEN & CHANNEL_SECRET
8. 等待佈署完成將 url 貼到 LINE DEV
