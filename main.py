from os import listdir
from os.path import isfile, join
import os

song_list = []
loading_dir = '/home/wv/Downloads/120_bpm/'
saving_dir = '/home/wv/Downloads/120_bpm/shorts/'

allfiles = [f for f in listdir(loading_dir) if isfile(join(loading_dir, f))]

if not os.path.exists(f'{saving_dir}'):
    try:
        os.mkdir(f'{saving_dir}')
    except Exception as e:
        print(e)

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
        os.system(f'ffmpeg -ss 00 -i {loading_dir}"{song}" -b:a 128k -t 60 {saving_dir}"{song}"')
except Exception as e:
    print(e)