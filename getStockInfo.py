from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# for chrome
from selenium.webdriver.chrome.options import Options
import os
import json




# ======== for local test / use Edge

# from selenium.webdriver.edge.service import Service
# # from selenium.webdriver.edge.options import Options



# # 获取当前脚本的目录
# current_directory = os.path.dirname(__file__)  # 使用__file__获取当前脚本的路径
# # 构建相对路径
# relative_path = "msedgedriver.exe"
# # 组合基准目录和相对路径
# absolute_path = os.path.join(current_directory, relative_path)
# # 使用absolute_path作为msedgedriver.exe的路径
# edge_driver_path = absolute_path
# # def scraple_website(url):

#     # Edge
#     edge_driver_path = './msedgedriver.exe'
#     s = Service(executable_path=edge_driver_path)

#     options = webdriver.EdgeOptions()
#     options.add_argument('--headless')
#     driver = webdriver.Edge(service=s,options=options)



#     # 打开目标URL
#     driver.get(url)

#     # 等待頁面加载完成的時間
#     # driver.implicitly_wait(10)

#     page_content = driver.page_source

#     soup = BeautifulSoup(page_content,'html.parser')

#     # 關閉
#     # driver.quit()

#     return soup

# ====== end local test


# for unbuntu && Render
def scraple_website(url):
    # 設定 Chrome WebDriver 的選項
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 启用无头模式
    chrome_options.add_argument("--disable-gpu")  # 禁用GPU加速
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--no-sandbox") # 必要的，否则会报错

    # 建一個 Chrome 實例
    driver = webdriver.Chrome(options=chrome_options)

    # 打开目标 URL
    driver.get(url)

    # 获取页面内容
    page_content = driver.page_source

    # 解析 HTML
    soup = BeautifulSoup(page_content, 'html.parser')

    # 关闭浏览器
    driver.quit()

    return soup

def getFearIndex():
    url = "https://alternative.me/crypto/fear-and-greed-index/"
    soup = scraple_website(url)
    
    # 查找包含 index-value的元素
    fear_index_element = soup.find("div", class_="fng-circle")
    #提取 "fear_index_element" 的内容
    fear_index = fear_index_element.text

    fear_index = int(fear_index)

    # 判斷fear index處於哪一個階段
    # <=25 Extreme Fear 
    # <45 Fear
    # >=45 Neutral
    # >=55 Greed
    # >=75 Extreme Greed
    if(fear_index < 25):
        fear_index_status = "Extreme Fear"
    elif(fear_index <45):
        fear_index_status = "Fear"
    elif(fear_index <55):
        fear_index_status = "Neutral"
    elif(fear_index < 75):
        fear_index_status = "Greed"
    else:
        fear_index_status= "Extreme Greed"
    
    fear_index_data = {
        "Fear Index" : fear_index,
        "Fear Index Status" : fear_index_status
    }
    #轉成json
    #fearIndex_json_data = json.dumps(fear_index_data)

    return fear_index_data

def getMaintenanceMargin():
    url = "https://www.istock.tw/post/twmarginrequirement"
    soup = scraple_website(url)

    #取頁面的p class=h1 font-bold m-t
    maintenance_margin = soup.find_all("p",class_="h1 font-bold m-t")
    
    #有4筆相同的，我們要的融資維持率在第二筆
    maintenance_margin_text = maintenance_margin[1].text

    maintenance_margin_data={
        "大盤融資維持率": maintenance_margin_text+"%"
    }

    #轉成json
    #maintenance_margin_json_data = json.dumps(maintenance_margin_data,ensure_ascii=False)
    return maintenance_margin_data
    # 查找包含 index-value的元素


# 測試
print(getFearIndex())
print(getMaintenanceMargin())
