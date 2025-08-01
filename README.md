# 🎵 YouTube to MP3 Downloader (Streamlit App)

This is a **personal-use web app** to convert YouTube videos to MP3 files for download.  
Built with **Python**, using **Streamlit**, **yt-dlp**, and **FFmpeg**.

---

## ✅ Features

- Paste a YouTube URL
- Downloads audio only
- Converts to `.mp3` with proper filename (`Title - Author.mp3`)
- Shows download button when ready
- Hosted for free on Streamlit Cloud

---

## 📁 Project Structure

urldownloader/
│
├── app.py # Streamlit app logic
├── utils.py # Helper to sanitize filenames
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🐛 Issues & Fixes

### 1. ❌ `HTTP Error 400: Bad Request`  
🔧 **Fix**: Switched from `pytube` to `yt-dlp`, which is more reliable and well-maintained.

---

### 2. ❌ `ffmpeg not found` / `ffprobe not found`  
🔧 **Fix**:  
- Streamlit Cloud doesn’t reliably expose system-installed FFmpeg.
- Solution: use `imageio-ffmpeg`, a Python package that bundles both `ffmpeg` & `ffprobe`.

```python
import imageio_ffmpeg

ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
...

'ffmpeg_location': ffmpeg_path,
'ffprobe_location': ffmpeg_path,  # Same path works
3. ❌ NameError: name 'subprocess' is not defined
🔧 Fix: Was caused by trying to debug FFmpeg availability. Removed after switching to imageio-ffmpeg.

🚀 Deployment Tips
Add imageio-ffmpeg to requirements.txt

No need for packages.txt on Streamlit Cloud

Keep everything Python-based for portability
⚠️ Disclaimer
This app is intended for personal use only. Do not use it to violate YouTube’s Terms of Service.
