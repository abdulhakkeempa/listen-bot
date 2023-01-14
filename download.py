from pytube import YouTube
import os
from pathlib import Path


def youtube2mp3 (url,outdir):
    yt = YouTube(url)
    video = yt.streams.filter(abr='160kbps').last()

    out_file = video.download(output_path=outdir)
    base, ext = os.path.splitext(out_file)
    new_file = Path(f'{base}.mp3')
    print(new_file)
    os.rename(out_file, new_file)
    if new_file.exists():
        return (new_file)
    else:
        return (f'ERROR: {yt.title}could not be downloaded!')