import datetime
import apis.twitchhelix

def uptime(text, args):
    targs = text.split()
    if len(targs) >= 1:
        username = targs[0]

    header = apis.twitchhelix.mkheader(args)
    
    response = apis.twitchhelix.get_stream(username, header)
    start_string = response['started_at']
    stime = datetime.datetime.strptime(start_string, '%Y-%m-%dT%H:%M:%SZ')
    deltat = datetime.datetime.utcnow()-stime
    timestr = int(deltat.total_seconds())
    message = str(timestr) + " seconds"
    return ['say ' + message]

