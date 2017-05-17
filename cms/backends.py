from embed_video.backends import VideoBackend
from django.conf import settings
import re

# htpps://arte7cine.s3.amazonaws.com/2
class CustomBackend(VideoBackend):
    re_detect = re.compile(r'http://arte7\.net/[0-9]+', re.I)
    re_code = re.compile(r'http://arte7\.net/(?P<code>[0-9]+)', re.I)

    allow_https = False
    pattern_url = '{protocol}://arte7cine.s3.amazonaws.com/media/videos/files/{code}.mp4'
    pattern_thumbnail_url = '{protocol}://arte7cine.s3.amazonaws.com/media/videos/thumbnails/{code}.png'

    template_name = 'embed_video/custombackend_embed_code.html'  # added in v0.9
