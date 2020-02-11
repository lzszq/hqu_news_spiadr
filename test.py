# -*- coding: utf-8 -*-

from flask import Flask, render_template

import mix

app = Flask(__name__, template_folder = '/myproject/venv/hqu_news_project/templates')

with open("/myproject/venv/hqu_news_project/count.txt", 'w',encoding='utf-8') as me:
    me.write('')
    me.close()

@app.route('/hqu_news')

def hqu_news():
    mix.hqu_module

    websites_txt = []

    with open("/myproject/venv/hqu_news_project/hqu_news.txt", encoding='utf-8') as me:
        websites = str(me.read())


    websites_str = ''

    for letter in websites:
        if letter != '\n':
            websites_str = websites_str + letter
        elif letter == '\n':
            websites_txt.append(f'{websites_str}')
            websites_str = ''

    site = []
    title = []
    for i in range(len(websites_txt)):
        if (i%2)==0:
            site.append(websites_txt[i])
        elif (i%2)!=0:
            title.append(websites_txt[i])

    with open("/myproject/venv/hqu_news_project/count.txt", 'a',encoding='utf-8') as me:
        me.write('1')
        me.close()
    with open("/myproject/venv/hqu_news_project/count.txt", encoding='utf-8') as me:
        counts_of_visit = len(str(me.read()))

    html =  render_template('index.html', site = site, title =title, counts_of_visit = counts_of_visit)
    return html

if __name__ == '__main__':
    app.run()
