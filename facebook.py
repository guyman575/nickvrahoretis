from facepy import GraphAPI
import json
import urllib
import subprocess
import warnings

warnings.filterwarnings('ignore', category=DeprecationWarning)

FACEBOOK_APP_ID     = ''
FACEBOOK_APP_SECRET = ''
FACEBOOK_PROFILE_ID = ''

oauth_args = dict(client_id     = FACEBOOK_APP_ID,
                  client_secret = FACEBOOK_APP_SECRET,
                  grant_type    = 'client_credentials')
oauth_curl_cmd = ['curl',
                  'https://graph.facebook.com/oauth/access_token?' + urllib.parse.urlencode(oauth_args)]
oauth_response = subprocess.Popen(oauth_curl_cmd,
                                  stdout = subprocess.PIPE,
                                  stderr = subprocess.PIPE).communicate()[0]



APP_TOKEN = json.loads(oauth_response)['access_token']
APP_TOKEN = ''
graph = GraphAPI(APP_TOKEN)

gID = '446923602181882'


groupData = graph.get(gID + "/feed", page=True, retry=3, limit=10)

for data in groupData:
    # json_data=json.dumps(data, indent = 4)
    # decoded_response = json_data.decode("UTF-8")
    # data = json.loads(decoded_response)
    print(data)
