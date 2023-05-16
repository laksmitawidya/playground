import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

#  import twurl from https://www.py4e.com/code3/ and set the oauth / api key from twitter developers

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print('')
    account = input('Enter Twitter Account')
    if (len(account) < 1): break
    
    url = twurl.augment(TWITTER_URL, {'screen_name': account, 'count': '5'})
    print('Retrieving', url)
    
    # ignore SSL certificate error
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    request = urllib.request.urlopen("https://api.github.com/users/laksmitawidya", context=ctx)

    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read()
    print(data)
    
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js=json.loads(data)
    print(json.dump(js, indent=4))

    for u in js['users']:
        print(u['screen_name'])
        s=u['status']['text']
        print('  ', s[:50])