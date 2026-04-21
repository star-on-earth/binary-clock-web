import webview
import sys
import os

def get_url():
    # If packaged by PyInstaller, load local files
    # Otherwise load from GitHub Pages
    if getattr(sys, 'frozen', False):
        base = sys._MEIPASS  # PyInstaller temp folder
        return f"file:///{base}/index.html"
    else:
        # For local dev, point to your local folder
        base = os.path.dirname(os.path.abspath(__file__))
        return f"file:///{base}/index.html"

webview.create_window(
    title='Binary Clock',
    url=get_url(),
    fullscreen=True,
    frameless=True,        # no title bar
    on_top=True,           # stays above taskbar
    background_color='#0a0a0f'
)

webview.start()