import apis.twitchhelix

def uptime(username):
    response = twitchhelix.get_stream(username)
    start_string = response['started_at']
    stime = datetime.datetime.strptime(start_string, '%Y-%m-%dT%H:%M%SZ')
    deltat = datetime.datetime.utcnow()-stime


