import cv2 as cv
import numpy as np
 
# # #RESIZING
# proto = cv.imread('D:\\reunion\\school.jpg')
# print(proto.shape)

# # # w = int(proto.shape[1]//5)
# # # h = int(proto.shape[0]//5)
# # dim = int(min(proto.shape[1]//2, proto.shape[0]//2))


# def resizing(image, scale):
#     width = int(image.shape[1]*scale)
#     height = int(image.shape[0]*scale)
#     dimensions = (width, height)
#     return cv.resize(image, dimensions, interpolation=cv.INTER_AREA)

# # img = cv.resize(proto, (dim, dim), interpolation=cv.INTER_AREA)
# img = resizing(proto, 0.5)

# # #GRAYSCALE
# gray  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# # #SIMPLE THRESHOLDING
# threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
# cv.imshow('simple threshold', thresh)

# print(thresh.shape)
# cv.waitKey(0)
# # cv.waitKey(0)


def get_image_matrix(path, scale=20, thres_val=50):
    proto = cv.imread(path)
    dim = (proto.shape[1]//scale, proto.shape[0]//scale)
    img = cv.resize(proto, dim, interpolation=cv.INTER_AREA)
    gray  = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    threshold, thresh = cv.threshold(gray, thres_val, 255, cv.THRESH_BINARY)
    return thresh