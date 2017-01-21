import facebook
import requests
import warnings

warnings.filterwarnings('ignore', category=DeprecationWarning)

access_token = 'EAACEdEose0cBANs3EST24SLdSvPYZALACFrcS1ZB61Wa3sfzNZCiYn9viOaFmcqCZAol6AQZBnsdAHswpnPI5iEoZA4T6E01Xc49QjAhZCB6Xgo8bZBuxMGN4XX05P9cjXuJKzHlq8lemCBJikIJKjVfZAL5axMuCpUgSSDOExpjtSwZDZD'
user = '502258806607064'

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts')

def get_data(post):
    print(post['picture'])
    print(post['message'])

while True:
    try:
        [get_data(post) for post in posts['data']]
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        break
