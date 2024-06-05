from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd
import time

# Credentials Entry
Celeb_name = 'Narendra Modi'
email = 'demev65739@crodity.com'
user_name = 'demev65739'
password_twitter = 'HELLOmf7810'

# Load the web driver
driver = webdriver.Chrome()
driver.get('https://twitter.com/i/flow/login')

time.sleep(3)

# Login using credential
email_input = driver.find_element("xpath", '//div/input')
time.sleep(2)
email_input.click()

time.sleep(2)
email_input.send_keys(email)
button = driver.find_element("xpath", '//div/button[2]')
time.sleep(2)
button.click()

time.sleep(3)

try:
    username_input = driver.find_element("xpath", '//div/input')
    username_input.click()
    time.sleep(5)
    username_input.send_keys(user_name)
    button = driver.find_element("xpath", '//div[@role="button"]/div/span/span')
    button.click()
except NoSuchElementException:
    username_input = driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
    username_input.click()
    button = driver.find_element("xpath", '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button/div')
    button.click()

time.sleep(10)

password_input = driver.find_element("xpath", '//div/input[@autocomplete="current-password"]')
time.sleep(2)
password_input.click()
password_input.send_keys(password_twitter)
button = driver.find_element("xpath", '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')
button.click()

time.sleep(10)

search = driver.find_element('xpath', '//div/div[2]/div/input')
time.sleep(3)
search.click()
search.send_keys(Celeb_name)
search.send_keys(Keys.ENTER)

time.sleep(3)

select_people = driver.find_element('xpath', "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]/a")
select_people.click()

time.sleep(3)

select_profile = driver.find_element('xpath', '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/section/div/div/div[1]/div/div/button/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]')
select_profile.click()

time.sleep(10)

soup = BeautifulSoup(driver.page_source, 'html.parser')
posting = soup.find_all("div", {"class": "css-146c3p1 r-8akbws r-krxsd3 r-dnmrzs r-1udh08x r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-bnwqim"})

# print(posting)

# quit()
# Scrolling and Saving to get new tweets

tweets = []
i= 1
try:
    while True:
        for index,post in enumerate(posting):
            tweets.append({"index":i,"Text":post.text})
            i = i+1
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        posting = soup.find_all("div", {"class": "css-146c3p1 r-8akbws r-krxsd3 r-dnmrzs r-1udh08x r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-bnwqim"})
        # tweets2 = list(set(tweets))
        if len(tweets) > 100:
            break
finally:
    driver.quit()

print(tweets)

# Saving the data into a csv file through pandas
df = pd.DataFrame(tweets)
df.to_excel('Tweets_scraping11111.xlsx', index=False)
print(df)







