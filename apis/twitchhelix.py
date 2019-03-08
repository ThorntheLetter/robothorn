import requests

BASE_URL = 'https://api.twitch.tv/helix/'

def mkheader(args):
    header = {}
    if 'client-id' in args:
        header['Client-ID'] = args['client-id']

    if 'oauth' in args:
        header['Authorization'] = 'Bearer ' + args['oauth']

    return header

def request(method, url, args=None, header=None):
    response = requests.request(method, BASE_URL + url, headers=header, params=args)
    return response.json()

def build_request(method, url, header=None, default_args=None):
    def nrequest(args=None):
        full_args = {**default_args, **args}
        return request(method, url, args=full_args, header=header)
    return nrequest

def get_stream(username, header):
    return request('GET', 'streams', args={'user_login': username}, header=header)['data'][0]
