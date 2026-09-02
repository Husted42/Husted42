debugMode = 0

###### - variable - #####
black = color(0, 0, 0)
white = color(255, 255, 255)
grey = color(121, 137, 140)
green = color(123, 191, 96)

carX = 50
carY = 250
cloudX = 800
cloud2X = 300
cloudY = 40
cloud2Y = 60
carBattery = 100
chargePlace = 0
velocity = 1
windSpeed=2

#FactoryVariables
factoryCheck1 = 0
factoryCheck2 = 0
factoryCheck3 = 0
factoryValue = 0
factoryState1 = 0
factoryState2 = 0
factoryState3 = 0
goods=0
factoryCollectColor1 = color(255, 0, 0)
factoryCollectColor2 = color(255, 0, 0)
factoryCollectColor3 = color(255, 0, 0)

###### - Functions - #####
#Static objects
def backgrounds():
    fill(green)
    rect(0, 150, 800, 650) #Grass
    fill(136, 233, 252) 
    rect(0, 0, 800, 150) #Sky
    
def drawTree(x, y):
    stroke(black)
    fill(100, 100, 0)
    rect(x - 5, y, 10, 20) #Bush
    fill(0, 200, 0)
    ellipse(x, y - 15, 40, 50) #Wood

def powerplant(x,y):
    fill(224, 133, 20)
    rect(x,y, 60, 30) 
    fill(20, 20, 200)
    rect(x+40, y-30, 10, 30) 
    fill(200, 5, 100)
    triangle(x, y, x+16, y-10, x+16, y)
    triangle(x+16, y, x+32, y-10, x+32, y)
    
def drawTurbine():
    stroke(white)
    line(200, 120, 220, 121)
    line(200, 120, 189, 137)
    line(200, 120, 191, 102)
    line(200, 120, 200, 170)

def drawRoad():
    noStroke()
    fill(grey)
    rect(250, 250, 500, 50)
    fill(grey)
    rect(0, 250, 150, 50)
    rect(700, 250, 50, 500)
    rect(400, 300, 50, 400)
    fill(grey)
    ellipse(200, 275, 150, 150)
    fill(green)
    ellipse(200, 275, 50, 50)
    
def drawChargepoint():
    fill(grey)
    rect(300,300,80,60)
    noStroke()
    fill(250,240,70)
    triangle(340,305,340,330,330,330)
    triangle(340,330,350,330,340,355)
    
###clouds#####
def drawCloudx(x, y):
    noStroke()
    fill(255, 255, 255)
    ellipse(x - 50, y, 50, 40)
    ellipse(x + 50, y, 50, 40)
    ellipse(x, y, 100, 60)

def cloudMove():
    global cloudX
    global cloud2X
    global cloudY
    global cloud2Y
    global windSpeed
    if cloudX < -100:
        cloudX = 900
        cloudY = random(30, 100)
    if cloud2X < -100:
        cloud2X = 900
        cloud2Y = random(30, 100)
    drawCloudx(cloudX, cloudY)
    drawCloudx(cloud2X, cloud2Y)
    cloudX = cloudX - windSpeed/10
    cloud2X = cloud2X - windSpeed/8

def windspeed():
    global windSpeed
    if frameCount%600==0 or frameCount==1:
        windSpeed=(random(3,11))
    fill(black)

        
###factoryGoods###
def drawPickup():
    stroke(0, 0, 0)
    fill(factoryCollectColor1)
    rect(400, 200, 50, 50)
    fill(factoryCollectColor2)
    rect(20, 300, 50, 50)
    fill(factoryCollectColor3)
    rect(450, 550, 50, 50)
    
def factoryChecker1():
    global factoryCheck1
    global factoryCheck2
    global factoryCheck3
    if 400<carX<450 and 200<carY<250:
        factoryCheck1 = 1
    elif 20<carX<70 and 300<carY<350:
        factoryCheck2 = 1
    elif 460<carX<500 and 450<carY<600:
        factoryCheck3 = 1
    else:
        factoryCheck1 = 0
        factoryCheck2 = 0
        factoryCheck3 = 0

def randomFactoryValue():
    global factoryValue
    if frameCount%60 == 0:
        factoryValue = int(random(1, 4))

def OnOffFactoryState():
    global factoryState1
    global factoryState2
    global factoryState3
    global factoryValue
    global factoryCollectColor1
    global factoryCollectColor2
    global factoryCollectColor3
    if factoryValue == 1:
        factoryState1 = 1
        factoryValue = 0
        factoryCollectColor1 = color(0, 255, 0)
    elif factoryValue == 2:
        factoryState2 = 1
        factoryValue = 0
        factoryCollectColor2 = color(0, 255, 0)
    elif factoryValue == 3:
        factoryState3 = 1
        factoryValue = 0
        factoryCollectColor3 = color(0, 255, 0)

def factoryCollect1():
    global goods
    global factoryState1
    global factoryState2
    global factoryState3
    global factoryCollectColor1
    global factoryCollectColor2
    global factoryCollectColor3
    if factoryCheck1 == 1 and factoryState1 == 1 and key == ' ' :
        goods = goods + 1
        factoryState1 = 0
        factoryCollectColor1 = color(255, 0, 0)
    elif factoryCheck2 == 1 and factoryState2 == 1 and key == ' ' :
        goods = goods + 1
        factoryState2 = 0
        factoryCollectColor2 = color(255, 0, 0)
    elif factoryCheck3 == 1 and factoryState3 == 1 and key == ' ' :
        goods = goods + 1
        factoryState3 = 0
        factoryCollectColor3 = color(255, 0, 0)
        
def factorySystem():
    factoryChecker1()
    randomFactoryValue()
    OnOffFactoryState()
    factoryCollect1()

####batterysystem####
def chargepoint():
    global chargePlace
    if 300<carX<380 and 300<carY<360:
        chargePlace = 1
    else:
        chargePlace = 0


def chargeBattery():
    global carBattery
    if key=='p' and chargePlace == 1:
        carBattery=carBattery+1
        
def dechargeBattery():
    global carBattery
    if velocity!=0:
        carBattery = carBattery - 0.1
    if carBattery < 0:
        carBattery = 0
    if carBattery > 100:
        carBattery = 100
    fill(0)
    
    
####car####
def speed():
    global velocity
    if 25>=carBattery>0:
        velocity = 0.50
    if carBattery>25:
        velocity = 1
    if carBattery<=0:
        velocity = 0
        
def movecar():
    global carX
    global carY
    global velocity
    drawCar(carX,carY)
    if (key == 'd'):
        carX = carX + velocity
    if (key == 'a'):
        carX = carX - velocity
    if (key == 'w'):
        carY = carY - velocity
    if (key == 's'):
        carY = carY + velocity
    if key == 'c':
        carX = 310
        carY = 310

def drawCar(x,y):
    stroke(0,0,0)
    fill(107, 250, 255)
    rect(x, y, 50, 20)
    fill(255, 0, 0)
    rect(x - 10, y + 15, 80, 15)
    fill(0, 0, 0)
    ellipse(x+ 5, y + 35, 20, 20)
    ellipse(x+ 50, y+ 35, 20, 20)
    fill(255, 255, 255)
    ellipse(x + 5, y + 35, 15, 15)
    ellipse(x + 50, y + 35, 15, 15)

# miscellaneous #
def textDisplay():
    text('batteryStatus  ' + str(carBattery), 10, 10)
    text('windSpeed='+str(int(windSpeed))+'m/s', 10, 25)
    

def deBugMode():
    if debugMode == 1:
        text("carX = " + str(carX), 10, 700)
        text("carY = " + str(carY), 10, 710)
        text("factoryValue = " + str(factoryValue), 10, 720)
        text("goods = " + str(goods), 10, 730)
        text("factoryCheck1 = " + str(factoryCheck1), 100, 700)
        text("factoryCheck2 = " + str(factoryCheck2), 100, 710)
        text("factoryCheck3 = " + str(factoryCheck3), 100, 720)
        text("factoryState1 = " + str(factoryState1), 200, 700)
        text("factoryState2 = " + str(factoryState2), 200, 710)
        text("factoryState3 = " + str(factoryState3), 200, 720)
    

def objects():
    backgrounds()
    drawRoad()
    powerplant(20,385)
    powerplant(400,160)
    powerplant(510,560)
    drawTurbine()
    drawTree(80, 150)
    drawTree(300, 150)
    drawTree(350, 150)
    drawChargepoint()
    drawPickup()
    
    
##### - canvas - #####
def setup():
    size(800, 800)

#### - mainloop - #####
def draw():
    objects()
    cloudMove()
    chargeBattery()
    dechargeBattery()
    chargepoint()
    movecar()
    speed()
    windspeed()
    textDisplay()
    factorySystem()
    deBugMode()
