import os
import time
from pytubefix import Search
import re
from add_metadata import add_metadata

# bypass age
DOWNLOAD_PATH = 'C:/Users/Nico/OneDrive/Escritorio/music'

data_for_later = []


def search_download(artist, to_search, album, playlist, attempt=0):
    output_path = f"{os.path.join(DOWNLOAD_PATH, playlist)}"
    output_filename = f'{artist} - {to_search}.mp3'

    complete_path = os.path.join(output_path, output_filename)
    if os.path.isfile(complete_path):
        print("Skipping " + output_filename)
        return

    search_name = f'{artist} {to_search} lyrics'
    to_download = Search(search_name).videos[attempt]
    stream = to_download.streams.filter(only_audio=True).first()

    try:
        # output_filename = re.sub('[^A-Za-z0-9]+', ' ', stream.title) + '.mp3'  # Name of YouTube video
        output_filename = f'{artist} - {to_search}.mp3'
        stream.download(output_path=output_path, filename=output_filename)
        print(f'Downloading: {output_filename}')

        # complete_path = os.path.join(output_path, output_filename)
        # add_metadata(complete_path, to_search, artist, album)
        # data_for_later.append([complete_path, to_search, artist, album])
    except:
        if attempt < 5:
            print('\nCould not download:', to_search + ' ' + artist, 'trying again, attempt ', attempt)
            search_download(artist, to_search, album, playlist, attempt + 1)
        else:
            print('Could not download:', to_search, 'GAVE UP')

