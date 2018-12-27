import os

from django.conf import settings


def save_upload_file(user, avatar):
    filename = 'avatar-%s' % user.id
    filepath = os.path.join(settings.BASE_DIR, 'images',filename)
    with open(filepath, 'wb') as fp:
        for chunk in avatar.chunks():
            fp.write(chunk)
    return filepath, filename


def upload_avatar_to_qiniu(user, filepath, filename):
    pass