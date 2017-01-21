import facebook
import urllib
import urlparse
import subprocess
import warnings

warnings.filterwarnings('ignore', category=DeprecationWarning)

app_id = 769684356512385
app_secret = 'bfafc3ab14067170a74e3977643584f6'
profile_id = '502258806607064'
profile_friend_name = 'XXXXXX'
oauth_access_token = 'EAACEdEose0cBANs3EST24SLdSvPYZALACFrcS1ZB61Wa3sfzNZCiYn9viOaFmcqCZAol6AQZBnsdAHswpnPI5iEoZA4T6E01Xc49QjAhZCB6Xgo8bZBuxMGN4XX05P9cjXuJKzHlq8lemCBJikIJKjVfZAL5axMuCpUgSSDOExpjtSwZDZD'
print(oauth_access_token)
facebook_graph = facebook.GraphAPI(oauth_access_token)

try:
    friends = facebook_graph.get_connections(id = 'me', connection_name = 'friends')
    print friends
except facebook.GraphAPIError as e:
    print 'Error occurred:', e.type, e.message
