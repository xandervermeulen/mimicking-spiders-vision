import cv2
import numpy as np


def calculate_middle_points_of_ball(cap, lower, upper):
    mean_x = []
    mean_y = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        mask = cv2.inRange(frame, lower, upper)
        detected_ball = cv2.bitwise_and(frame, frame, mask=mask)
        red_coordinates = (
            np.column_stack(np.where((detected_ball[:, :, 0] >= lower[0]) & (detected_ball[:, :, 0] <= upper[0]) &
                                     (detected_ball[:, :, 1] >= lower[1]) & (detected_ball[:, :, 1] <= upper[1]) &
                                     (detected_ball[:, :, 2] >= lower[2]) & (detected_ball[:, :, 2] <= upper[2]))))
        red_coordinates[:, 0] = frame.shape[0] - red_coordinates[:, 0]
        mean_x.append(np.median(red_coordinates[:, 1]))
        mean_y.append(np.median(red_coordinates[:, 0]))

    cap.release()
    cv2.destroyAllWindows()
    return mean_x, mean_y
