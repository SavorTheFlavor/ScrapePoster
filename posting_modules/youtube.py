import os

def postVideo(video):
    title = video.split('.mp4')[0]
    desc = ''

    os.system(f'mv content/{video} archive')