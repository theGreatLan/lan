#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
import logging
import re
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(pathname)s:%(lineno)d][%(funcName)s][%(name)s][%(levelname)s] %(message)s',
                    filename='imgs1.log',
                    filemode='a'
                    )

headers = {
    'Origin': 'http://thznn.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
}


def get_img(url):
    logging.info('================' + url + '================')
    res = ''
    try:
        r = requests.get(url, timeout=3, headers=headers)
        res = r.text
        # logging.info(r.text)
    except Exception as e:
        logging.exception(e)

    # with open('./res','w+') as file:
    #     file.write(res)

    ary_url = re.findall(r'id="normalthread(.+?).html"', res, re.S)
    ary_new_url = []
    for i in ary_url:
        index = i.rfind('"') + 1
        path = i[index:].encode('utf-8')
        html = 'http://thznn.com/' + path + '.html'
        ary_new_url.append(html)

    logging.info(ary_new_url)

    num = 0
    for url in ary_new_url:
        num += 1
        logging.info('------第' + str(num) + '页------')
        logging.info(url)
        try:
            r = requests.get(url, timeout=3, headers=headers)
            res = r.text
            # logging.info(r.text)
        except Exception as e:
            logging.exception(e)
            continue

        # with open('./res', 'w+') as file:
        #     file.write(res)

        file_dir = os.getcwd() + '/imgs/' + url[url.rfind('/')+1: -5]
        if not os.path.exists(file_dir):
            os.mkdir(file_dir)

        ary_url = re.findall(r'\sfile="(.+?)"', res, re.S)
        logging.info(ary_url)

        for img in ary_url:
            img_ext = img[(img.rfind('.')+1):]
            if img_ext != 'jpg' and img_ext != 'jpeg' and img_ext != 'png' and img_ext != 'JPG' and img_ext != 'PNG':
                continue

            if img[0:1] == '/':
                img = 'http://thznn.com' + img
            logging.info(img)
            try:
                response = requests.get(img, headers=headers)
                img_data = response.content
                dir = file_dir + '/' + img[(img.rfind('/') + 1):]
                logging.info(dir)
                with open(dir, 'wb') as f:
                    f.write(img_data)
            except Exception as e:
                logging.exception(e)
                continue

    logging.info('-----END-------')


urls = [
    'http://thznn.com/forum-181-11.html',
    #     'http://thznn.com/forum-181-12.html',
    #     'http://thznn.com/forum-181-13.html',
    #     'http://thznn.com/forum-181-14.html',
    #     'http://thznn.com/forum-181-15.html',
    #     'http://thznn.com/forum-181-16.html',
    #     'http://thznn.com/forum-181-17.html',
    #     'http://thznn.com/forum-181-18.html',
    #     'http://thznn.com/forum-181-19.html',
    #     'http://thznn.com/forum-181-20.html',
    #     'http://thznn.com/forum-181-21.html',
    #     'http://thznn.com/forum-181-22.html',
    #     'http://thznn.com/forum-181-23.html',
    #     'http://thznn.com/forum-181-24.html',
    #     'http://thznn.com/forum-181-25.html',
    #     'http://thznn.com/forum-181-26.html',
    #     'http://thznn.com/forum-181-27.html',
    #     'http://thznn.com/forum-181-28.html',
    #     'http://thznn.com/forum-181-29.html',
    #     'http://thznn.com/forum-181-30.html',
    #     'http://thznn.com/forum-181-30.html',
    #     'http://thznn.com/forum-181-30.html',
    #     'http://thznn.com/forum-181-30.html',
    #     'http://thznn.com/forum-181-30.html',
    #     'http://thznn.com/forum-181-30.html',
        'http://thznn.com/forum-181-31.html',
        'http://thznn.com/forum-181-32.html',
        'http://thznn.com/forum-181-33.html',
        'http://thznn.com/forum-181-34.html',
        'http://thznn.com/forum-181-35.html',
        'http://thznn.com/forum-181-36.html']

for url in urls:
    get_img(url)