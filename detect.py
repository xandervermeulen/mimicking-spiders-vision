import cv2
import numpy as np


def detect_ball(frame):
    current_rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    lower_yellow = np.array([219, 230, 6])
    upper_yellow = np.array([239, 250, 26])
    # Create a mask for the yellow color
    mask = cv2.inRange(current_rgb_frame, lower_yellow, upper_yellow)
    detected_ball = cv2.bitwise_and(current_rgb_frame, current_rgb_frame, mask=mask)
    # Find contours in the mask
    # contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Highlight the yellow ball by drawing contours on the frame
    # cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    return detected_ball
