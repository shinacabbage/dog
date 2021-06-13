import RoboDog as dog

def main():
    dg=dog.RoboDog([140,40,110,70,60,120,90,90])# 140,40,110,70,60,120,90,90
    while True:
        dg.walk(10)

if __name__ == '__main__':
    main()
