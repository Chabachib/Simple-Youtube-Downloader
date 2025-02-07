from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path

def audio_download(urls):
    download_path = Path.home() / "Downloads"
    for url in urls:
        yt = YouTube(url, on_progress_callback=on_progress)
        ys = yt.streams.get_audio_only()
        ys.download(output_path=download_path)

def video_download(urls):
    download_path = Path.home() / "Downloads"
    for url in urls:
        yt = YouTube(url, on_progress_callback=on_progress)
        ys = yt.streams.get_highest_resolution()
        ys.download(output_path=download_path)