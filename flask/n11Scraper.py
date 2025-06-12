from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from app import app, db, Product, Comment

options = Options()
# options.add_argument("--headless")
service = Service()

driver = webdriver.Chrome(service=service, options=options)

url = "https://www.n11.com/urun/apple-ipad-2021-9-nesil-wi-fi-mk2n3tua-256-gb-102-tablet-gri-2154031?magaza=mertel"
driver.get(url)
produc_id = 4

time.sleep(2) # dynamic js loading wait

comments = driver.find_elements(By.XPATH, "//li[contains(@class, 'comment')]")
print(len(comments))

scraped_comments = []

for comment in comments:
    try:
        username = comment.find_element(By.CLASS_NAME, 'userName').text
        commentPlatform = "n11"
        rating = "yeah not doing this"
        userComment = comment.find_element(By.TAG_NAME, "p").text

        scraped_comments.append(Comment(product_id=3, user= username, text= userComment, rating=5, platform= commentPlatform))
    except:
        continue

driver.quit()


with app.app_context():
    db_comments = Comment.query.filter_by(product_id=produc_id).all()
    item_count_added = 0

    for comment in scraped_comments:
        flag = False
        for db_comment in db_comments:
            if db_comment.text == comment.text:
                flag = True 
                break
        
        if not flag:
            db.session.add(comment)
            item_count_added += 1
    db.session.commit()
    print(f"scraped data sucessfully, added {item_count_added} items")
