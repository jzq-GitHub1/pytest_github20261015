import requests


class RequestUtil():
    session_util = requests.session()

    def send_request(self, method, url, **kwargs):
        res = RequestUtil.session_util.request(method=method, url=url, **kwargs)
        return res
