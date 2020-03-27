# Motion-Detection-Advanced-Filtering-and-Contours
Active motion detection, great noise filtering and advanced contours application.

I've used the KNN background subtraction (works amazing) and then applied a filtering process to the mask. The filtering is an Open operation followed by a Close one both with a 3x3 rectangular filter, to eliminate unwanted external noise. Then get the countours with the highest hierarchy (RETR_EXTERNAL), simplify them (CHAIN_APPROX_SIMPLE) and finally delete more contour noise (convexHull).

![](demo.gif)


