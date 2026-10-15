import pytest
from common.get_csrf import get_csrf_token
from common.read_yaml import read_yaml_data
from common.request_util import RequestUtil
from common.find_file import find_path

csrf_token = get_csrf_token()
def test_login():
    url = "http://47.107.116.139/phpwind/index.php?m=u&c=login&a=dorun"
    data = {
        "username": "13345678901",
        "password": "123456",
        "backurl": "http://47.107.116.139/phpwind/",
        "invite": "",
        "csrf_token": read_yaml_data(file_path=find_path(dir_name="yaml_file",file_name="new_write_data.yaml"),
                                     key_name="csrf_token")
    }
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "X-Requested-With": "XMLHttpRequest"
    }

    # res = requests.post(url=url, data=data, headers=headers, cookies=cookies)
    res = RequestUtil().send_request(method="post", url=url, data=data, headers=headers)
    print(res.json())
    assert res.json()["state"] == "success"


if __name__ == '__main__':
    pytest.main(["-vs"])


# def get_csrf_token():
#     global csrf_token1
#     url = "http://47.107.116.139/phpwind/"
#     session = requests.Session()
#     # 先发起请求以获取 Cookie
#     session.get(url=url)
#
#     # 直接从 CookieJar 中获取指定 key 的值
#     csrf_token = session.cookies.get("csrf_token")  # 注意：key 名称取决于后端框架，Django 默认为 'csrftoken'，其他可能为 'XSRF-TOKEN' 等
#     print(csrf_token)


# ---------
# res = RequestUtil().send_request(method="get", url=url)
# csrf_token_value = re.search('csrf_token" value="(.*?)"', res.text)
# csrf_token1 = csrf_token_value.group(1)
# print(csrf_token1)
# return csrf_token1
#----------
#
#     # data = {
#     #     "username": "msxyname",
#     #     "password": "msxypassword",
#     #     "backurl": "http://47.107.116.139/phpwind/",
#     #     "invite": "",
#     #     "csrf_token": csrf_token
#     # }
#     # data = {
#     #     "username": "18331560173",
#     #     "password": "18331560173",
#     #     "backurl": "http://47.107.116.139/phpwind/",
#     #     "invite": "",
#     #     "csrf_token": read_yaml_data("./yaml_file/new_write_data.yaml","csrf_token")
#     # }
#
