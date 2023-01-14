from pytube import YouTube
import os
import time
from pathlib import Path


def youtube2mp3 (url,outdir):
    start_time = time.time()
    yt = YouTube(url)
    video = yt.streams.filter(abr='160kbps').last()
    print("download started")
    out_file = video.download(output_path=outdir)
    base, ext = os.path.splitext(out_file)
    new_file = Path(f'{base}.mp3')
    print(new_file)
    os.rename(out_file, new_file)
    log = open("logs/log.txt", "a")
    log.write(str(yt.length)+":")
    log.write(str(time.time() - start_time))
    log.close()

    if new_file.exists():
        print("download ended")
        return (new_file)
    else:
        return (f'ERROR: {yt.title}could not be downloaded!')