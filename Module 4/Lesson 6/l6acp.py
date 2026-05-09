import cv2
import numpy as np
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.GREEN + Style.BRIGHT + "🎥 Starting Hand Gesture Tracker...")
print(Fore.YELLOW + "Press 'q' to quit the program.\n")

cap = cv2.VideoCapture(0)

shape_x = 300
shape_y = 200
shape_size = 60
shape_color = (0, 255, 0)

prev_x = 0
prev_y = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print(Fore.RED + "❌ Failed to access webcam.")
        break

    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=2)
    mask = cv2.GaussianBlur(mask, (5, 5), 100)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        contour = max(contours, key=cv2.contourArea)

        if cv2.contourArea(contour) > 5000:
            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cx = x + w // 2
            cy = y + h // 2

            cv2.circle(frame, (cx, cy), 8, (0, 0, 255), -1)

            if cx - prev_x > 20:
                direction = "Moving Right ➡"
                shape_x += 10
            elif prev_x - cx > 20:
                direction = "Moving Left ⬅"
                shape_x -= 10
            elif cy - prev_y > 20:
                direction = "Moving Down ⬇"
                shape_y += 10
            elif prev_y - cy > 20:
                direction = "Moving Up ⬆"
                shape_y -= 10
            else:
                direction = "Stable ✋"
            
            prev_x = cx
            prev_y = cy

            aspect_ratio = h / w

            if aspect_ratio > 1.5:
                gesture = "Open Hand ✋"
                shape_color = (0, 255, 0)
            else:
                gesture = "Thumbs Up 👍"
                shape_color = (0, 0, 255)

            shape_size = max(30, min(150, w))

            cv2.rectangle(
                frame,
                (shape_x, shape_y),
                (shape_x + shape_size, shape_y + shape_size),
                shape_color,
                -1
            )

            cv2.putText(frame, direction, (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (255, 255, 255), 2)

            cv2.putText(frame, gesture, (20, 80), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 255), 2)

    else:
        cv2.putText(frame, "No Hand Detected ❌", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Hand Gesture Tracker", frame)
    cv2.imshow("Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(Fore.GREEN + "\n✅ Program closed successfully.")
