from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)

class Cell:#サーボの情報を設定するノード
    def __init__(self,deg_,rot_time_,servo_speed_):
        self.front=None
        self.next=None
        self.deg=deg_
        self.rot_time=rot_time_
        self.servo_speed=servo_speed_

class ServoMovingList:
    def __init__(self,pin,deg):
        self.pin=pin
        self.servo_deg=deg
        self.loop_flg=False
        #各サーボの角度初期化
        num=0
        for i in self.pin:
            kit.servo[i].angle=self.servo_deg[num]
            num+=1;
        self.servo_reached=[False,False,False,False,False,False,False,False]
        self.servo_speed=[2,2,2,2,2,2,2,2]#各サーボの初期設定スピード
        self.startdeg=deg

        self.head =Cell(deg,0,self.servo_speed)
        self.front=self.head
        self.currentcell=self.head
    def set_loopflg(self,flg_):
        self.loop_flg=flg_
    def set_speed(self,speed_):
        self.speed=speed_
    def append(self,deg_,servo_speed_):#目標とする角度、各サーボのスピードを設定
        self.endflg=False;
        cell=Cell(deg_,0,servo_speed_)
        self.front.next=cell
        self.front=cell
    def moving_reset(self):
        self.startdeg=self.servo_deg
        self.head =Cell(self.servo_deg,0)
        self.front=self.head
        self.currentcell=self.head
    def play_node(self):
            if self.endflg==False:
                num=0
                for i in self.servo_deg:
                    if self.startdeg[num]<self.currentcell.deg[num]:
                        if self.servo_reached[num]==False:
                            self.servo_deg[num]+=self.currentcell.servo_speed[num]#self.speed
                            if self.servo_deg[num]>=self.currentcell.deg[num]:
                                #print("reached")
                                self.servo_reached[num]=True
                    elif self.startdeg[num]>self.currentcell.deg[num]:
                        if self.servo_reached[num]==False:
                            self.servo_deg[num]-=self.currentcell.servo_speed[num]#self.speed
                            if self.servo_deg[num]<=self.currentcell.deg[num]:
                                #print("reached")
                                self.servo_reached[num]=True
                    num+=1
                time.sleep(0.01)
                #各サーボへの書き込み
                num=0
                for i in self.pin:
                    kit.servo[i].angle=self.servo_deg[num]
                    #誤差修正
                    if abs(self.servo_deg[num]-self.currentcell.deg[num])<0.01:
                        self.servo_deg[num]=self.currentcell.deg[num]
                        self.servo_reached[num]=True
                    num+=1
                #到着
                if self.servo_reached[0] and self.servo_reached[1] and self.servo_reached[2] and self.servo_reached[3] and self.servo_reached[4] and self.servo_reached[5] and self.servo_reached[6] and self.servo_reached[7]:
                    self.startdeg=self.servo_deg
                    if self.currentcell.next ==None and self.loop_flg==True:#ループフラグがたってて、ノードの終わりに来た時最初のノードに戻る
                        self.currentcell=self.head
                    elif self.currentcell.next ==None:#つぎのノードがないときは終了フラグをたてる
                        self.endflg=True
                    else:#とくに何もない場合は次のノードに
                        self.currentcell=self.currentcell.next
                    self.servo_reached=[False,False,False,False,False,False,False,False]
