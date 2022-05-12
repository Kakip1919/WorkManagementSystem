from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

lists = {}
options = webdriver.ChromeOptions()

# options.add_argument("--headless")

driver = webdriver.Chrome('../chromedriver', options=options)

driver.get(
    "https://crowdworks.jp/public/jobs/search?category_id=226&keep_search_criteria=true&order=new&hide_expired=false")

WebDriverWait(driver, 10)


def replace_words(word):
    return word.replace("\n", "").replace(" ", "").replace("　", "")


li_nodes = driver.execute_script(
    "return document.querySelector('#result_jobs > div.search_results > ul').childElementCount")
for i in range(li_nodes):
    job_title = driver.execute_script(
        "return document.querySelector('#result_jobs > div.search_results > ul > li:nth-child({}) > div > div > div.item_body.job_data_body > div.job_data_row > div.job_data_column.summary > h3 > a').textContent".format(
            i + 1))
    job_url = driver.execute_script(
        "return document.querySelector('#result_jobs > div.search_results > ul > li:nth-child({}) > div > div > div.item_body.job_data_body > div.job_data_row > div.job_data_column.summary > h3 > a').href".format(
            i + 1))
    job_description = driver.execute_script(
        "return document.querySelector('#result_jobs > div.search_results > ul > li:nth-child({}) > div > div > div.item_body.job_data_body > div.job_data_row > div.job_data_column.summary > div.item_description > p').textContent".format(
            i + 1))
    job_price = driver.execute_script(
        "return document.querySelector('#result_jobs > div.search_results > ul > li:nth-child({}) > div > div > div.item_body.job_data_body > div.job_data_row > div.job_data_column.entry > div > div.entry_data.payment > div > b').textContent".format(
            i + 1))
    client_name = driver.execute_script(
        "return document.querySelector('#result_jobs > div.search_results > ul > li:nth-child({}) > div > div > div.item_body.job_data_body > div.item_meta > div.client-information > span.user-name > a').textContent".format(
            i + 1))
    client_url = driver.execute_script(
        "return document.querySelector('#result_jobs > div.search_results > ul > li:nth-child({}) > div > div > div.item_body.job_data_body > div.item_meta > div.client-information > span.user-name > a').href".format(
            i + 1))
    post_date = driver.execute_script(
        "return document.querySelector('#result_jobs > div.search_results > ul > li:nth-child({}) > div > div > div.item_body.job_data_body > div.item_meta > div.post_date.meta_column').textContent".format(
            i + 1))

    lists[i] = {
        "job_url": replace_words(job_url),
        "job_description": replace_words(job_description),
        "job_title": replace_words(job_title),
        "job_price": replace_words(job_price),
        "client_name": replace_words(client_name),
        "client_url": replace_words(client_url),
        "post_time": replace_words(post_date)
    }

print(lists[5].values())