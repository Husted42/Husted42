###### - variable - #####
grey = color(121, 137, 140) 
factoryState1 = 0
factoryState2 = 0
agarX = 200
agarY = 200
goods = 0
state = 0
onOff1 = 0
onOff2 = 0

test = 0

###### - Functions - #####
#StaticObjects
def drawAgar():
    rect(agarX, agarY, 40, 40)

#Factories
def factory1():
    rect(50, 50, 50, 50)
    
def factory2():
    rect(300, 50, 50, 50)

#MovePlayer
def agarMove():
    global agarX
    global agarY
    if (key == 'd'):
        agarX = agarX + 1.5
    if (key == 'a'):
        agarX = agarX - 1.5
    if (key == 'w'):
        agarY = agarY - 1.5
    if (key == 's'):
        agarY = agarY + 1.5

#Tjek if player is in factory
def factoryRefill():
    global factoryState1
    if 50<agarX<100 and 50<agarY<100:
        factoryState1 = 1
    else:
        factoryState1 = 0

def factoryRefill2():
    global factoryState2
    if 300<agarX<350 and 50<agarY<100:
        factoryState2 = 1
    else:
        factoryState2 = 0

#Set random state value
def setStateValue():
    global state
    if frameCount%300==0:
        state = int(random(1, 3))

#Set factory state
def factoryOnOff():
    global onOff1
    global onOff2
    global state
    if state == 1:
        onOff1 = 1
        state = 0
    elif state == 2:
        onOff2 = 1
        state = 0

def factoryCollect():
    global goods
    global onOff1
    if factoryState1 == 1 and onOff1 == 1 and key == 'c' :
        goods = goods + 1
        onOff1 = 0

def factoryCollect2():
    global goods
    global onOff2
    if factoryState2 == 1 and onOff2 == 1 and key == 'c':
        goods = goods + 1
        onOff2 = 0

# - Call functions - #
def factoryFunctions():
    factoryRefill()
    factoryRefill2()
    #factoryReset()
    factoryCollect2()
    factoryCollect()
    factoryOnOff()
    setStateValue()
    

def drawObjects():
    drawAgar()
    factory1()
    factory2()

#Text
def factoryStateText():
    text('factory1 = '+str(factoryState1), 0, 10)
    text('factory2 = '+str(factoryState2), 0, 20)
    text('goods = '+str(goods), 100, 10)
    text('onOff1 = '+str(onOff1), 200, 10)
    text('onOff2 = '+str(onOff2), 200, 20)
    text('test = '+str(state), 100, 20)

##### - canvas - #####
def setup():
    size(400,400)

#### - mainloop - #####
def draw():
    background(grey)
    drawObjects()
    factoryFunctions()
    agarMove()
    factoryStateText()
