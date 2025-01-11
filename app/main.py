import streamlit as st
from download import audio_download, video_download

st.set_page_config(
    page_title="Youtube Downloader",
    page_icon="🎞️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Youtube Downloader")

st.sidebar.header("Format Selection")

select_box = st.sidebar.radio(
    "Select the format",
    ("Audio", "Video")
)

num_urls = st.sidebar.number_input(
    "Enter the number of YouTube URLs:",
    min_value=1,
    max_value=100,
    step=1,
    value=1
)

urls = []

for i in range(num_urls):
    url = st.text_input(f"Enter URL {i + 1}:", key=f"url_{i}")
    if url.strip():
        urls.append(url.strip())

download_button = st.button("Download")

if download_button:
    if select_box == "Audio":
        audio_download(urls)
        st.write("Audio(s) is downloaded Successfully !")
    elif select_box == "Video":
        video_download(urls)
        st.write("Video(s) is downloaded Successfully !")