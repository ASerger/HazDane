from requests.models import Response
from config import client_id, client_secret, clientUserAgent, base_url # type: ignore
import string
import random
import requests
import json

_clientid = client_id
_clientsecret = client_secret
_baseOauthUrl = 'https://www.reddit.com/api/v1/access_token'
_type = 'code'
_redirectUri = f'{base_url}/api/authorize_callback'
_duration = 'temporary'
_scopeString = 'history'
_randomString = ''
_clientUserAgent = clientUserAgent

class redditauth:
    def get_new_client_bearer_token():
        headers = {'User-Agent':_clientUserAgent }
        token_req_payload = {'grant_type':'client_credentials'}
        token_response = requests.post(_baseOauthUrl, headers=headers, data=token_req_payload, verify=False, allow_redirects=False, auth=(_clientid, _clientsecret))
        tokens = json.loads(token_response.text)

        return tokens

    def enable_user_impersonation():
        _clientAuthUrl = f'https://www.reddit.com/api/v1/authorize?client_id={_clientid}&response_type={_type}&redirect_uri={_redirectUri}&duration={_duration}&scope={_scopeString}'
        _randomString = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        _clientAuthUrl += f'&state={_randomString}'
        print(_clientAuthUrl)

    def user_impersonation_redirect(state, code):
        headers = { 'User-Agent': _clientUserAgent, 'Content-Type': 'application/x-www-form-urlencoded' }
        payload = {'grant_type':'authorization_code', 'code': code, 'redirect_uri': _redirectUri}
        response = requests.post(_baseOauthUrl, headers=headers, data=payload, auth=(_clientid, _clientsecret))
        token = json.loads(response.text)
        print(token)
