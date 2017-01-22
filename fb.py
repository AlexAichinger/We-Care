import facebook
#import urllib
#import urlparse
#import subprocess
#import warnings


#warnings.filterwarnings('ignore', category=DeprecationWarning)

def getFriends(access_token):
  graph = facebook.GraphAPI(access_token)

  try:
    posts = graph.get_connections(id='me', connection_name='posts')
    print posts
  except facebook.GraphAPIError as e:
    print('Error occurred:', e.type, e.message)
