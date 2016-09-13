import os.path
import re
import urllib.request
from functools import reduce
from bs4 import BeautifulSoup


def dir_tree(path, st, slp, dir_lst):
    dir_name = os.listdir(path)
    st_txt = st
    slp_txt = slp

    n = 0
    for dirnm in dir_name:
        # print(path + dirnm, os.path.isfile(path + '\\' + dirnm), os.path.isdir(path + '\\' + dirnm))
        if os.path.isfile(path + '\\' + dirnm):
            dir_lst.append(st_txt + slp_txt + dirnm)

        elif os.path.isdir(path + '\\' + dirnm):

            dir_lst.append(st_txt + slp_txt + dirnm)
            dir_tree(path + '\\' + dirnm, '|   ' + st, slp, dir_lst)

        else:
            continue
        n += 1


def txt_grep(file, keyword):
    lines = []
    f = open(file, 'r').readlines()
    for line in f:
        if keyword in line:
            lines.append(line)
    return lines


def txt_wrap1(file, max):
    lines = []
    if max > 0:
        f = open(file, 'r').readlines()

        for line in f:
            if len(line) > max - 1:
                n = len(line) // max + 1
                for i in range(n):
                    lines.append(line[i * max : (i+1) * max] + '\n')
                    i += 1
            else:
                lines.append(line)
    else:
        print('The width should be big than 0!')

    return lines


def txt_wrap2(file, max):
    lines = []
    if max > 0:
        wordList = open(file).read().split()
        lenList = list(map(len, wordList))
        st = 0
        i  = 0
        for l in lenList:
            lst_index = int(reduce(lambda x, y: x + y, lenList[st : i + 1 ])) + i - st
            nxt_index = int(reduce(lambda x, y: x + y, lenList[st : i + 2 ])) + i -st + 1
            if (lst_index <= max) and  (nxt_index > max):
                # print(st, i, lst_index, nxt_index, wordList[st : i + 1 ])
                lines.append(' '.join(wordList[st : (i + 1) ]) + '\n')
                st = i + 1
            # print(st, i, lines)
            i += 1

    return lines


def txt_freq(file):
    freq = {}
    words = re.sub(r'[,.;?)(]', '', open(file).read()).split()
    for wd in words:
        freq[wd] = freq.get(wd, 0) + 1

    return freq


def gg_crawle(word, filepath):
    # 设置url
    url = "https://www.google.co.jp/#q="

    # 伪装浏览器环境
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}

    # 传入关键词,百度的关键词标签是wd
    values = {'q': word}

    # 转码
    urlf = url
    # print urlf

    # 取结果
    response = urllib.request.urlopen(urlf)
    html = response.read()

    print(html)

    # 保存文件
    open(filepath, 'w').write(html)


def trace(f):
    f.indent = 0
    def g(x):
        print('| ' * f.indent + '|--', f.__name__ , x)
        f.indent += 1
        value = f(x)
        print('| ' * f.indent + '|--', 'return', repr(value))
        f.indent -= 1
        return value
    return g


def memoize(f):
    cache = {}
    def g(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return g


# def store_spider(url):
#     page = urllib.request.urlopen(url)
#     contents = page.read()
#     soup = BeautifulSoup(contents, 'html.parser')
#     # print(u'豆瓣电影250: 序号 \t影片名\t 评分 \t评价人数')
#     # print(soup)
#     for tag in soup.find_all('div', class_='item'):
#
#         # print()
#         # m_order = int(tag.find('td', class_='m_order').get_text())
#         # m_name = tag.a.get_text()
#         # m_year = tag.span.get_text()
#         # m_rating_score = float(tag.em.get_text())
#         # m_rating_num = int(tag.find(headers="m_rating_num").get_text())
#         # print("%s %s %s %s %s" % (m_order, m_name, m_year, m_rating_score, m_rating_num))

