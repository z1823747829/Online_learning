from hashlib import md5

from django.conf import settings


def md5_salt(data):
    return md5((settings.SECRET_KEY + data).encode('utf-8')).hexdigest()
