#Write a script that uses a web API to create a social media post.
#There is a tweet bot API listening at http://127.0.0.1:8082, GET / returns basic info about the API.
#POST / with x-api-key:tweetbotkeyv1 and data with user tweetbotuser and a status-update of alientest.

import urllib.parse
import urllib.request

url = "http://127.0.0.1:8082/"
header={"x-api-key" : 'tweetbotkeyv1'}
post_param = urllib.parse.urlencode({
                    'user' : 'tweetbotuser',
           'status-update' : 'alientest'
          }).encode('UTF-8')

req = urllib.request.Request(url, post_param, header)
response = urllib.request.urlopen(req)

print(response.read())
