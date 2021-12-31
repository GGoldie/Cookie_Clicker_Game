# Simple Cookie Clicker game
# Written in Python 3.10.1
# 31/12/2021
# by @Goldie (Simon)
# v1.02
import turtle

# Creates the game window
wn = turtle.Screen()
wn.title("Cookie Clicker Clone by @Goldie")
wn.setup(850, 850)
wn.bgpic("resources/bg.gif")

# Draws the cookie on screen
cookieImage = "resources/cookie.gif"
wn.register_shape(cookieImage)
cookie = turtle.Turtle()
cookie.shape(cookieImage)
cookie.speed(0)

# Draws the upgrade button on screen
upgradeImage = "resources/upgrade.gif"
wn.register_shape(upgradeImage)
upgrade = turtle.Turtle()
upgrade.shape(upgradeImage)
upgrade.speed(0)
upgrade.penup()
upgrade.sety(-300)

# Initialises variables
# Clicks = cookie balance
clicks = 0
upgradesPurchased = 0
upgradeCost = 10
upgradePower = 2
highScore = 0

# Creates the cookiePen
cookiePen = turtle.Turtle()
cookiePen.hideturtle()
cookiePen.color("white")
cookiePen.penup()

# Creates the costPen
costPen = turtle.Turtle()
costPen.hideturtle()
costPen.color("white")
costPen.penup()

# Creates the Cookies per Click pen
cpcPen = turtle.Turtle()
cpcPen.hideturtle()
cpcPen.color("white")
cpcPen.penup()

# Creates the High score pen
hsPen = turtle.Turtle()
hsPen.hideturtle()
hsPen.color("white")
hsPen.penup()

# Creates the upgrade Click pen
upcPen = turtle.Turtle()
upcPen.hideturtle()
upcPen.color("white")
upcPen.penup()

# Writes the text to display cookies clicked
# If total clicks is a new high score, refresh high score
def updateCookies():
    global clicks
    global highScore
    cookiePen.clear()
    cookiePen.goto(0, 300)
    cookiePen.write(f"Cookies: {clicks}", align="center", font=("Courier New", 32, "bold"))
    if clicks > highScore:
        highScore = clicks
        updateHS()

# Writes the text to display upgrade cost
def drawUpc():
    global upgradeCost
    upcPen.clear()
    upcPen.goto(0, -200)
    upcPen.write(f"Upgrade Click", align="center", font=("Courier New", 22, "bold"))

# Writes the text to display upgrade cost
def updateCost():
    global upgradeCost
    costPen.clear()
    costPen.goto(0, -235)
    costPen.write(f"Cost: {upgradeCost} cookies", align="center", font=("Courier New", 22, "bold"))

# Refresh cpc text, if no upgrades = 1. else, cpc = cpc * param * upgrades owned
def updateCpc():
    global upgradesPurchased
    global upgradePower
    cpcPen.clear()
    cpcPen.goto(0, 250)
    if upgradesPurchased == 0:
        cpc = 1
    else:
        cpc = upgradePower * (upgradesPurchased + 1)
    cpcPen.write(f"Cookies per Click: {cpc}", align="center", font=("Courier New", 20, "bold"))
    cpcPen.penup()
    cpcPen.goto(0, 220)
    cpcPen.write(f"Upgrades purchased: {upgradesPurchased}", align="center", font=("Courier New", 16, "bold"))

# Clear Highscore and redraw with new value
def updateHS():
    global highScore
    hsPen.clear()
    hsPen.goto(-250, -340)
    hsPen.write(f"High Score: {highScore} cookies", align="center", font=("Courier New", 15, "bold"))

# Function for when the cookie is clicked, increment clicks and refresh display
def cookieClicked(x, y):
    global clicks
    global upgradesPurchased
    global upgradePower
    if upgradesPurchased == 0:
        clicks += 1
    else:
        clicks = clicks + (upgradePower * (upgradesPurchased + 1))
    updateCookies()

# Function that checks the player can afford to purchase the upgrade
# if can afford, increase cookies per click, increment purchased, and update text
def upgradePurchase(x, y):
    global clicks
    global upgradesPurchased
    global upgradeCost
    if clicks >= upgradeCost:
        clicks = clicks - upgradeCost
        upgradesPurchased += 1
        upgradeCost = round(upgradeCost * 1.8)
        updateCookies()
        updateCpc()
        updateCost()

# Calls the update functions to write the totals on screen
updateCookies()
updateCpc()
drawUpc()
updateCost()
updateHS()

# Calls upgrade function on click
upgrade.onclick(upgradePurchase)

# Calls clicked function on click
cookie.onclick(cookieClicked)


wn.mainloop()