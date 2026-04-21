import tkinter as tk
import time
import math

COLS = [
    {'type': 'h', 'div': 10}, {'type': 'h', 'div': 1},
    {'type': 'm', 'div': 10}, {'type': 'm', 'div': 1},
    {'type': 's', 'div': 10}, {'type': 's', 'div': 1},
]
COLORS = {
    'h': '#f72585',
    'm': '#b47aff',
    's': '#00f5d4',
}
OFF_COLOR = '#111118'
BG = '#0a0a0f'
ROWS = 4
GAP_COLS = [2, 4]  # separators before these column indices

def get_digits():
    t = time.localtime()
    h, m, s = t.tm_hour, t.tm_min, t.tm_sec
    return [h//10, h%10, m//10, m%10, s//10, s%10]

class BinaryClock:
    def __init__(self, root):
        self.root = root
        root.attributes('-fullscreen', True)
        root.attributes('-topmost', True)
        root.configure(bg=BG)
        root.title('Binary Clock')

        # Exit on any input
        root.bind('<KeyPress>', lambda e: root.destroy())
        root.bind('<ButtonPress>', lambda e: root.destroy())
        # root.bind('<Motion>', self.on_motion)
        self.last_mouse = None

        self.canvas = tk.Canvas(root, bg=BG, highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)

        self.dots = {}   # (col, row) -> canvas oval id
        self.glows = {}  # (col, row) -> canvas oval id (glow layer)
        self.time_text_id = None

        self.root.after(100, self.setup)
        self.root.after(200, self.tick)

    def on_motion(self, e):
        pos = (e.x, e.y)
        if self.last_mouse and self.last_mouse != pos:
            self.root.destroy()
        self.last_mouse = pos

    def setup(self):
        # w = self.canvas.winfo_width()
        # h = self.canvas.winfo_height()
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()


        r = min(w, h) // 22          # dot radius
        col_gap = r * 3
        sep_gap = r * 2
        row_gap = r * 3

        n_separators = len(GAP_COLS)
        total_w = 6 * col_gap + n_separators * sep_gap
        total_h = ROWS * row_gap

        start_x = (w - total_w) // 2 + r
        start_y = (h - total_h) // 2 + r

        self.r = r
        self.positions = {}  # (col, row) -> (cx, cy)

        x = start_x
        for ci in range(6):
            if ci in GAP_COLS:
                x += sep_gap
            for ri in range(ROWS):
                cy = start_y + ri * row_gap
                self.positions[(ci, ri)] = (x, cy)
            x += col_gap

        # Draw all dots (off state first)
        for (ci, ri), (cx, cy) in self.positions.items():
            col_type = COLS[ci]['type']
            color = COLORS[col_type]
            # glow (larger, transparent-ish — simulated with a bigger oval)
            g = self.canvas.create_oval(
                cx - r, cy - r, cx + r, cy + r,
                fill=BG, outline='', state='hidden'
            )
            d = self.canvas.create_oval(
                cx - r, cy - r, cx + r, cy + r,
                fill=OFF_COLOR, outline='#1a1a2e', width=1
            )
            self.dots[(ci, ri)] = (d, g, color)

        # Time text at bottom
        font_size = max(12, r)
        self.time_text_id = self.canvas.create_text(
            w // 2, start_y + ROWS * row_gap + r * 2,
            text='', fill='#333344',
            font=('Courier New', font_size, 'bold')
        )

    def tick(self):
        digits = get_digits()
        t = time.localtime()
        timestr = f"{t.tm_hour:02d}:{t.tm_min:02d}:{t.tm_sec:02d}"

        for ci, digit in enumerate(digits):
            for ri in range(ROWS):
                bit_pos = ROWS - 1 - ri
                on = bool(digit & (1 << bit_pos))
                d, g, color = self.dots[(ci, ri)]
                if on:
                    self.canvas.itemconfig(d, fill=color, outline=color)
                    self.canvas.itemconfig(g, fill=color, state='normal')
                    self.canvas.tag_lower(g, d)
                else:
                    self.canvas.itemconfig(d, fill=OFF_COLOR, outline='#1a1a2e')
                    self.canvas.itemconfig(g, state='hidden')

        if self.time_text_id:
            self.canvas.itemconfig(self.time_text_id, text=timestr)

        self.root.after(1000, self.tick)

if __name__ == '__main__':
    root = tk.Tk()
    app = BinaryClock(root)
    root.mainloop()