# youtube_downloader_360p.py
import yt_dlp
import os

URL = "https://youtu.be/"
FILENAME = "MyVideo_360p.mp4"

ydl_opts = {
    # Best practical format for ~360p mp4 in 2025+
    # Prefers H.264 mp4 video + m4a audio when possible
    'format': 'bestvideo[height<=360][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height<=360]+bestaudio/best[height<=360]',

    'outtmpl': FILENAME,
    'merge_output_format': 'mp4',

    # Download subtitles (manual + auto-generated)
    'writesubtitles': True,
    'writeautomaticsub': True,
    'subtitleslangs': ['en', 'fa'],       # English and Persian
    'subtitlesformat': 'srt',

    # Authentication / cookies handling
    'cookiefile': 'cookies.txt' if os.path.exists('cookies.txt') else None,
    'cookiesfrombrowser': ('chrome',) if not os.path.exists('cookies.txt') else None,

    # General settings
    'nooverwrites': False,
    'quiet': False,                 # Set to True for minimal output
    'noprogress': False,

    # Only uncomment if you have signature / throttling issues
    # 'extractor_args': {'youtube': {'player_skip': ['js', 'web']}},

    # Helps with unstable connections / rate limits
    'retries': 10,
    'fragment_retries': 10,
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([URL])
    print(f"Successfully downloaded → {FILENAME}")
    print("   (including English & Persian subtitles if available)")
except yt_dlp.utils.DownloadError as e:
    print("Download error (possibly age-restricted, geo-blocked or needs cookies):", e)
except Exception as e:
    print("Unexpected error:", e)
