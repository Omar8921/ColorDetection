# 🎨 Color Detector with OpenCV

This is a simple Python program that lets you click anywhere on an image and shows you the nearest color name based on RGB values. It's useful for identifying colors from pictures using a predefined color dataset.

---

## 📌 Features

- Detects the RGB color at the position of a mouse double-click.
- Matches it to the closest color name using Euclidean distance.
- Displays the name and RGB values in a rectangle overlay.
- Automatically switches text color (black or white) based on background brightness for readability.

---

## 📂 Files

- `color_detector.py`: Main script.
- `colors.csv`: CSV file containing color names and RGB values.
- `example.jpg`: (Optional) An image file for testing.

---

## 📦 Requirements

- Python 3.x
- OpenCV
- Pandas

Install dependencies using pip:

```bash
pip install opencv-python pandas
```

---

## ▶️ How to Run

Run the script from the terminal or command prompt:

```bash
python color_detector.py --image your_image.jpg
```

Example:

```bash
python color_detector.py --image example.jpg
```

---

## 🧾 Format of `colors.csv`

No headers required. The file must follow this format:

```
color,color_name,hex,r,g,b
```

Example rows:

```
red,Red,#FF0000,255,0,0
green,Green,#00FF00,0,255,0
blue,Blue,#0000FF,0,0,255
```

Make sure the file is named `colors.csv` and is in the same directory as the script.

---

## 🖱️ How to Use

- Run the program.
- A window will open showing the image.
- Double-click anywhere on the image.
- A rectangle will show the color name and RGB values.
- Press `Esc` to exit.

---

## 📌 Example Output

When you double-click on a blue pixel:

```
Color Name: Blue    R: 0   G: 0   B: 255
```
