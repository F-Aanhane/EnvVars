from mock_api import credential_store
import random
import string
import requests
import base64

_AUTHENTICATED = False


def _encode_creds(*credentials: str):
    encoded_credentials = []
    for cred in credentials:
        cred_bytes = cred.encode('ascii')
        encoded_bytes = base64.b64encode(cred_bytes)
        encoded_cred = encoded_bytes.decode('ascii')
        encoded_credentials.append(encoded_cred)
    return encoded_credentials


def _decode_creds(*encoded_credentials: str):
    credentials = []
    for encoded_cred in encoded_credentials:
        encoded_bytes = encoded_cred.encode('ascii')
        cred_bytes = base64.b64decode(encoded_bytes)
        cred = cred_bytes.decode('ascii')
        credentials.append(cred)
    return credentials


def _pwd_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def authenticate(credentials: list):
    encoded_username = _encode_creds(credentials[0])
    try:
        encoded_pwd = credential_store.pairs.get(encoded_username[0])
        pwd = _decode_creds(encoded_pwd).pop()
        if credentials[1] == pwd:
            global _AUTHENTICATED
            _AUTHENTICATED = True
            return print('Authentication succeeded')
        else:
            return print('Authentication failed')
    except:
        raise ValueError('Wrong username')


def request_data():
    if _AUTHENTICATED:
        s = requests.Session()
        r = s.get('https://httpbin.org/base64/SGVsbG8gd29ybGQsIHRoZSBkYXRhIHRvIGJlIGZldGNoZWQgaXM6IDQy')
        print(r.text)

    else:
        raise ValueError('not authenticated. Couldn\'t receive data')
