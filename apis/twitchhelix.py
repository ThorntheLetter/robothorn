import requests

BASE_URL = https://api.twitch.tv/helix/

def init(clientid=None, oath=None):
    global HEADER = {}
    if clientid:
        HEADER['Client-ID'] = clientid
    if oath:
        HEADER['Authorization'] = 'Bearer ' + oath

def request(method, url, args=None):
    reponse = requests.request(method, BASE_URL + url, headers=HEADER, params=args)
    return response.json()

def build_request(method, url, default_args=None):
    def nrequest(args=None):
        full_args = {**default_args, **args}
        return request(method, url, args=full_args)
    return nrequest

def get_stream(username):
    return request('GET', 'streams', {'user_login': username})['data'][0]
