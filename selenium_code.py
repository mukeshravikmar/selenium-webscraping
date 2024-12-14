from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
import time
from pymongo import MongoClient
from googletrans import Translator  
client = MongoClient("mongodb://localhost:27017/")  
db = client["web_scraping"]
collection = db["test"]

url = 'https://www.youtube.com/ #paste your related content for scraping'
chrome_driver = "/usr/local/bin/chromedriver"
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
service = Service(chrome_driver)
browser = webdriver.Chrome(service=service, options=chrome_options)

browser.set_script_timeout(60)
browser.set_page_load_timeout(120)

browser.get(url)

WebDriverWait(browser, 20).until(
    EC.presence_of_all_elements_located((By.ID, "video-title-link"))
)
last_height = browser.execute_script("return document.documentElement.scrollHeight")
while True:
    browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(7)  
    new_height = browser.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

soup = BeautifulSoup(browser.page_source, 'lxml')
videos = soup.find_all('a', id='video-title-link')
translator = Translator()
for video in videos[:5]: 
    title = video.get('title').strip()
    if title.endswith(' - Tutorial'):
        title = title.rsplit(' - Tutorial', 1)[0]

    link = video.get('href')
    full_link = f'https://www.youtube.com{link}'

    aria_label = video.get('aria-label')
    if aria_label:
        match = re.search(r'(\d{1,3}(,\d{3})*) views (.+?) ago', aria_label)
        if match:
            views = match.group(1).replace(',', '')
            time_posted = match.group(3)

            try:
                browser.get(full_link)
            except Exception as e:
                print(f"Failed to navigate to {full_link}: {e}")
                continue  
            time.sleep(5)  
            browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(5)
            try:
                likes_element = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label^='like this video']"))
                )
                likes_text = likes_element.get_attribute('aria-label')
                likes = re.search(r'(\d[\d,]*)', likes_text).group(1).replace(',', '')
            except Exception as e:
                print(f"Error extracting likes for {full_link}: {e}")
                likes = 'N/A'

            comments = []
            last_comment_height = browser.execute_script("return document.documentElement.scrollHeight")

            while True:
                browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
                time.sleep(5) 
                
                comment_elements = browser.find_elements(By.XPATH, '//*[@id="contents"]//*[@id="content-text"]/span')
                for element in comment_elements:
                    comment_text = element.text.strip()
                    if comment_text and comment_text not in comments:
                        comments.append(comment_text)
                new_comment_height = browser.execute_script("return document.documentElement.scrollHeight")
                if new_comment_height == last_comment_height:
                    break
                last_comment_height = new_comment_height
            translated_comments = []
            for comment in comments:
                translated = translator.translate(comment, dest='en').text
                translated_comments.append(translated)
            video_data = {
                'title': title,
                'link': full_link,
                'views': views,
                'time_posted': time_posted,
                'likes': likes,
                'comments': translated_comments  
            }
            collection.insert_one(video_data)

browser.quit()