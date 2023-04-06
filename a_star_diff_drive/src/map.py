import cv2
import numpy as np
import time

def map():
    map_canvas = np.zeros((200, 600, 3))
    cv2.rectangle(map_canvas, (0, 0), (600, 200), (255, 255, 255), 5)
    cv2.rectangle(map_canvas, (150, 75), (165, 200), (150, 100, 100), -1)
    cv2.rectangle(map_canvas, (150, 75), (165, 200), (255, 255, 255), 5)
    cv2.rectangle(map_canvas, (250, 0), (265, 125), (150, 100, 100), -1)
    cv2.rectangle(map_canvas, (250, 0), (265, 125), (255, 255, 255), 5)
    cv2.circle(map_canvas, (400, 110), 50, (150, 100, 100), -1)
    cv2.circle(map_canvas, (400, 110), 50, (255, 255, 255), 5)
    return map_canvas
