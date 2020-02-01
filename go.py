import time
import re
import requests
from requests import RequestException
from selenium import webdriver

SLEEP_TIME = 60
URL = r'https://www.52pojie.cn/forum-8-1.html'

#这是一个修改
def get_content():
    try:
        data = requests.get(URL)
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
    keyword = ["mg", "c4d", "ae", "李辰"]
    pattern_key = re.compile(r'class="s xst">(.*?)</a>')
    result = re.findall(pattern_key, html)
    for temp in keyword:
        for list_str in result:
            if temp in list_str:
                print(temp, list_str)
                return list_str
    return ''


def action_go() -> str:
    # 1. get html from url
    html = get_content()

    # 2. parse html
    content_str = parse_page_detail(html)
    return content_str


if __name__ == '__main__':
    for _ in range(100000):
        content = action_go()

        if content != '':
            driver = webdriver.Chrome()
            driver.get(URL)
            time.sleep(SLEEP_TIME)
            exit()
        else:
            print(">>> 没有匹配的项目")
        time.sleep(SLEEP_TIME)
