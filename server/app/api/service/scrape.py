from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from bs4 import ResultSet
import time

from fastapi import FastAPI, HTTPException

from typing import List
import schemas.mylist as mylist_schema
from service.get_id_in_url import get_id_in_url

from utils.const_values import DANIME_MYLISTPAGE_BASE_URL, DANIME_ANIMEPAGE_BASE_URL


class Scrape:
    def __init__(self):
        pass

    def __get_html(self, url: str) -> BeautifulSoup:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome("chromedriver", options=options)
        driver.implicitly_wait(10)
        driver.get(url)
        html = driver.page_source.encode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        return soup

    def mylist(self, id: str) -> List[mylist_schema.MyListContent]:
        soup = self.__get_html(f"{DANIME_MYLISTPAGE_BASE_URL}?shareListId={id}")
        # print(soup.prettify())

        title_elm_list: List[ResultSet] = soup.find_all("span", class_="ui-clamp")
        link_elm_list: List[ResultSet] = soup.find_all("a", class_="itemModuleIn")

        mylist_list: List[mylist_schema.MyListContent] = []
        for (title_elm, link_elm) in zip(title_elm_list, link_elm_list):
            mylist_list.append(
                mylist_schema.MyListContent(
                    anime_id=get_id_in_url(url=link_elm.get("href"), param_name="workId"), mylist_id=id
                )
            )

        if mylist_list == []:
            raise HTTPException(status_code=402, detail="mylist page not exist.")
        return mylist_list

    def anime_info(self, id: str) -> mylist_schema.AnimeInfo:
        soup = self.__get_html(f"{DANIME_ANIMEPAGE_BASE_URL}?workId={id}")
        first_title_elm = soup.find("span", class_="ui-clamp webkit2LineClamp")
        stories_tmp = soup.find("div", class_="titleWrap")
        image_elm = soup.find("img", class_="lazyloaded")

        stories = stories_tmp.h1.span.text
        title = stories_tmp.h1.text.replace(stories, "")
        image = image_elm.get("src")
        time.sleep(1)
        return mylist_schema.AnimeInfo(
            anime_id=id,
            first=first_title_elm.text,
            stories=stories,
            image=image,
            title=title,
            url=f"{DANIME_ANIMEPAGE_BASE_URL}?workId={id}",
        )
