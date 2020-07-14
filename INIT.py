import pickle
import numpy as np
import os
import numpy as np
def init():
    ppp = os.listdir('./final_data/')
    ooo = []
    for o in ppp:
        f = open('./final_data/'+o,'rb')
        sss = pickle.load(f)
        f.close()
        ooo.append(sss)
        #ss.show_hole_file(sss)
    ooo = np.array(ooo)
    #print (ooo.shape)

    x = ooo[:,:,0]
    y = ooo[:,:,1]
    z = ooo[:,:,2]
    x_max = x.max()
    x_min = x.min()
    y_max = y.max()
    y_min = y.min()
    z_max = z.max()
    z_min = z.min()
    
    x_n = (x-x_min)/(x_max-x_min)
    y_n = (y-y_min)/(y_max-y_min)
    z_n = (z-z_min)/(z_max-z_min)

    x_n = np.expand_dims(x_n,axis=2)
    y_n = np.expand_dims(y_n,axis=2)
    z_n = np.expand_dims(z_n,axis=2)

    xyz = np.concatenate([x_n,y_n,z_n],axis=2)

    rgb = ooo[:,:,3:6]
    rgb = rgb/255.0

    lll = ooo[:,:,6]
    lll = np.expand_dims(lll,axis=2)

    ppp = np.concatenate([xyz,rgb,rgb,lll],axis=2)
    #print (ppp.shape)


    # In[5]:

    return ppp
