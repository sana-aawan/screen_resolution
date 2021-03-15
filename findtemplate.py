import cv2
import numpy as np


def find_templates(obj, sensitivity):

    image = cv2.imread('images/vlc.PNG', cv2.IMREAD_COLOR)
    template = cv2.imread(obj, cv2.IMREAD_COLOR)

    h, w = template.shape[:2]

    print('h', h, 'w', w)

    method = cv2.TM_CCORR_NORMED

    threshold = 0.90

    res = cv2.matchTemplate(image, template, method)
    res_h, res_w = res.shape[:2]

    # fake out max_val for first run through loop
    max_val = 1
    centers = []
    while max_val > sensitivity:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        print(min_val, max_val, min_loc, max_loc)
        if max_val > sensitivity:
            centers.append( (max_loc[0] + w//2, max_loc[1] + h//2) )

            x1 = max(max_loc[0] - w//2, 0)
            y1 = max(max_loc[1] - h//2, 0)

            x2 = min(max_loc[0] + w//2, res_w)
            y2 = min(max_loc[1] + h//2, res_h)

            res[y1:y2, x1:x2] = 0

            image = cv2.rectangle(image,(max_loc[0],max_loc[1]), (max_loc[0]+w+1, max_loc[1]+h+1), (0,255,0) )

    print(centers)

    cv2.imwrite('images/output.png', image)

find_templates("media.PNG", 0.90)