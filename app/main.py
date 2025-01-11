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

url = st.text_input("Enter the URL")
download_button = st.button("Download")

if download_button:
    if select_box == "Audio":
        audio_download(url)
        st.write("Audio is downloaded Successfully !")
    elif select_box == "Video":
        video_download(url)
        st.write("Video is downloaded Successfully !")