# 🎥 YouTube Web Scraper

This project is a powerful web scraper that extracts YouTube video data, including titles, views, likes, and translated comments, storing them in a MongoDB database.

---

## 🚀 Features
- 📊 Scrapes video titles, links, views, likes, and comments.
- 🌐 Translates comments to English using Google Translate.
- 🗄️ Stores data in a MongoDB collection.

---

## 🛠️ Prerequisites
1. **Python 3.x**
2. **Google Chrome and ChromeDriver**
3. **MongoDB (running locally)**
4. Required Libraries:
   - `selenium`
   - `beautifulsoup4`
   - `pymongo`
   - `googletrans==4.0.0-rc1`

---

## 💻 Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mukeshravikmar/selenium-webscraping.git
   cd selenium-webscraping
   ```

2. **Create a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Configuration
- **Update the Variables:**
  - Replace the YouTube URL in the `url` variable.
  - Ensure the correct ChromeDriver path in `chrome_driver`.

---

## ▶️ Usage
1. **Run the Script:**
   ```bash
   python selenium_code.py
   ```

2. **Check MongoDB:**
   Open MongoDB Compass or run a query in the MongoDB shell to verify the scraped data:
   ```bash
   mongo
   use web_scraping
   db.test.find().pretty()
   ```

---

## 📚 Documentation: Selenium Overview

Selenium is an open-source web automation framework used for web scraping and browser automation. In this project, it performs actions like opening YouTube, scrolling the page, and extracting video details.

### Selenium Key Concepts:
- **WebDriver:** Core component that controls the browser.
- **ChromeDriver:** Tool for controlling Google Chrome.
- **WebElement:** Represents elements on a web page.
- **Expected Conditions:** Helps wait for specific page conditions.

### How Selenium is Used Here:
1. **Setup:**
   ```python
   from selenium import webdriver
   from selenium.webdriver.chrome.service import Service
   from selenium.webdriver.chrome.options import Options
   from selenium.webdriver.common.by import By
   ```

2. **Browser Initialization:**
   ```python
   chrome_options = Options()
   chrome_options.add_argument('--headless')
   chrome_options.add_argument('--disable-gpu')
   service = Service('/path/to/chromedriver')
   browser = webdriver.Chrome(service=service, options=chrome_options)
   ```

3. **Page Navigation:**
   ```python
   browser.get(url)
   ``

4. **Element Interaction:**
   ```python
   browser.find_element(By.ID, 'video-title')
   ```

5. **Scroll Automation:**
   ```python
   browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
   ```

6. **Wait for Elements:**
   ```python
   from selenium.webdriver.support.ui import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC
   WebDriverWait(browser, 20).until(
       EC.presence_of_all_elements_located((By.ID, 'video-title-link'))
   )
   ```

---

## 🛑 Troubleshooting
- 🧩 Ensure ChromeDriver is in your PATH or provide the full path in the script.
- 🔄 Check if MongoDB is running.
- ✅ Use the correct versions of libraries.

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🤝 Contribution
Contributions are welcome! Feel free to submit issues and pull requests.

---

**Happy Scraping!** 🚀


## Connect with Me

- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/mukesh-p-r-a08ba7249?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)