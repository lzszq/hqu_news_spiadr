class hqu_module:

    from urllib.request import Request, urlopen

    import random

    from bs4 import BeautifulSoup

    import re
    
    import time

    url = 'https://www.hqu.edu.cn/hdxw.htm'

    # 伪装其是通过浏览器访问

    ua_list = [

        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36", # chrome

        "Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN) AppleWebKit/537.36 (KHTML, like Gecko) Version/5.0.1 Safari/537.36", # safari

        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0", # Firefox

        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)" # IE

    ]

    ua = random.choice(ua_list)# 随机选择一个user-agent

    request = Request(url, headers = {'User-agent':ua})# 将ua加到请求头中

    response = urlopen(request)

    with response:

        with open('/myproject/venv/hqu_news_project/hqu_news.html', 'wb') as d:

            d.write(response.read())

    # 将爬到的网页存在hqu_news.html



    # 自动生成一个hqu_news.txt

    html_doc = open("/myproject/venv/hqu_news_project/hqu_news.html", encoding="utf-8") # 打开爬好的网页

    soup = BeautifulSoup(html_doc, 'html.parser')

    with open("/myproject/venv/hqu_news_project/hqu_news.txt", "w", encoding='utf-8') as me:  # 生成一个空文件

        me.write('')

        me.close() 

    strb = "https://www.hqu.edu.cn/"  # 数据中的链接缺少域名，添加域名

    for result in soup.find_all(href = re.compile("info/1067")):

        with open("/myproject/venv/hqu_news_project/hqu_news.txt", "a+", encoding='utf-8') as me:

            me.write(strb + str(result.get('href')))

            me.write('\n')

            me.write(result.get_text())

            me.write('\n')                            # 将网址和标题存入hqu_news.txt



    if __name__ == '__main__':

        localtime = time.asctime( time.localtime(time.time()) )

        print('successful', localtime)
