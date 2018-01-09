array=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

def printarray():
    print(array[0][0],array[0][1],array[0][2],array[0][3],array[0][4])
    print(array[1][0],array[1][1],array[1][2],array[1][3],array[1][4])
    print(array[2][0],array[2][1],array[2][2],array[2][3],array[2][4])
    print(array[3][0],array[3][1],array[3][2],array[3][3],array[3][4])
    print(array[4][0],array[4][1],array[4][2],array[4][3],array[4][4])

#初始点设置
ini_x=3
ini_y=3

array[ini_x-1][ini_y-1]=1
printarray()
print("开始你的表演")
#通过wasd控制1的上下左右的移动，空格代表操作结束
while 1==1:
    p=input()
    if p==' ':
        break
    else:
        if p=='w':
            if ini_x==1:
                continue           
            array[ini_x-1][ini_y-1]=0           
            ini_x=ini_x-1
            array[ini_x-1][ini_y-1]=1
        else:
            if p=='s':
                if ini_x==5:
                    continue
                array[ini_x-1][ini_y-1]=0
                ini_x=ini_x+1
                array[ini_x-1][ini_y-1]=1
            else:
                if p=='a':
                    if ini_y==1:
                        continue
                    array[ini_x-1][ini_y-1]=0
                    ini_y=ini_y-1
                    array[ini_x-1][ini_y-1]=1
                else:
                    if p=='d':
                        if ini_y==5:
                            continue
                        array[ini_x-1][ini_y-1]=0
                        ini_y=ini_y+1
                        array[ini_x-1][ini_y-1]=1
                    else:
                        continue
    printarray()



