import cv2


def draw_contour_outline(img, cnts, color, thickness=1, alpha=0.2):
    img_aux = img.copy()
    for cnt in cnts:
        cv2.drawContours(img_aux, [cnt], 0, color, -1)
        cv2.drawContours(img, [cnt], 0, color, thickness)
    cv2.addWeighted(img_aux, alpha, img, 1 - alpha, 0, dst=img)


backSub = cv2.createBackgroundSubtractorKNN()
cap = cv2.VideoCapture(0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

while True:
    _, frame = cap.read()

    fgMask = backSub.apply(frame)
    mask = cv2.morphologyEx(fgMask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    _, contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    image_contour = frame.copy()
    for contour in contours:
        if cv2.contourArea(contour) > 5000:
            contour = cv2.convexHull(contour)
            epsilon = 0.01 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, epsilon, True)
            draw_contour_outline(image_contour, [approx], (0, 255, 0), 2)

    cv2.imshow('Nice Contour', image_contour)

    keyboard = cv2.waitKey(1)
    if keyboard == ord('q') or keyboard == 27:
        break

cv2.destroyAllWindows()
cap.release()
