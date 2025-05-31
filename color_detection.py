def get_color(event, x, y, flags, params):
    global b, g, r, clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True
        b,g,r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)
 
def find_nearest_color(r, g, b):
    minn = float('inf')
    color = None
    for i in range(df.shape[0]):
        d = math.sqrt((r - df.loc[i, 'r']) ** 2 + (g - df.loc[i, 'g']) ** 2 + (b - df.loc[i, 'b']) ** 2)
        if d < minn:
            minn = d
            color = df.loc[i, 'color_name']
 
    return color
 
import argparse
import cv2
import math
import pandas as pd
 
names = ['color', 'color_name', 'hex', 'r', 'g', 'b']
df = pd.read_csv('colors.csv', header=None, names=names)
 
 
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
image_path = args['image']
 
b = g = r = 0
clicked = False
 
img = cv2.imread(image_path, 1)
cv2.imshow('Window', img)
cv2.setMouseCallback('Window', get_color)
 
while cv2.waitKey(1) != 27:
    cv2.imshow('Window', img)
    if clicked:
        nearest_color = find_nearest_color(r, g, b)
 
        cv2.rectangle(img, (25,25), (550, 100), (b,g,r), -1)
        cv2.putText(img, f'{nearest_color} R: {r} G: {g} B:{b}', (50,75), 2, 0.8, (255,255,255), 2)
 
        if b + g + r > 600:
            cv2.putText(img, f'{nearest_color} R: {r} G: {g} B:{b}', (50,75), 2, 0.8, (0,0,0), 2)
 
        clicked = False
 
cv2.destroyAllWindows()