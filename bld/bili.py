import os
import sys
from urllib import request
import time
import ffd
import random
import socket
import struct
import json
import hashlib


def __request(url, method='GET', header={}):
    randIp = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
    return request.Request(
        url = url,
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
            'X-Forwarded-For': randIp,
            **header},
        method = method)

def getPlayUrl(bvid, cid):
    entropy = 'rbMCKn@KuamXWlPMoJGsKcbiJKUfkPF_8dABscJntvqhRSETg'
    appkey, sec = ''.join([chr(ord(i) + 2) for i in entropy[::-1]]).split(':')
    params = 'appkey={appkey}&cid={cid}&otype=json&qn=80&quality=80&type=flv'.format(
        cid=cid, appkey=appkey)
    chksum = hashlib.md5(bytes(params + sec, 'utf8')).hexdigest()
    play_url = 'https://interface.bilibili.com/v2/playurl?%s&sign=%s' % (params, chksum)
    with request.urlopen(__request(play_url, header={'Referer': 'https://interface.bilibili.com'})) as res:
        content = json.loads(res.read().decode("UTF-8"))
    try:
        print('quality: %s' % content['quality'])
        return content['durl'][0]['url']
    except Exception as e:
        print(content)
        raise e

def download(bvid, threads=None, output=None, dest=None, force=False):
    view_url = 'https://api.bilibili.com/x/web-interface/view?bvid=' + bvid
    with request.urlopen(__request(view_url)) as res:
        content = json.loads(res.read().decode("UTF-8"))

    cid = content['data']['pages'][0]['cid']
    title = content['data']['title']
    play_url = getPlayUrl(bvid, cid)

    opener = request.build_opener()
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'),
        ('Accept', '*/*'),
        ('Accept-Language', 'en-US,en;q=0.5'),
        ('Accept-Encoding', 'gzip, deflate, br'),
        # ('Range', 'bytes=0-'),
        ('Referer', view_url),
        ('Origin', 'https://www.bilibili.com'),
        ('Connection', 'keep-alive'),
    ]
    request.install_opener(opener)
    ffd.download(url=play_url, threads=threads, dest=dest, output=output or (bvid + '.flv'), force=force)



