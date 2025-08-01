# app.py
import streamlit as st
import tempfile
import os
import imageio_ffmpeg  # ✅ New import
from utils import clean_filename
from yt_dlp import YoutubeDL

# Debug info (optional)

ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
ffmpeg_dir = os.path.dirname(ffmpeg_path)

st.write("Using bundled FFmpeg from:", ffmpeg_path)


st.set_page_config(page_title="YouTube to MP3 Downloader")
st.title("🎵 YouTube to MP3 Downloader")

url = st.text_input("Enter YouTube URL:")
start_conversion = st.button("Convert")

if start_conversion and url:
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            st.info("📥 Downloading and converting...")

            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(tmpdir, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'ffmpeg_location': ffmpeg_path,
                'ffprobe_location': ffmpeg_path,
                'quiet': True,
                'no_warnings': True,
                'headers': {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                'AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Chrome/115.0.0.0 Safari/537.36'
                },
            }


            with YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                title = info_dict.get('title', 'audio')
                author = info_dict.get('uploader', 'youtube')

            mp3_filename = clean_filename(title, author)
            mp3_path = os.path.join(tmpdir, title + ".mp3")

            st.success("✅ Conversion complete!")
            with open(mp3_path, 'rb') as f:
                st.download_button(
                    label="Download MP3",
                    data=f,
                    file_name=mp3_filename,
                    mime="audio/mpeg"
                )

    except Exception as e:
        st.error(f"Something went wrong: {e}")
