from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from app import app, db, Product, Comment

options = Options()
options.add_argument("--headless")
service = Service()

driver = webdriver.Chrome(service=service, options=options)

url = "https://www.hepsiburada.com/vivaq/kadin-siyah-4-cepli-kapakli-kolon-askili-fermuar-ve-cit-cit-kapama-el-kol-ve-omuz-cantasi-p-895538051/yorumlar?boutiqueId=61&merchantId=512967&sav=true"
driver.get(url)

time.sleep(2) # dynamic js loading wait


comments = driver.find_elements(By.CLASS_NAME, "comment")

scraped_comments = []

for comment in comments:
    try:
        username = comment.find_element(By.CLASS_NAME, 'comment-info-item').text
        commentPlatform = "trendyol"
        rating = "yeah not doing this"
        userComment = comment.find_element(By.CLASS_NAME, "comment-text").text

        scraped_comments.append(Comment(product_id=3, user= username, text= userComment, rating=5, platform= commentPlatform))
    except:
        continue

driver.quit()


with app.app_context():
    db_comments = Comment.query.filter_by(product_id=3).all()
    item_count_added = 0

    for comment in scraped_comments:
        flag = False
        for db_comment in db_comments:
            if db_comment.text == comment.text:
                flag = True 
                break
        
        if not flag:
            db.session.add(comment)
            item_count_added = 1
    db.session.commit()
    print(f"scraped data sucessfully, added {item_count_added} items")
