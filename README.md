# YouTube 360p Downloader (yt-dlp)

A simple Python script to download YouTube videos in **360p resolution** (or the best available video ≤360p) with the **best audio quality**, automatically merged into an MP4 file. It also downloads manual and auto-generated subtitles in English and Persian (Farsi).

Powered by the excellent **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** — a feature-rich fork of youtube-dl.

## Features

- Downloads the best video stream with height ≤ 360p
- Pairs it with the highest-quality audio available
- Merges video + audio into a single MP4 file (using ffmpeg)
- Automatically downloads:
  - Manual subtitles (if available)
  - Auto-generated subtitles
- Supports English (`en`) and Persian/Farsi (`fa`) subtitles
- Clean output filename based on video title

## Requirements

- Python 3.7 or higher
- **ffmpeg** (must be installed and available in your PATH)
- `yt-dlp` Python package

## Installation

1. Clone or download this repository
2. Install the required package:

```bash
pip install yt-dlp

Make sure ffmpeg is installed on your system:Windows: Download from https://ffmpeg.org/download.html or use a package manager like Chocolatey (choco install ffmpeg)
macOS: brew install ffmpeg
Linux: sudo apt install ffmpeg (Debian/Ubuntu) or use your package manager

UsageOpen youtube_downloader_360p.py
Replace the URL line with your YouTube video link:

python

URL = "https://youtu.be/your-video-id-here"

Run the script:

bash

python youtube_downloader_360p.py

The video (with subtitles) will be saved in the same folder with the original YouTube title.

Optional: Uncomment Cookies (for age-restricted/private videos)If you need to download age-restricted or private videos that require login:python

'cookiesfrombrowser': ('chrome',),  # or 'firefox', 'edge', 'safari', etc.

Make sure you're logged into YouTube in that browser.NotesIf 360p is not available, yt-dlp will download the closest lower resolution.
Subtitles are saved as .vtt files alongside the video.
The script merges everything into a single .mp4 file for easy playback.

Legal NoteOnly download videos that you have permission to download. Respect YouTube's Terms of Service and copyright laws.LicenseMIT License — feel free to use, modify, and distribute.

