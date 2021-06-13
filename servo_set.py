import RoboDog as dog
def servo_set():
    #基準角度に設定　main.pyの実行前にこちらでサーボ角度を設定して、脚の取り付けのち、mainを実行してください。
    dg=dog.RoboDog([90,90,90,90,90,90,90,90])

if __name__ == '__main__':
    servo_set()
