import cv2
import pyautogui
method = cv2.TM_SQDIFF_NORMED

# Read the images from the file
small_image = cv2.imread('images/video.PNG')
large_image = cv2.imread('images/vlc.PNG')

h, w = large_image.shape[:2]
sh, sw = small_image.shape[:2]
result = cv2.matchTemplate(small_image, large_image, method)
res_h, res_w = result.shape[:2]

# We want the minimum squared difference
mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx, MPy = mnLoc
print(MPx,  MPy)

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = small_image.shape[:2]
# print(trows,tcols)

# Step 3: Draw the rectangle on large_image
cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# Display the original image with the rectangle around the match.
cv2.imshow('output',large_image)
cv2.imwrite('result/result_video.png', large_image)

# The image is only displayed if we call this
cv2.waitKey(0)
