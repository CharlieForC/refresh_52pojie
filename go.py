import time

import requests
from requests import RequestException
import re
from selenium import webdriver


def get_content(url):
    try:
        data = requests.get(url)
        if data.status_code == 200:
            return data.text
        return None
    except RequestException:
        print(">> RequestException")
        return None


def parse_page_detail(html) -> str:
    """
    keyword: mg, c4d, ae, 李辰
    :param html: html内容
    :return: 网页内容是否包含关键字：mg, c4d, ae, 李辰
    """
    keyword = ["mg", "c4d", "ae", "李辰", '百度']
    pattern_key = re.compile(r'class="s xst">(.*?)</a>')
    result = re.findall(pattern_key, html)
    for temp in keyword:
        for list_str in result:
            if temp in list_str:
                print(temp, list_str)
                return list_str
    return ''


def action_go() -> str:
    # 1. define url
    url = r'https://www.52pojie.cn/forum-8-1.html'

    # 2. get html from url
    html = get_content(url)

    # 3. parse html
    content_str = parse_page_detail(html)
    return content_str


if __name__ == '__main__':
    for _ in range(100000):
        content = action_go()

        if content != '':
            driver = webdriver.Chrome()
            url = r'https://www.52pojie.cn/forum-8-1.html'
            driver.get(url)
            time.sleep(10)
            exit()
        else:
            print(">>> 没有匹配的项目")
        time.sleep(10)
