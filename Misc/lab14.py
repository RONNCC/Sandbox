import Tkinter
from random import randint,choice
import tkMessageBox
from time import sleep,time
wheight = 200
wwidth =200
cdiameter = 20
top = Tkinter.Tk()
C = Tkinter.Canvas(top, bg="white", height=wheight, width=wwidth)
circles = []
for y in range(wheight/cdiameter):
    temp = []
    for x in range(wwidth/cdiameter):
        temp.append(-1);
    circles.append(temp);

array = []

background = "white"
def makeinitial():
    for y in range(wheight/cdiameter):
        temp = []
        for x in range(wwidth/cdiameter):
            temp.append(randint(1,2));
        array.append(temp);
    redraw()
    C.pack()
def deletecorners():
    array[0][0] = 0
    array[len(array)-1][0] = 0
    array[0][len(array)-1] =0
    array[len(array)-1][len(array)-1] =0
    redraw()
def delete20():
    removed = 0
    while(removed < 20):
        y = randint(0,len(array)-1)
        x = randint(0,len(array)-1)
        if array[y][x] != 0:
            C.delete(circles[y][x])
            array[y][x] = 0
            removed+=1
def add5():
    added = 0
    while(added< 5):
        y = randint(0,len(array)-1)
        x = randint(0,len(array)-1)
        if array[y][x] == 0:
            color = choice(["red","blue"])
            circles[y][x] = C.create_oval(cdiameter*y,cdiameter*x,cdiameter+cdiameter*y, cdiameter+cdiameter*x, fill = color)
            if color == "red":
                array[y][x] = 2
            if color == "blue":
                array[y][x] = 1
            added+=1
def isvalid(x,y):
  return (x>=0 and x<len(array) and y>=0 and y < len(array))

def neighbors(x,y):
  neighs = []
  for dx in [-1,0,1]:
    for dy in [-1,0,1]:
      if (dx == 0 and dy == 0):
        continue
      if isvalid(dx+x,dy+y) == True:
        neighs.append((dx+x,dy+y))
  return neighs
def ishappy(x,y):
  neighs = neighbors(x,y)
  lenn = len(neighs)
  eleis = array[y][x]
  want = -1
  if lenn == 1 or lenn ==2:
    want = 1
  if lenn == 3 or lenn ==4 or lenn == 5:
    want = 2
  if lenn == 6 or lenn ==7 or lenn == 8:
    want = 3
  have = sum([1 for x in neighs if array[x[1]][x[0]] == eleis])
  return (have >= want)
def ishappyat(x,y,color):
  neighs = neighbors(x,y)
  lenn = len(neighs)
  eleis = color
  want = -1
  if lenn == 1 or lenn ==2:
    want = 1
  if lenn == 3 or lenn ==4 or lenn == 5:
    want = 2
  if lenn == 6 or lenn ==7 or lenn == 8:
    want = 3
  have = sum([1 for x in neighs if array[x[1]][x[0]] == eleis])
  return (have >= want)
def empty(x,y):
    emp = []
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx==0 and dy ==0:
                continue
            if isvalid(dx+x,dy+y) and array[y][x] ==0:
                emp.append((dx+x,dy+y))
    return emp
def move(x,y):
    possible = -1
    empties = empty(x,y)
    if len(empties) > 0:
        for e in empties:
            if ishappyat(e[0],e[1],array[y][x]):
                moveto(e[0],e[1],x,y)
                return 2
        ##else
        rchoice = choice(empties)
        moveto(rchoice[0],rchoice[1],x,y)
        return 1
    else:
        return 0
def circlesDefined(x,y):
    return (circles[y][x] != -1)
def redraw():
    for y in range(len(array)):
      for x in range(len(array[y])):
            if array[y][x] == 0:
                if circlesDefined(x,y) == True:
                  C.delete(circles[y][x])
                else:
                    circles[y][x] == -1
            if array[y][x] == 1:
                if circlesDefined(x,y) == True:
                    C.delete(circles[y][x])
                    circles[y][x] = C.create_oval(cdiameter*y,cdiameter*x,cdiameter+cdiameter*y, cdiameter+cdiameter*x, fill = "blue")
                else:
                    circles[y][x] = C.create_oval(cdiameter*y,cdiameter*x,cdiameter+cdiameter*y, cdiameter+cdiameter*x, fill = "blue")
            if array[y][x] == 2:
                if circlesDefined(x,y) == True:
                    C.delete(circles[y][x])
                    circles[y][x] = C.create_oval(cdiameter*y,cdiameter*x,cdiameter+cdiameter*y, cdiameter+cdiameter*x, fill = "red")
                else:
                    circles[y][x] = C.create_oval(cdiameter*y,cdiameter*x,cdiameter+cdiameter*y, cdiameter+cdiameter*x, fill = "red")
            if array[y][x] == 3:
                if circlesDefined(x,y) == True:
                    C.delete(circles[y][x])
                    circles[y][x] = C.create_oval(cdiameter*y,cdiameter*x,cdiameter+cdiameter*y, cdiameter+cdiameter*x, fill = "green")
                else:
                    circles[y][x] = C.create_oval(cdiameter*y,cdiameter*x,cdiameter+cdiameter*y, cdiameter+cdiameter*x, fill = "green")
            if array[y][x] == 4:
                if circlesDefined(x,y) == True:
                    C.delete(circles[y][x])
                    circles[y][x] = C.create_oval(cdiameter*y,cdiameter*x,cdiameter+cdiameter*y, cdiameter+cdiameter*x, fill = "orange")
                else:
                    circles[y][x] = C.create_oval(cdiameter*y,cdiameter*x,cdiameter+cdiameter*y, cdiameter+cdiameter*x, fill = "orange")
            if array[y][x] == 5:
                if circlesDefined(x,y) == True:
                    C.delete(circles[y][x])
                    circles[y][x] = C.create_oval(cdiameter*y,cdiameter*x,cdiameter+cdiameter*y, cdiameter+cdiameter*x, fill = "pink")
                else:
                    circles[y][x] = C.create_oval(cdiameter*y,cdiameter*x,cdiameter+cdiameter*y, cdiameter+cdiameter*x, fill = "pink")

def moveto(x1,y1,x2,y2):
##    if(array[y1][x1] != 0):
##        print 'MoveError'
##        print 'at:', array[y1][x1]
##        exit(1)
    array[y1][x1] = array[y2][x2]
    array[y2][x2] = 0
def checkAllHappy():
    for y in range(len(array)):
        for x in range(len(array[y])):
            if ishappy(x,y) == False:
                return False
    return True
            
def makehappy():
    z = 0
    last = array
    while checkAllHappy() == False:
        z+=1
        print 'iteration: ',z,' elements:', sum([sum([1 for y in x]) for x in array])
        for y in range(len(array)):
            for x in range(len(array[y])):
                happy = ishappy(x,y)
                if happy == True:
                    continue
                if happy == False:
                    move(x,y)
        redraw()
        sleep(1)
def main():
    makeinitial()
    ##delete corners
    C.after(1000,deletecorners)
    C.after(2000,delete20)
    C.after(3000,add5)
    C.after(4000,makehappy)
    top.mainloop()

if __name__ == "__main__":
    main()


