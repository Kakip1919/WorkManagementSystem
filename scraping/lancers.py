from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

lists = {}
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome('../chromedriver', options=options)
driver.get('https://www.lancers.jp/work/search/system?open=1&ref=header_menu')


def replace_words(word):
    return word.replace("\n", "").replace(" ", "").replace("　", "")


driver.execute_script(
    "window.location.href='https://www.lancers.jp/work/search/system?open=1&ref=header_menu&show_description=1&sort=started&work_rank%5B%5D=0&work_rank%5B%5D=2&work_rank%5B%5D=3'")

for i in range(30):
    job_url = driver.execute_script(
        "return document.querySelector('body > div.l-wrapper > div.l-base.l-base--gray.p-search.p-search-job > main > section > section > div.c-paper.p-search__contents.l-search-section-content.clearfix > div.p-search__right > div.c-media-list.c-media-list--forClient > div:nth-child({}) > div.c-media__content > div.c-media__content__right > a').href".format(
            i + 1))
    job_title = driver.execute_script(
        "return document.querySelector('body > div.l-wrapper > div.l-base.l-base--gray.p-search.p-search-job > main > section > section > div.c-paper.p-search__contents.l-search-section-content.clearfix > div.p-search__right > div.c-media-list.c-media-list--forClient > div:nth-child({}) > div.c-media__content > div.c-media__content__right > a > span').textContent".format(
            i + 1))
    job_price = driver.execute_script(
        "return document.querySelector('body > div.l-wrapper > div.l-base.l-base--gray.p-search.p-search-job > main > section > section > div.c-paper.p-search__contents.l-search-section-content.clearfix > div.p-search__right > div.c-media-list.c-media-list--forClient > div:nth-child({}) > div.c-media__content > div.c-media__content__right > div:nth-child(3) > div > span.c-media__job-price').textContent".format(
            i + 1))
    job_description = driver.execute_script(
        "return document.querySelector('body > div.l-wrapper > div.l-base.l-base--gray.p-search.p-search-job > main > section > section > div.c-paper.p-search__contents.l-search-section-content.clearfix > div.p-search__right > div.c-media-list.c-media-list--forClient > div:nth-child({}) > div.c-media__content > div.c-media__content__right > div:nth-child(6)').textContent".format(
            i + 1))

    lists[i] = {
        "job_url": replace_words(job_url),
        "job_description": replace_words(job_description),
        "job_title": replace_words(job_title),
        "job_price": replace_words(job_price),
    }
