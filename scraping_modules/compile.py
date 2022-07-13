import os
import config

intro = config.intro 
outro = config.outro 

def makeBorders():
    for i in range(config.dl_count):
        cmd = f'cd content; ffmpeg -i {i}-merged.mp4 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1" {i}-borders.mp4'
        os.system(cmd)
    os.system('cd content; rm *merged.mp4')

def compile(title, intro = None, outro = None, transition = None):
    makeBorders()

    # adding to VideoNames.txt
    video_names = open("content/VideoNames.txt", "a")

    # Writing video files to text in order, with intro/outro if specified
    if intro != None:
        video_names.write(f"file '{intro}'\n")
    for i in range(config.dl_count):
        video_names.write(f"file '{i}-borders.mp4'\n")
    if outro != None:
        video_names.write(f"file '{outro}'\n")

    video_names.close()
    # Merging videos in order of VideoNames.txt file listing with ffmpeg
    os.system(f'cd content; ffmpeg -f concat -safe 0 -i VideoNames.txt -c copy {title}.mp4')

    # Clearing text file
    video_names = open("content/VideoNames.txt", "w")
    video_names.write('')
    video_names.close()

    os.system(f'cd content; rm *borders.mp4') # Clearing seperate video files