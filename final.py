import wx
import numpy as np
import read_pcd
import cv2
import pickle


points = read_pcd.init()
x = points[:,:,0]
y = points[:,:,1]
z = points[:,:,2]
width = x.max()-x.min()
height = y.max() - y.min()

joints =  np.zeros([8,3],dtype=np.float)
num = 0

class Example(wx.Frame):

    def __init__(self,title):
        super(Example, self).__init__(None,title='Annotation Tools',size=(1600,1000))

        self.InitUI()
        self.Center()

    def InitUI(self):

        self.pnl = wx.Panel(self)
        #主panel 基础得panel

        #这个是用于还下一张点云得按钮
        self.changepic_Button = wx.Button(self.pnl, label = 'CHANGE',pos=(100,800),size=(60,20))
        self.changepic_Button.Bind(wx.EVT_BUTTON,self.ChangePic)

        #这是用于记录点
        #self.save_Button = wx.Button(self.pnl, label = 'SHOW', pos = (600,100),size=(60,20))

        #用于清零
        self.clear_Button = wx.Button(self.pnl, label = 'CLEAR',pos= (100,830),size=(60,20))
        self.clear_Button.Bind(wx.EVT_BUTTON,self.Clear)

        #用于手动设置z坐标
        self.set_Btton = wx.Button(self.pnl, label = 'SetZ', pos = (100,860),size=(60,20))
        self.set_Btton.Bind(wx.EVT_BUTTON,self.set_z)
        #用于保存
        self.save_Button = wx.Button(self.pnl, label = 'SAVE',pos=(100,890),size=(60,20))
        self.save_Button.Bind(wx.EVT_BUTTON,self.save)
        #用于选择多少号点云
        self.path_text = wx.TextCtrl(self.pnl,pos=(500,480),size=(40,20))

        #用于显示不同的视图
        self.SHOW_Button = wx.Button(self.pnl, label='SHOW', pos=(180, 800), size=(60, 20))
        self.SHOW_Button.Bind(wx.EVT_BUTTON, self.show_cankao)

        #用于显示和获得关节的坐标
        self.j1_text = wx.TextCtrl(self.pnl, pos=(400, 510), size=(180, 20))
        self.j2_text = wx.TextCtrl(self.pnl, pos=(400, 540), size=(180, 20))
        self.j3_text = wx.TextCtrl(self.pnl, pos=(400, 570), size=(180, 20))
        self.j4_text = wx.TextCtrl(self.pnl, pos=(400, 610), size=(180, 20))
        self.j5_text = wx.TextCtrl(self.pnl, pos=(400, 640), size=(180, 20))
        self.j6_text = wx.TextCtrl(self.pnl, pos=(400, 670), size=(180, 20))
        self.j7_text = wx.TextCtrl(self.pnl, pos=(400, 700), size=(180, 20))
        self.j8_text = wx.TextCtrl(self.pnl, pos=(400, 730), size=(180, 20))

        #用于手动设置z坐标
        self.z1_text = wx.TextCtrl(self.pnl, pos=(600, 510), size=(80, 20))
        self.z2_text = wx.TextCtrl(self.pnl, pos=(600, 540), size=(80, 20))
        self.z3_text = wx.TextCtrl(self.pnl, pos=(600, 570), size=(80, 20))
        self.z4_text = wx.TextCtrl(self.pnl, pos=(600, 610), size=(80, 20))
        self.z5_text = wx.TextCtrl(self.pnl, pos=(600, 640), size=(80, 20))
        self.z6_text = wx.TextCtrl(self.pnl, pos=(600, 670), size=(80, 20))
        self.z7_text = wx.TextCtrl(self.pnl, pos=(600, 700), size=(80, 20))
        self.z8_text = wx.TextCtrl(self.pnl, pos=(600, 730), size=(80, 20))

        #和cpnl相同的位置用于获取鼠标点击事件
        self.cpn2 = wx.Panel(self.pnl, pos=(50, 20), size=(400, 400))
        #用于显示主视图得点云得框
        self.cpnl = wx.Panel(self.pnl, pos=(50, 20), size=(400, 400))


        self.cpnl.SetBackgroundColour('red')

        self.zuo = wx.Panel(self.pnl, pos=(50,450), size=(310,310))

        #self.Bind(wx.EVT_KEY_DOWN, self.onMove)
        #self.Bind(wx.EVT_MOTION, self.onMove)
        # 用于标注,双击触发
        self.cpn2.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
        self.zuo.SetBackgroundColour('blue')
        #self.changepic_Button.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)

        #用于显示左视图骨架照片
        self.cn_gu_zuo = wx.Panel(self.pnl, pos=(980, 20), size=(310, 310))
        self.cn_gu_zuo.SetBackgroundColour('blue')

        #用于显示上视图照片
        self.cn_shang = wx.Panel(self.pnl, pos=(650, 20), size=(310, 310))
        self.cn_shang.SetBackgroundColour('blue')

        #用于显示正视图照片
        self.cn_gu_zheng = wx.Panel(self.pnl, pos=(750, 400), size=(310, 310))
        self.cn_gu_zheng.SetBackgroundColour('blue')

        # 用于显示上视图骨架照片
        self.cn_gu_shang = wx.Panel(self.pnl, pos=(1080, 400), size=(310, 310))
        self.cn_gu_shang.SetBackgroundColour('blue')
    def show_cankao(self,event):
    #    print ("OK")
        global joints
        path = self.path_text.GetValue()
        path = int(path)
        frame = points[path]
        read_pcd.draw_zuo(joints,frame)
        read_pcd.draw_gu(joints)
        read_pcd.draw_shang(joints,frame)
        read_pcd.draw_zhenggu(joints)
        read_pcd.draw_shanggu(joints)
        wx.StaticBitmap(self.zuo, wx.ID_ANY,
                        wx.Bitmap("zuo.jpg", wx.BITMAP_TYPE_ANY))

        self.zuo.Refresh()
        wx.StaticBitmap(self.cn_gu_zuo, wx.ID_ANY,
                    wx.Bitmap("zuo_gu.jpg", wx.BITMAP_TYPE_ANY))

        self.cn_gu_zuo.Refresh()
        wx.StaticBitmap(self.cn_shang, wx.ID_ANY,
                    wx.Bitmap("shang.jpg", wx.BITMAP_TYPE_ANY))

        self.cn_shang.Refresh()
        wx.StaticBitmap(self.cn_gu_zheng, wx.ID_ANY,
                    wx.Bitmap("zheng_gu.jpg", wx.BITMAP_TYPE_ANY))

        self.cn_gu_zheng.Refresh()
        wx.StaticBitmap(self.cn_gu_shang, wx.ID_ANY,
                    wx.Bitmap("shang_gu.jpg", wx.BITMAP_TYPE_ANY))

        self.cn_gu_shang.Refresh()
    def set_z(self,event):
        global joints
        z1 = self.z1_text.GetValue()
        z2 = self.z2_text.GetValue()
        z3 = self.z3_text.GetValue()
        z4 = self.z4_text.GetValue()
        z5 = self.z5_text.GetValue()
        z6 = self.z6_text.GetValue()
        z7 = self.z7_text.GetValue()
        z8 = self.z8_text.GetValue()

        z1 = float(z1)
        z2 = float(z2)
        z3 = float(z3)
        z4 = float(z4)
        z5 = float(z5)
        z6 = float(z6)
        z7 = float(z7)
        z8 = float(z8)

        joints[0, 2] = z1
        joints[1, 2] = z2
        joints[2, 2] = z3
        joints[3, 2] = z4
        joints[4, 2] = z5
        joints[5, 2] = z6
        joints[6, 2] = z7
        joints[7, 2] = z8

        self.j1_text.SetValue("x: " + str(joints[0, 0]) + "y: " + str(joints[0, 1]) + "z: " + str(joints[0, 2]))
        self.j2_text.SetValue("x: " + str(joints[1, 0]) + "y: " + str(joints[1, 1]) + "z: " + str(joints[1, 2]))
        self.j3_text.SetValue("x: " + str(joints[2, 0]) + "y: " + str(joints[2, 1]) + "z: " + str(joints[2, 2]))
        self.j4_text.SetValue("x: " + str(joints[3, 0]) + "y: " + str(joints[3, 1]) + "z: " + str(joints[3, 2]))
        self.j5_text.SetValue("x: " + str(joints[4, 0]) + "y: " + str(joints[4, 1]) + "z: " + str(joints[4, 2]))
        self.j6_text.SetValue("x: " + str(joints[5, 0]) + "y: " + str(joints[5, 1]) + "z: " + str(joints[5, 2]))
        self.j7_text.SetValue("x: " + str(joints[6, 0]) + "y: " + str(joints[6, 1]) + "z: " + str(joints[6, 2]))
        self.j8_text.SetValue("x: " + str(joints[7, 0]) + "y: " + str(joints[7, 1]) + "z: " + str(joints[7, 2]))

    def save(self,event):
        global joints

        path = self.path_text.GetValue()
        path = int(path)
        frame = points[path]

        whole = []
        whole.append(joints)
        whole.append(frame)
        s_p = './save/' + str(path)+'.pkl'
        f = open(s_p,'wb')
        pickle.dump(whole,f)
        f.close()


    def Clear(self,event):
        global num
        global joints
        num = 0
        joints = np.zeros([8,3],dtype=np.float)
        self.j1_text.SetValue("x: " + str(joints[0,0])+ "y: "+str(joints[0,1])+"z: "+str(joints[0,2]))
        self.j2_text.SetValue("x: " + str(joints[1, 0]) + "y: " + str(joints[1, 1]) + "z: " + str(joints[1, 2]))
        self.j3_text.SetValue("x: " + str(joints[2, 0]) + "y: " + str(joints[2, 1]) + "z: " + str(joints[2, 2]))
        self.j4_text.SetValue("x: " + str(joints[3, 0]) + "y: " + str(joints[3, 1]) + "z: " + str(joints[3, 2]))
        self.j5_text.SetValue("x: " + str(joints[4, 0]) + "y: " + str(joints[4, 1]) + "z: " + str(joints[4, 2]))
        self.j6_text.SetValue("x: " + str(joints[5, 0]) + "y: " + str(joints[5, 1]) + "z: " + str(joints[5, 2]))
        self.j7_text.SetValue("x: " + str(joints[6, 0]) + "y: " + str(joints[6, 1]) + "z: " + str(joints[6, 2]))
        self.j8_text.SetValue("x: " + str(joints[7, 0]) + "y: " + str(joints[7, 1]) + "z: " + str(joints[7, 2]))

        path = self.path_text.GetValue()
        path = int(path)
        frame = points[path]
        read_pcd.draw(frame)
        wx.StaticBitmap(self.cpnl, wx.ID_ANY,
                                    wx.Bitmap("zheng.jpg",wx.BITMAP_TYPE_ANY))
        #self.cpnl.Refresh()
        self.z1_text.SetValue(str(joints[0, 2]))
        self.z2_text.SetValue(str(joints[1, 2]))
        self.z3_text.SetValue(str(joints[2, 2]))
        self.z4_text.SetValue(str(joints[3, 2]))
        self.z5_text.SetValue(str(joints[4, 2]))
        self.z6_text.SetValue(str(joints[5, 2]))
        self.z7_text.SetValue(str(joints[6, 2]))
        self.z8_text.SetValue(str(joints[7, 2]))


    def onMove(self,e):
        pos = e.GetPosition()
        print (pos.x)
    def on_left_down(self,event):
        '''
        用于接受标注
        '''
        global joints
        global num
        if num>=8:
            event.Skip()
        #print ("OK")
        else:
            pos = event.GetPosition()
            x = pos.x
            y = pos.y
            #print (x)
            #print (y)

            im = cv2.imread('zheng.jpg')
            im = cv2.circle(im,(x,y),5,(0,0,0),-1)
            cv2.imwrite('zheng.jpg',im)

            path = self.path_text.GetValue()
            path = int(path)
            frame = points[path]

            joints[num,0] = pos.x/400.0

            joints[num,1] = pos.y/400.0
            joints[num,2] = read_pcd.find_z(pos.x/400.0,pos.y/400.0,frame)
            sss = 'x:'+str(joints[num,0])+' y:'+str(joints[num,1]) + 'z: ' + str(joints[num,2])
            if num == 0:
                self.j1_text.SetValue(sss)
            if num == 1:
                self.j2_text.SetValue(sss)
            if num == 2:
                self.j3_text.SetValue(sss)
            if num == 3:
                self.j4_text.SetValue(sss)
            if num == 4:
                self.j5_text.SetValue(sss)
            if num == 5:
                self.j6_text.SetValue(sss)
            if num == 6:
                self.j7_text.SetValue(sss)
            if num == 7:
                self.j8_text.SetValue(sss)
            num+=1
            wx.StaticBitmap(self.cpnl, wx.ID_ANY,
                            wx.Bitmap("zheng.jpg", wx.BITMAP_TYPE_ANY))
            #self.cpnl.Refresh()
            self.z1_text.SetValue(str(joints[0, 2]))
            self.z2_text.SetValue(str(joints[1, 2]))
            self.z3_text.SetValue(str(joints[2, 2]))
            self.z4_text.SetValue(str(joints[3, 2]))
            self.z5_text.SetValue(str(joints[4, 2]))
            self.z6_text.SetValue(str(joints[5, 2]))
            self.z7_text.SetValue(str(joints[6, 2]))
            self.z8_text.SetValue(str(joints[7, 2]))

    def ChangePic(self,e):
        '''
        用于自动换点云帧
        :param e: 事件自动填了

        :return:
        '''
    #    #obj = e.GetEventObject()
        global joints
        global num
        joints = np.zeros([8, 3], dtype=np.float)
        num = 0
        self.cpnl.SetBackgroundColour('green')
        path =  self.path_text.GetValue()
        path = int(path)
        frame = points[path]
        read_pcd.draw(frame)
        wx.StaticBitmap(self.cpnl, wx.ID_ANY,
                                    wx.Bitmap("zheng.jpg",wx.BITMAP_TYPE_ANY))
        self.j1_text.SetValue("x: " + str(joints[0, 0]) + "y: " + str(joints[0, 1]) + "z: " + str(joints[0, 2]))
        self.j2_text.SetValue("x: " + str(joints[1, 0]) + "y: " + str(joints[1, 1]) + "z: " + str(joints[1, 2]))
        self.j3_text.SetValue("x: " + str(joints[2, 0]) + "y: " + str(joints[2, 1]) + "z: " + str(joints[2, 2]))
        self.j4_text.SetValue("x: " + str(joints[3, 0]) + "y: " + str(joints[3, 1]) + "z: " + str(joints[3, 2]))
        self.j5_text.SetValue("x: " + str(joints[4, 0]) + "y: " + str(joints[4, 1]) + "z: " + str(joints[4, 2]))
        self.j6_text.SetValue("x: " + str(joints[5, 0]) + "y: " + str(joints[5, 1]) + "z: " + str(joints[5, 2]))
        self.j7_text.SetValue("x: " + str(joints[6, 0]) + "y: " + str(joints[6, 1]) + "z: " + str(joints[6, 2]))
        self.j8_text.SetValue("x: " + str(joints[7, 0]) + "y: " + str(joints[7, 1]) + "z: " + str(joints[7, 2]))

        self.z1_text.SetValue(str(joints[0, 2]))
        self.z2_text.SetValue(str(joints[1, 2]))
        self.z3_text.SetValue(str(joints[2, 2]))
        self.z4_text.SetValue(str(joints[3, 2]))
        self.z5_text.SetValue(str(joints[4, 2]))
        self.z6_text.SetValue(str(joints[5, 2]))
        self.z7_text.SetValue(str(joints[6, 2]))
        self.z8_text.SetValue(str(joints[7, 2]))

        self.cpnl.Refresh()
app = wx.App()
ex = Example("oo")
ex.Show()
app.MainLoop()
