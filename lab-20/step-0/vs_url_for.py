from flask import url_for

URL_PREFIX = '/usr/289'
#URL_PREFIX = ''

def vs_url_for(view):
    url = url_for(view)
    url = URL_PREFIX + url
    return url


