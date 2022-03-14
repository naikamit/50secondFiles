import os
from os import listdir
from os.path import isfile, join

song_list = []
loading_dir = '/home/amit/Desktop/HPHI/'
saving_dir = '/home/amit/Desktop/HPHI/shorts/'

allfiles = [f for f in listdir(loading_dir) if isfile(join(loading_dir, f))]

for song in allfiles:
    if (song.endswith('mp3') and
            not song.endswith('bass.mp3') and
            not song.endswith('drums.mp3') and
            not song.endswith('other.mp3') and
            not song.endswith('piano.mp3') and
            not song.endswith('vocals.mp3') and
            not song.endswith('recombined.mp3')):
        song_list.append(song)

try:
    for song in song_list:
        os.system(f'ffmpeg -ss 00 -i {loading_dir}"{song}" -t 60 -c copy {saving_dir}"{song}"')
except Exception as e:
    print(e)