#-*- coding:utf-8 -*-
import re
import requests

def dowmloadPic(html,keyword):

    pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
    i = 0
    print 'the keyword:'+keyword+'picture，is downloading...'
    for each in pic_url:
        print 'downloading the'+str(i+1)+'picture and store at:'+str(each)
        try:
            pic= requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print 'error'
            continue
        string = './data/boss/' + str(i) + '.jpg'
        #resolve the problem of encode, make sure that chinese name could be store
        fp = open(string.decode('utf-8').encode('cp936'),'wb')
        fp.write(pic.content)
        fp.close()
        i += 1



if __name__ == '__main__':
    word = "新垣结衣"
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'
    result = requests.get(url)
    dowmloadPic(result.text,word)
