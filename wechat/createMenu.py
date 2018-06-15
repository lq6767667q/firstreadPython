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

def createmenu():

    # access_token = get_access_token()
    access_token = '6_SXgAZ2-S7DE_Nq6ZFzpyoQqqj5zQYOZoC_TmhyioZlKm9RDsBr4DbhVnXS0Ii7_O96ZutNF0CYfaHN6saBmMQmhB5Tc_rOqeh5XMPzYM69ZNMqVDn5Gj-Xa7pdAj_8eAu96PRso4t4Djjw9XOSNfAJAKOJ'

    body = {
        "button": [
            {
                "type": "click",
                "name": "今日歌曲",
                "key": "V1001_TODAY_MUSIC"
            },
            {
                "name": "菜单",
                "sub_button": [
                    {
                        "type": "view",
                        "name": "搜索",
                        "url": "http://www.soso.com/"
                    },
                    {
                        "type": "click",
                        "name": "赞一下我们",
                        "key": "V1001_GOOD"
                    }]
            }]
    }
    response = requests.post(
        url="https://api.weixin.qq.com/cgi-bin/menu/create",
        params={
            'access_token': access_token
        },
        data=bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8')
    )
    # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
    result = response.json()
    print(result)



if __name__ == '__main__':
    createmenu()