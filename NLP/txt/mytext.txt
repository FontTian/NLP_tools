#!/usr/bin/env python
#4-1.py
import cv2


fn="test1.jpg"

if __name__ == '__main__':
    print 'http://blog.csdn.net/myhaspl'
    print 'myhaspl@qq.com'
    print
    print 'loading %s ...' % fn
    img = cv2.imread(fn)
    cv2.imshow('preview', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
