import cv2
import numpy as np

def apply_color_filter(image, filter_type):
    """Apply the specified color filter to the image."""
    filtered_image = image.copy()

    if filter_type == "original":
        return filtered_image
    
    elif filter_type == "red_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 0] = 0

    elif filter_type == "blue_tint":
        filtered_image[:, :, 1] = 0
        filtered_image[:, :, 2] = 0

    elif filter_type == "green_tint":
        filtered_image[:, :, 0] = 0
        filtered_image[:, :, 2] = 0

    elif filter_type == "increase_red":
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)

    elif filter_type == "decrease_blue":
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 0], 50)
    
    return filtered_image

image_path = 'exa.jpg'
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
else:
    fixed_width = 600
    fixed_height = 400
    image = cv2.resize(image, (fixed_width, fixed_height))

    filter_type = "original"

    # Map keys to filter types for cleaner code
    key_filter_map = {
        ord('r'): "red_tint",
        ord('b'): "blue_tint",
        ord('g'): "green_tint",
        ord('i'): "increase_red",
        ord('d'): "decrease_blue",
        ord('q'): "quit"
    }

    print("Press keys:")
    print("r - Red Tint")
    print("b - Blue Tint")
    print("g - Green Tint")
    print("i - Increase Red")
    print("d - Decrease Blue")
    print("q - Quit")

    while True:
        filtered_image = apply_color_filter(image, filter_type)
        cv2.imshow("Filtered Image", filtered_image)

        key = cv2.waitKey(0) & 0xFF

        if key in key_filter_map:
            if key_filter_map[key] == "quit":
                print("Exiting...")
                break
            filter_type = key_filter_map[key]
        else:
            print("Invalid key! Use r/b/g/i/d/q")

cv2.destroyAllWindows()