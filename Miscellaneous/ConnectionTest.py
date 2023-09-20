import urllib.request as request

def connect(host='http://google.com'):
    try:
        request.urlopen(host)
        return True
    except:
        return False

print( "Internet Connection was detected." if connect() else "Internet Connection was not detected." )