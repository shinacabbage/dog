import ServoMovingList as smlist

#各ピン
#下記は実際に接続した番号と合わせること
lfu=0
rfu=1
lfd=4
rfd=3
lbu=9
rbu=5
lbd=13
rbd=11
class RoboDog:
    def __init__(self,first_deg):
        self.sml=smlist.ServoMovingList([lfu,rfu,lfd,rfd,lbu,rbu,lbd,rbd],first_deg)
        self.base_deg=first_deg#基準の角度を保存　各ｓｅｒｖｏはこの角度との相対角度で決定
        self.motion_setting=False
    def motion_reset(self):#モーションの設定をリセット
        self.motion_setting=False
        self.sml.moving_reset()
    def walk(self,speed):#歩く
        self.sml.set_loopflg(True)
        if self.motion_setting==False:
            self.sml.append([self.base_deg[0]-100,self.base_deg[1]+0,self.base_deg[2]-90,self.base_deg[3]+0,self.base_deg[4]-10,self.base_deg[5]-0,self.base_deg[6]-10,self.base_deg[7]+0],[3,3,3,3,3,3,3,3])
            self.sml.append([self.base_deg[0]-80,self.base_deg[1]+0,self.base_deg[2]-60,self.base_deg[3]+0,self.base_deg[4]-30,self.base_deg[5]-0,self.base_deg[6]+0,self.base_deg[7]+0],[3,3,3,3,3,3,3,3])
            self.sml.append([self.base_deg[0]-80,self.base_deg[1]+0,self.base_deg[2]-60,self.base_deg[3]+0,self.base_deg[4]-30,self.base_deg[5]+40,self.base_deg[6]+0,self.base_deg[7]-40],[3,3,3,3,3,3,3,3])
            self.sml.append([self.base_deg[0]-80,self.base_deg[1]+0,self.base_deg[2]-60,self.base_deg[3]-40,self.base_deg[4]-30,self.base_deg[5]+40,self.base_deg[6]+60,self.base_deg[7]-0],[3,3,3,3,3,3,3,3])
            self.sml.append([self.base_deg[0]-0,self.base_deg[1]+80,self.base_deg[2]+40,self.base_deg[3]+90,self.base_deg[4]-30,self.base_deg[5]-10,self.base_deg[6]+40,self.base_deg[7]-0],[3,3,3,3,3,3,3,3])
            self.motion_setting=True
        self.sml.play_node()
    def backfoward(self,speed):
        #if self.motion_setting==False:
            #モーションをここに記載
        self.sml.play_node()
    def sit_down(self,speed):#座る
        if self.motion_setting==False:
            self.sml.append([self.base_deg[0]-0,self.base_deg[1]+0,self.base_deg[2]+20,self.base_deg[3]-20,self.base_deg[4]+30,self.base_deg[5]-30,self.base_deg[6]+60,self.base_deg[7]-60],[1,1,1,1,1,1,1,1])
            self.motion_setting=True
        self.sml.play_node()
