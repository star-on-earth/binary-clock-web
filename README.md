# 🕐 Binary Clock Screensaver

A fullscreen binary clock screensaver built with Python + Tkinter. Displays hours, minutes, and seconds as glowing binary LED dots — inspired by the [WiFi Binary Clock](https://github.com/circuito-suman/BinaryInternetClock) hardware project by circuito-suman.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📸 Preview

Six columns of glowing dots represent each digit of HH:MM:SS in binary (4 bits per digit, MSB on top). Colors: **pink** for hours, **purple** for minutes, **cyan** for seconds.

```
H1  H2  |  M1  M2  |  S1  S2
●   ○      ○   ●      ○   ○     ← bit 3 (value 8)
○   ●      ●   ○      ○   ●     ← bit 2 (value 4)
●   ○      ●   ●      ○   ○     ← bit 1 (value 2)
○   ●      ○   ●      ●   ○     ← bit 0 (value 1)
```

---

## 📁 Project Structure

```
binary-clock-web/
├── index.html              # Web version (browser / GitHub Pages)
├── screensaver.py          # Tkinter screensaver (Windows .scr)
├── assets/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── clock.js
├── dist/
│   ├── screensaver.exe     # Packaged executable
│   └── screensaver.scr     # Windows screensaver file
└── README.md
```

---

## ✨ Features

- Fullscreen binary clock with neon glow aesthetics
- Live time from system clock (always NTP-accurate)
- Any keypress or mouse movement exits the screensaver
- Works as a standalone `.exe` or installed `.scr` on Windows
- Also deployable as a web page via GitHub Pages
- No external dependencies except Python standard library

---

## 🛠️ Requirements

- Python 3.10+
- PyInstaller (for building `.exe`)

```bash
pip install pyinstaller
```

> Tkinter is bundled with standard Python — no separate install needed.

---

## 🚀 Setup — Run Directly (Development)

```bash
git clone https://github.com/YOUR_USERNAME/binary-clock-web.git
cd binary-clock-web
python screensaver.py
```

Closes on any keypress or mouse movement.

---

## 📦 Build the `.exe`

```bash
# Clean any previous builds first
del screensaver.spec
rmdir /s /q build
rmdir /s /q dist

# Build
pyinstaller --onefile --windowed screensaver.py
```

Output: `dist\screensaver.exe`

---

## 🖥️ Install as Windows Screensaver (Step by Step)

### Step 1 — Rename `.exe` to `.scr`

```bash
copy dist\screensaver.exe dist\screensaver.scr
```

### Step 2 — Copy to System32 (requires Admin)

Open **Command Prompt as Administrator**:
- Search "cmd" in Start Menu
- Right-click → **Run as administrator**

Then run:

```bash
copy "C:\path\to\your\dist\screensaver.scr" "C:\Windows\System32\screensaver.scr"
```

Replace `C:\path\to\your\` with your actual project path. Example:

```bash
copy "C:\Users\KIIT0001\Documents\studymaterial\binary-clock-web\dist\screensaver.scr" "C:\Windows\System32\screensaver.scr"
```

### Step 3 — Set as Active Screensaver

1. Press `Win + I` → **Personalization**
2. Click **Lock Screen**
3. Scroll down → click **Screen Saver**
4. In the dropdown, select **"screensaver"**
5. Set your preferred wait time (e.g. 5 minutes)
6. Click **Apply** → **OK**

### Step 4 — Preview it

Click **Preview** in the Screen Saver Settings dialog — your binary clock should launch fullscreen immediately.

> **To exit:** Move the mouse or press any key.

---

## 🌐 Web Version (GitHub Pages)

The `index.html` version runs in any browser:

```bash
# Local dev
python -m http.server 8080
# Open http://localhost:8080
```

### Deploy to GitHub Pages

1. Push the repo to GitHub
2. Go to repo **Settings → Pages**
3. Source: **Deploy from branch → main → / (root)**
4. Save — live at `https://YOUR_USERNAME.github.io/binary-clock-web/`

---

## ⚙️ Configuration

Inside `screensaver.py`, you can tweak:

```python
IDLE_THRESHOLD = 60     # seconds before screensaver activates (if using daemon)
ROWS = 4                # bits per column (don't change unless you know binary clock layout)

COLORS = {
    'h': '#f72585',     # hours color   (pink)
    'm': '#b47aff',     # minutes color (purple)
    's': '#00f5d4',     # seconds color (cyan)
}
BG = '#0a0a0f'          # background color
OFF_COLOR = '#111118'   # unlit dot color
```

---

## 🔧 Troubleshooting

| Problem | Fix |
|---|---|
| Blank screen on launch | Ensure Python 3.10+ is installed |
| `.scr` not showing in screensaver list | Make sure you copied to `C:\Windows\System32\` as Admin |
| PyInstaller fails | Delete `build/`, `dist/`, `screensaver.spec` and retry |
| Mouse doesn't close it | Screensaver only detects movement after initial position is set — move again |
| Antivirus flags `.exe` | Normal for PyInstaller — add an exception in your AV settings |

---

## 🙏 Acknowledgements

Inspired by [circuito-suman/BinaryInternetClock](https://github.com/circuito-suman/BinaryInternetClock) — an ESP8266 hardware binary clock with NTP sync and LED matrix display.

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

*Made by Avrrodeep Banerjee*
