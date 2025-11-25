from withoutbg import WithoutBG
import tkinter as tk
from tkinter import filedialog
import os
import sys


def main():
	root = tk.Tk()
	root.withdraw()

	filetypes = [("Image files", "*.png *.jpg *.jpeg *.bmp *.webp"), ("All files", "*.*")]
	img_path = filedialog.askopenfilename(
		title="Select image to remove background",
		initialdir=os.getcwd(),
		filetypes=filetypes,
	)

	if not img_path:
		print("No file selected.")
		return 0

	clcoding = WithoutBG.opensource()
	try:
		result = clcoding.remove_background(img_path)
		base, _ = os.path.splitext(img_path)
		save_path = base + "_no_bg.png"
		result.save(save_path)
		print(f"Saved: {save_path}")
		return 0
	except Exception as e:
		print("Error removing background:", e)
		return 1


if __name__ == "__main__":
	sys.exit(main())
