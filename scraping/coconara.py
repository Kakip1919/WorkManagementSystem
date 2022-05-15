from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def replace_words(word):
    return word.replace("\n", "").replace(" ", "").replace("　", "")


lists = {}
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument(
    '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0 Mobile/14C92 Safari/602.1')
driver = webdriver.Chrome('../chromedriver', options=options)

driver.get('https://coconala.com/requests/categories/11?categoryId=11&page=1')
WebDriverWait(driver, 10)
sleep(2)

post_count = driver.execute_script(
    "return document.querySelector('#__layout > div > div:nth-child(2) > div.c-searchPage > div.c-columns > div.c-columns_main > div.c-searchResults > div > div > div').childElementCount")

for i in range(post_count):
    job_url = driver.execute_script(
        "return document.querySelector('#__layout > div > div:nth-child(2) > div.c-searchPage > div.c-columns > div.c-columns_main > div.c-searchResults > div > div > div > a:nth-child({}) > div > div.c-itemInfo > div.c-itemInfo_title > a').href".format(
            i + 1))
    job_description = driver.execute_script(
        "return document.querySelector('#__layout > div > div:nth-child(2) > div.c-searchPage > div.c-columns > div.c-columns_main > div.c-searchResults > div > div > div > a:nth-child({}) > div > div.c-itemInfo > div.c-itemInfo_title > a').textContent".format(
            i + 1))
    job_title = driver.execute_script(
        "return document.querySelector('#__layout > div > div:nth-child(2) > div.c-searchPage > div.c-columns > div.c-columns_main > div.c-searchResults > div > div > div > a:nth-child({}) > div > div.c-itemInfo > div.c-itemInfo_title > a').textContent".format(
            i + 1))
    job_price = driver.execute_script(
        "return document.querySelector('#__layout > div > div:nth-child(2) > div.c-searchPage > div.c-columns > div.c-columns_main > div.c-searchResults > div > div > div > a:nth-child({}) > div > div.c-itemDetail > div.c-itemTile > div.c-itemTile_tile.c-itemTile_tile-budget > div.c-itemTileContent > div > span > span > span').textContent".format(
            i + 1))
    client_url = driver.execute_script(
        "return document.querySelector('#__layout > div > div:nth-child(2) > div.c-searchPage > div.c-columns > div.c-columns_main > div.c-searchResults > div > div > div > a:nth-child({}) > div > div.c-itemInfo > div.c-itemInfoUser > div.c-itemInfoUser_detail > div.c-itemInfoUser_name > a').href".format(
            i + 1))
    client_name = driver.execute_script(
        "return document.querySelector('#__layout > div > div:nth-child(2) > div.c-searchPage > div.c-columns > div.c-columns_main > div.c-searchResults > div > div > div > a:nth-child({}) > div > div.c-itemInfo > div.c-itemInfoUser > div.c-itemInfoUser_detail > div.c-itemInfoUser_name > a').textContent".format(
            i + 1))
    post_date = driver.execute_script(
        "return document.querySelector('#__layout > div > div:nth-child(2) > div.c-searchPage > div.c-columns > div.c-columns_main > div.c-searchResults > div > div > div > a:nth-child({}) > div > div.c-itemInfo > div.c-itemInfoUser > div.c-itemInfoUser_detail > div.c-itemInfoUser_info > div > span:nth-child(2)')".format(
            i + 1)).text

    lists[i] = {
        "job_url": replace_words(job_url),
        "job_description": replace_words(job_description),
        "job_title": replace_words(job_title),
        "job_price": replace_words(job_price),
        "client_name": replace_words(client_name),
        "client_url": replace_words(client_url),
    }
    print(lists[i]["job_description"])
