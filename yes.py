
import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img, "SUN", (100, 100), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0, 0, 255))
cv2.putText(img, "Mercury", (100, 180), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0, 0, 255))
cv2.putText(img, "VENUS", (180, 260), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0, 0, 255))
cv2.putText(img, "EARTH", (260, 160), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0, 0, 255))
cv2.putText(img, "MARS", (380, 260), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0, 0, 255))
cv2.putText(img, "JUPITER", (500, 160), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0, 0, 255))
cv2.putText(img, "SATURN", (800, 160), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0, 0, 255))
cv2.putText(img, "URANUS", (950, 160), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0, 0, 255))
cv2.putText(img, "NEPTUNE", (1100, 160), fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1, color = (0, 0, 255))

cv2.imshow("NO", img)
cv2.waitKey(5000)
