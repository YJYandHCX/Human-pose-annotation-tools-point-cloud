import pickle
import numpy as np
import INIT
import cv2

def init():
    t = INIT.init()
    return t
def draw(frame):
    x = frame[:,0]
    y = frame[:,1]
    z = frame[:,2]
    l = frame[:,9]
    num_p = len(x)

    #width = abs(x.max()-x.min())
    #height = abs(y.max()-y.min())

    im = np.zeros([401,401,3],dtype=np.int)
    im[:,:,:] = [255,255,255]

    for i in range(num_p):
        p_x = int(x[i]*400)
        p_y = int(y[i]*400)

        if l[i] == 1:
            im[p_y,p_x,:] = [255,0,0]
        if l[i] == 2:
            im[p_y,p_x,:] = [0,0,255]
        if l[i] == 0:
            im[p_y,p_x,:] = [0,255,0]
        if l[i] == 3:
            im[p_y,p_x,:] = [46,139,87]
        if l[i] == 4:
            im[p_y,p_x,:] = [238,220,130]
        if l[i] == 5:
            im[p_y,p_x,:] = [139,115,85]
    cv2.imwrite('./zheng.jpg',im)
def find_z(px,py,frame):
    x = frame[:,0]
    y = frame[:,1]
    z = frame[:,2]
    dx = x*x
    dy = y*y
    dx = abs(dx-px*px)
    dy = abs(dy-py*py)
    d = dx+dy
    return z[np.argmin(d)]
def draw_zuo(joints,frame):
    x = frame[:,0]
    y = frame[:,1]
    z = frame[:,2]
    l = frame[:,9]
    num_p = len(x)
    im = np.zeros([310, 310, 3], dtype=np.int)
    im[:, :, :] = [255, 255, 255]

    for i in range(num_p):
        p_z = int(z[i]*300)
        p_y = int(y[i]*300)
        if l[i] == 1:
            im[p_y,p_z,:] = [255,0,0]
        if l[i] == 2:
            im[p_y,p_z,:] = [0,0,255]
        if l[i] == 0:
            im[p_y,p_z,:] = [0,255,0]
        if l[i] == 3:
            im[p_y,p_z,:] = [46,139,87]
        if l[i] == 4:
            im[p_y,p_z,:] = [238,220,130]
        if l[i] == 5:
            im[p_y,p_z,:] = [139,115,85]

    im = cv2.circle(im, (int(joints[0, 2] * 300), int(joints[0, 1] * 300)), 5, (0, 0, 0), -1)
    im = cv2.circle(im, (int(joints[1, 2] * 300), int(joints[1, 1] * 300)), 5, (0, 0, 0), -1)

    im = cv2.circle(im, (int(joints[2, 2] * 300), int(joints[2, 1] * 300)), 5, (255, 255, 0), -1)
    im = cv2.circle(im, (int(joints[3, 2] * 300), int(joints[3, 1] * 300)), 5, (255, 255, 0), -1)
    im = cv2.circle(im, (int(joints[4, 2] * 300), int(joints[4, 1] * 300)), 5, (255, 255, 0), -1)

    im = cv2.circle(im, (int(joints[5, 2] * 300), int(joints[5, 1] * 300)), 5, (255, 0, 255), -1)
    im = cv2.circle(im, (int(joints[6, 2] * 300), int(joints[6, 1] * 300)), 5, (255, 0, 255), -1)
    im = cv2.circle(im, (int(joints[7, 2] * 300), int(joints[7, 1] * 300)), 5, (255, 0, 255), -1)
    #for o in joints:
    #    im = cv2.circle(im, (int(o[2]*300), int(o[1]*300)), 5, (0, 0, 0), -1)
    cv2.imwrite('./zuo.jpg',im)
def draw_gu(joints):
    im = np.zeros([310, 310, 3], dtype=np.int)
    im[:, :, :] = [255, 255, 255]
    im = cv2.circle(im, (int(joints[0, 2] * 300), int(joints[0, 1] * 300)), 5, (0, 0, 0), -1)
    im = cv2.circle(im, (int(joints[1, 2] * 300), int(joints[2, 1] * 300)), 5, (0, 0, 0), -1)
    cv2.line(im, (int(joints[0, 2] * 300), int(joints[0, 1] * 300)), (int(joints[1, 2] * 300), int(joints[1, 1] * 300)), (140,78,23),5)

    im = cv2.circle(im, (int(joints[2, 2] * 300), int(joints[2, 1] * 300)), 5, (255, 255, 0), -1)
    cv2.line(im, (int(joints[1, 2] * 300), int(joints[1, 1] * 300)),(int(joints[2, 2] * 300), int(joints[2, 1] * 300)),
             (45, 178, 3), 5)

    im = cv2.circle(im, (int(joints[3, 2] * 300), int(joints[3, 1] * 300)), 5, (255, 255, 0), -1)
    cv2.line(im, (int(joints[2, 2] * 300), int(joints[2, 1] * 300)),(int(joints[3, 2] * 300), int(joints[3, 1] * 300)),
             (45, 178, 3), 5)
    im = cv2.circle(im, (int(joints[4, 2] * 300), int(joints[4, 1] * 300)), 5, (255, 255, 0), -1)
    cv2.line(im, (int(joints[3, 2] * 300), int(joints[3, 1] * 300)),(int(joints[4, 2] * 300), int(joints[4, 1] * 300)),
             (45, 178, 3), 5)

    im = cv2.circle(im, (int(joints[5, 2] * 300), int(joints[5, 1] * 300)), 5, (255, 0, 255), -1)
    cv2.line(im, (int(joints[1,2] * 300), int(joints[1, 1] * 300)),(int(joints[5, 2] * 300), int(joints[5, 1] * 300)),
             (145, 90, 178 ), 5)
    im = cv2.circle(im, (int(joints[6, 2] * 300), int(joints[6, 1] * 300)), 5, (255, 0, 255), -1)
    cv2.line(im, (int(joints[5, 2] * 300), int(joints[5, 1] * 300)),(int(joints[6, 2] * 300), int(joints[6, 1] * 300)),
             (145, 90, 178), 5)
    im = cv2.circle(im, (int(joints[7, 2] * 300), int(joints[7, 1] * 300)), 5, (255, 0, 255), -1)
    cv2.line(im, (int(joints[6, 2] * 300), int(joints[6, 1] * 300)),(int(joints[7, 2] * 300), int(joints[7, 1] * 300)),
             (145, 90, 178), 5)
    #print (im.shape)
    #print (im)
    cv2.imwrite('zuo_gu.jpg',im)
def draw_shang(joints,frame):
    x = frame[:,0]
    y = frame[:,0]
    z = frame[:,2]
    l = frame[:,9]
    num_p = len(x)
    im = np.zeros([310, 310, 3], dtype=np.int)
    im[:, :, :] = [255, 255, 255]

    for i in range(num_p):
        p_z = int(z[i]*300)
        p_y = int(y[i]*300)
        if l[i] == 1:
            im[p_y,p_z,:] = [255,0,0]
        if l[i] == 2:
            im[p_y,p_z,:] = [0,0,255]
        if l[i] == 0:
            im[p_y,p_z,:] = [0,255,0]
        if l[i] == 3:
            im[p_y,p_z,:] = [46,139,87]
        if l[i] == 4:
            im[p_y,p_z,:] = [238,220,130]
        if l[i] == 5:
            im[p_y,p_z,:] = [139,115,85]

    im = cv2.circle(im, (int(joints[0, 2] * 300), int(joints[0, 0] * 300)), 5, (0, 0, 0), -1)
    im = cv2.circle(im, (int(joints[1, 2] * 300), int(joints[1, 0] * 300)), 5, (0, 0, 0), -1)

    im = cv2.circle(im, (int(joints[2, 2] * 300), int(joints[2, 0] * 300)), 5, (255, 255, 0), -1)
    im = cv2.circle(im, (int(joints[3, 2] * 300), int(joints[3, 0] * 300)), 5, (255, 255, 0), -1)
    im = cv2.circle(im, (int(joints[4, 2] * 300), int(joints[4, 0] * 300)), 5, (255, 255, 0), -1)

    im = cv2.circle(im, (int(joints[5, 2] * 300), int(joints[5, 0] * 300)), 5, (255, 0, 255), -1)
    im = cv2.circle(im, (int(joints[6, 2] * 300), int(joints[6, 0] * 300)), 5, (255, 0, 255), -1)
    im = cv2.circle(im, (int(joints[7, 2] * 300), int(joints[7, 0] * 300)), 5, (255, 0, 255), -1)
    #for o in joints:
    #    im = cv2.circle(im, (int(o[2]*300), int(o[1]*300)), 5, (0, 0, 0), -1)
    cv2.imwrite('./shang.jpg',im)
def draw_zhenggu(joints):
    im = np.zeros([310, 310, 3], dtype=np.int)
    im[:, :, :] = [255, 255, 255]
    im = cv2.circle(im, (int(joints[0, 0] * 300), int(joints[0, 1] * 300)), 5, (0, 0, 0), -1)
    im = cv2.circle(im, (int(joints[1, 0] * 300), int(joints[1, 1] * 300)), 5, (0, 0, 0), -1)
    cv2.line(im, (int(joints[0, 0] * 300), int(joints[0, 1] * 300)), (int(joints[1, 0] * 300), int(joints[1, 1] * 300)), (140,78,23),5)

    im = cv2.circle(im, (int(joints[2, 0] * 300), int(joints[2, 1] * 300)), 5, (255, 255, 0), -1)
    cv2.line(im, (int(joints[1, 0] * 300), int(joints[1, 1] * 300)),(int(joints[2, 0] * 300), int(joints[2, 1] * 300)),
             (45, 178, 3), 5)

    im = cv2.circle(im, (int(joints[3, 0] * 300), int(joints[3, 1] * 300)), 5, (255, 255, 0), -1)
    cv2.line(im, (int(joints[2, 0] * 300), int(joints[2, 1] * 300)),(int(joints[3, 0] * 300), int(joints[3, 1] * 300)),
             (45, 178, 3), 5)
    im = cv2.circle(im, (int(joints[4, 0] * 300), int(joints[4, 1] * 300)), 5, (255, 255, 0), -1)
    cv2.line(im, (int(joints[3, 0] * 300), int(joints[3, 1] * 300)),(int(joints[4, 0] * 300), int(joints[4, 1] * 300)),
             (45, 178, 3), 5)

    im = cv2.circle(im, (int(joints[5, 0] * 300), int(joints[5, 1] * 300)), 5, (255, 0, 255), -1)
    cv2.line(im, (int(joints[1,0] * 300), int(joints[1, 1] * 300)),(int(joints[5, 0] * 300), int(joints[5, 1] * 300)),
             (145, 90, 178 ), 5)
    im = cv2.circle(im, (int(joints[6, 0] * 300), int(joints[6, 1] * 300)), 5, (255, 0, 255), -1)
    cv2.line(im, (int(joints[5, 0] * 300), int(joints[5, 1] * 300)),(int(joints[6, 0] * 300), int(joints[6, 1] * 300)),
             (145, 90, 178), 5)
    im = cv2.circle(im, (int(joints[7, 0] * 300), int(joints[7, 1] * 300)), 5, (255, 0, 255), -1)
    cv2.line(im, (int(joints[6, 0] * 300), int(joints[6, 1] * 300)),(int(joints[7, 0] * 300), int(joints[7, 1] * 300)),
             (145, 90, 178), 5)
    #print (im.shape)
    #print (im)
    cv2.imwrite('zheng_gu.jpg',im)
def draw_shanggu(joints):
    im = np.zeros([310, 310, 3], dtype=np.int)
    im[:, :, :] = [255, 255, 255]
    im = cv2.circle(im, (int(joints[0, 0] * 300), int(joints[0, 2] * 300)), 5, (0, 0, 0), -1)
    im = cv2.circle(im, (int(joints[1, 0] * 300), int(joints[1, 2] * 300)), 5, (0, 0, 0), -1)
    cv2.line(im, (int(joints[0, 0] * 300), int(joints[0, 2] * 300)), (int(joints[1, 0] * 300), int(joints[1, 2] * 300)), (140,78,23),5)

    im = cv2.circle(im, (int(joints[2, 0] * 300), int(joints[2, 2] * 300)), 5, (255, 255, 0), -1)
    cv2.line(im, (int(joints[1, 0] * 300), int(joints[1, 2] * 300)),(int(joints[2, 0] * 300), int(joints[2, 2] * 300)),
             (45, 178, 3), 5)

    im = cv2.circle(im, (int(joints[3, 0] * 300), int(joints[3, 2] * 300)), 5, (255, 255, 0), -1)
    cv2.line(im, (int(joints[2, 0] * 300), int(joints[2, 2] * 300)),(int(joints[3, 0] * 300), int(joints[3, 2] * 300)),
             (45, 178, 3), 5)
    im = cv2.circle(im, (int(joints[4, 0] * 300), int(joints[4, 2] * 300)), 5, (255, 255, 0), -1)
    cv2.line(im, (int(joints[3, 0] * 300), int(joints[3, 2] * 300)),(int(joints[4, 0] * 300), int(joints[4, 2] * 300)),
             (45, 178, 3), 5)

    im = cv2.circle(im, (int(joints[5, 0] * 300), int(joints[5, 2] * 300)), 5, (255, 0, 255), -1)
    cv2.line(im, (int(joints[1,0] * 300), int(joints[1, 2] * 300)),(int(joints[5, 0] * 300), int(joints[5, 2] * 300)),
             (145, 90, 178 ), 5)
    im = cv2.circle(im, (int(joints[6, 0] * 300), int(joints[6, 2] * 300)), 5, (255, 0, 255), -1)
    cv2.line(im, (int(joints[5, 0] * 300), int(joints[5, 2] * 300)),(int(joints[6, 0] * 300), int(joints[6, 2] * 300)),
             (145, 90, 178), 5)
    im = cv2.circle(im, (int(joints[7, 0] * 300), int(joints[7, 2] * 300)), 5, (255, 0, 255), -1)
    cv2.line(im, (int(joints[6, 0] * 300), int(joints[6, 2] * 300)),(int(joints[7, 0] * 300), int(joints[7, 2] * 300)),
             (145, 90, 178), 5)
    #print (im.shape)
    #print (im)
    cv2.imwrite('shang_gu.jpg',im)