import pyautogui
import math
import time
from PIL import Image

x, y = pyautogui.position()

# The coordinates of the first color (white)
first_color_x = 2623
first_color_y = 198

# The distance from the center of white to the center of the right color (or any other two neighbor colors)
color_center_distance = 60

# The distance from the center of a cell to the center of another cell
cell_distance = 17

"""
Calculate the mouse location of the target color
"""
def color_coord(x,y):
	return first_color_x + color_center_distance * x, first_color_y + color_center_distance*y

"""
Click on the target color
"""
def change_color(x,y):
	click_x, click_y = color_coord(x,y)
	pyautogui.click(click_x, click_y)

colors = ["#ffffff","#c4c4c4","#888888","#555555","#222222","#000000","#003638","#006600","#1b7400","#477050","#22b14c","#02be01","#51e119","#94e044","#98fb98","#fbff5b","#e5d900","#e6be0c","#e59500","#ff7000","#ff3904","#e50000","#ce2939","#ff416a","#9f0000","#6b0000","#ff755f","#a06a42","#633c1f","#99530d","#bb4f00","#ffc49f","#ffdfcc","#ffa7d1","#cf6ee4","#820080","#330077","#020763","#5100ff","#0000ea","#044bff","#005ba1","#6583cf"]

# Based on https://stackoverflow.com/questions/73687831/finding-the-closest-color-using-hex-codes
def compare(input_hex: str) -> str:    
    color_distance_list = []

    input_color = tuple(int(input_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

    for i in range (len(colors)):
        use_color = colors[i]
        my_color = tuple(int(use_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        get_distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(my_color, input_color)])) 
        color_distance_list.append(get_distance)

    sorted_color_distance_list = min(color_distance_list)
    closest_hex = color_distance_list.index(sorted_color_distance_list)

   
    return colors[closest_hex], closest_hex

# Based on https://stackoverflow.com/questions/65645044/get-hex-color-code-coordinate-of-the-pixel-in-a-image
img = Image.open('pic.png')
print("Drawing the image pic.png starting from top left at the mouse position..")
pixels = img.load() 
width, height = img.size

for y_img in range(height):      # this row
	for x_img in range(width):   # and this row was exchanged
		if len(pixels[x_img, y_img]) == 3:
			r, g, b = pixels[x_img, y_img]
		else:
			r, g, b, a = pixels[x_img, y_img]
			# Skip transparent cell
			if a == 0:
				continue
		hex = f"#{r:02x}{g:02x}{b:02x}"
		_, closest_color_idx = compare(hex)
		change_color(closest_color_idx % 2, closest_color_idx // 2)
		pyautogui.click(x + (x_img) * cell_distance, y + (y_img) * cell_distance)
		time.sleep(0.1)