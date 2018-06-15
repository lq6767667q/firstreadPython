# pip3 install requests
import requests
import json
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException

def get_access_token():
    """
    获取微信全局接口的凭证(默认有效期俩个小时)
    如果不每天请求次数过多, 通过设置缓存即可
    """
    result = requests.get(
        url="https://api.weixin.qq.com/cgi-bin/token",
        params={
            "grant_type": "client_credential",
            "appid": "wx40f71ecdd1e07bc3",
            "secret": "ff008a1fe40993149b22f2c7d0d4188a",
        }
    ).json()

    if result.get("access_token"):
        access_token = result.get('access_token')
    else:
        access_token = None
    print(access_token)
    return access_token

def sendmsg(openid,msg):

    # access_token = get_access_token()
    access_token = '6_tps-TE9KLSYcu5g-JHgqdqWnwPQSV1cjudygzAhjFQaAHvto47kMlBywA8xXA4Vw5PT4t4Gf-Ojj7xGRRv3UUI9g-hxsb4M1Sibcw5qFbTBIodybomimqwwsUcXejwLvvAmacOFv-87epsUqBXIeAGAVRC'

    body = {
        "touser": "oiU7c0-RPA0vBOnV_y-0KocLC39Y",
        # "touser": "oiU7c02qvosUQVNDz4XSvDwciaJ8",
        "template_id": "r7fEKuzF8-IaaMcg4dB7QuQXGYbHYlx56yE9oybKGBM",
        "url": "http://www.aprilqi.top/wx_flask",
        "topcolor": "#FF0000",
        "data": {
            "keyword": {
                "value": "biu~~~~",
                "color": "#173177"
            }
        }
    }
    response = requests.post(
        url="https://api.weixin.qq.com/cgi-bin/message/template/send",
        params={
            'access_token': access_token
        },
        data=bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8')
    )
    # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
    result = response.json()
    print(result)



if __name__ == '__main__':
    sendmsg('oiU7c0-RPA0vBOnV_y-0KocLC39Y','biu~~~~')