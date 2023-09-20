import requests

def request_status_code():
    r = requests.get('https://google.com')

    print('Connecting to url ' + r.url)
    print('Status Code: ' + str(r.status_code))

if __name__ == '__main__':
    request_status_code()