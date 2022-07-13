import requests
import urllib.request
import os

videos = []

# Gets the page contents through a json url, and appends the videos array 
# with mp4 and mp3 url pairs to be downloaded
def getPage(url):
    resp = requests.get(url, headers={'user-agent': 'Mozilla/5.0'})
    
    for post in resp.json()['data']['children']:
        if post['data']['media'] != None:
            if 'reddit_video' in post['data']['media'] != None:
                raw = (post['data']['media']['reddit_video']['fallback_url'])
                video = raw.split('.mp4')[0] + '.mp4'
                audio = video.split('_')[0] + '_audio.mp4'

                videos.append([video, audio])


# Downloads the seperate mp4 and mp3 files from the given links
# within the videos array
def download(dl_count):
    count = 0
    print('Downloading...')
    print(f'{count}/{dl_count}')
    for i in videos:
        urllib.request.urlretrieve(i[0], 'content/' + str(count)+'-raw.mp4')
        try:
            urllib.request.urlretrieve(i[1], 'content/' + str(count)+'-raw.mp3')
        except:
            continue

        count +=1 
        print(f'{count}/{dl_count}')
        if count == dl_count:
            break


# Opens the content folder, and combines mp3 and mp4 files
# with the same name into one video each, then removes raw files
def combine(dl_count):
    for i in range(dl_count):
        try:
            cmd = f'cd content; ffmpeg -y -i {i}-raw.mp4 -i {i}-raw.mp3 -c:v copy -c:a aac {i}-merged.mp4'
        except: # Exeption upon no mp3 file being present
            cmd = f'cd content; mv {i}-raw.mp4 {i}-merged.mp4'
        os.system(cmd)
    os.system('cd content; rm *-raw.mp3 *-raw.mp4')


def parse(url, dl_count):
    getPage(url)
    download(dl_count)
    combine(dl_count)