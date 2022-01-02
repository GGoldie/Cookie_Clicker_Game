# Simple Cookie Clicker game
# Written in Python 3.10.1
# 31/12/2021
# by @Goldie (Simon)
# v2.00
import pygame
import os

pygame.init()

# Creates the game display object
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CENTERx, CENTERy = round(WIDTH * 0.5), round(HEIGHT * 0.5)
FONT = pygame.font.SysFont("Courier New", 24, True)
FONTxsmall = pygame.font.SysFont("Courier New", 18, False)
FONTsmall = pygame.font.SysFont("Courier New", 20, True)
FONTbig = pygame.font.SysFont("Courier New", 36, True)
PALE_BLUE = (202, 228, 241)
pygame.display.set_caption("Cookie Clicker")

CLOCK = pygame.time.Clock()
FPS = 60

COOKIE_IMAGE = pygame.image.load(os.path.join("resources", "cookie.png"))
EXIT_IMAGE = pygame.image.load(os.path.join("resources", "exit.png"))
UPGRADE_IMAGE = pygame.image.load(os.path.join("resources", "upgrade.png"))
CLICKER_IMAGE = pygame.image.load(os.path.join("resources", "mouse.png"))


class Button():
    def __init__(self, x, y, image, scale):
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.angle = 0
        self.clicked = False

    def draw(self):
        """Draw button on screen"""
        WIN.blit(self.image, (self.x - int(self.width/2), self.y - int(self.height/2)))

        action = False

        self.rect.x = self.x - int(self.width / 2)
        self.rect.y = self.y - int(self.height / 2)

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and (pygame.mouse.get_pressed()[0] == 1 and not self.clicked):
            self.clicked = True
            action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action

    def drawRotate(self, speed):
        """Draw a rotating button on screen at the speed of @para speed"""
        self.angle = self.angle + speed
        imageCopy = pygame.transform.rotate(self.image, self.angle)
        WIN.blit(imageCopy, (self.x - int(imageCopy.get_width() / 2), self.y - int(imageCopy.get_height() / 2)))

        action = False

        self.rect.x = self.x - int(self.width / 2)
        self.rect.y = self.y - int(self.height / 2)

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and (pygame.mouse.get_pressed()[0] == 1 and not self.clicked):
            self.clicked = True
            action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action


# Creates the cookie as an object of class Button with x, y, image, scale
cookieButton = Button(CENTERx - 300, CENTERy + 50, COOKIE_IMAGE, 1)
upgradeButton = Button(1550, 500, UPGRADE_IMAGE, 0.15)
clickerButton = Button(1430, 800, CLICKER_IMAGE, 0.1)

cookieBalance = 0
highScore = 0
upgradesPurchased = 0
clickersPurchased = 0
cps = 0
cookiesPerClick = 0
second = True
pygame.time.set_timer(second, 1000)
upgradeCost = 0
clickerCost = 0


def gameText():
    global cookieBalance
    global highScore
    global cookiesPerClick
    global clickersPurchased
    global cps
    global cookiesPerClick
    global upgradeCost

    cookieBalanceText = FONTbig.render("Cookies: " + str(cookieBalance), False, (0, 0, 0))
    WIN.blit(cookieBalanceText, (215, 30))

    infoText1 = FONTxsmall.render("Click the cookie to bake cookies", False, (0, 0, 0))
    WIN.blit(infoText1, (480, 670))

    infoText2 = FONTxsmall.render("Click the upgrade or clicker icons to purchase", False, (0, 0, 0))
    WIN.blit(infoText2, (400, 690))

    upgradesinfoText1 = FONTsmall.render("Purchase upgrades to increase", False, (0, 0, 0))
    WIN.blit(upgradesinfoText1, (720, 130))

    upgradesinfoText2 = FONTsmall.render("the amount of cookies per click", False, (0, 0, 0))
    WIN.blit(upgradesinfoText2, (718, 160))

    upgradesPurchasedText = FONT.render("Upgrades Purchased: " + str(upgradesPurchased), False, (0, 0, 0))
    WIN.blit(upgradesPurchasedText, (750, 250))

    upgradeCostText = FONT.render("Cost to Purchase Upgrade: " + str(upgradeCost), False, (0, 0, 0))
    WIN.blit(upgradeCostText, (720, 190))

    clickerCostText = FONT.render("Cost to Purchase Clicker: " + str(clickerCost), False, (0, 0, 0))
    WIN.blit(clickerCostText, (720, 460))

    clickersinfoText1 = FONTsmall.render("Purchase clicker to auto click", False, (0, 0, 0))
    WIN.blit(clickersinfoText1, (720, 400))

    clickersinfoText2 = FONTsmall.render("cookies for you ever second", False, (0, 0, 0))
    WIN.blit(clickersinfoText2, (718, 430))

    highScoreText = FONT.render("High Score: " + str(highScore), False, (0, 0, 0))
    WIN.blit(highScoreText, (10, 685))

    clickersPurchasedText = FONT.render("Clickers Purchased: " + str(clickersPurchased), False, (0, 0, 0))
    WIN.blit(clickersPurchasedText, (750, 540))

    cpsText = FONTsmall.render("Cookies Per Second: " + str(cps), False, (0, 0, 0))
    WIN.blit(cpsText, (200, 150))

    cookiesPerClickText = FONTsmall.render("Cookies Per Click: " + str(cookiesPerClick), False, (0, 0, 0))
    WIN.blit(cookiesPerClickText, (215, 100))


def update_balances():
    global cookieBalance
    global highScore
    global cookiesPerClick
    global upgradeCost
    global clickerCost
    global cps

    cps = round(0.1 * clickersPurchased, 2)

    if pygame.event.get(second):
        cookieBalance = round((cookieBalance + cps), 2)

    cookiesPerClick = upgradesPurchased + 1

    if cookieBalance > highScore:
        highScore = round(cookieBalance, 2)

    if upgradesPurchased == 0:
        upgradeCost = 10
    else:
        upgradeCost = upgradesPurchased * 23 + 10
    clickerCost = 3 * (clickersPurchased + 1)


def draw_window():
    global cookieBalance
    global upgradesPurchased
    global clickersPurchased
    """Draws all graphics each frame"""
    WIN.fill(PALE_BLUE)
    gameText()

    if cookieButton.drawRotate(-0.5):
        cookieBalance = round((cookieBalance + cookiesPerClick), 2)
    if upgradeButton.draw() and cookieBalance >= upgradeCost:
        upgradesPurchased += 1
        cookieBalance = round((cookieBalance - upgradeCost), 2)
    if clickerButton.draw() and cookieBalance >= clickerCost:
        clickersPurchased += 1
        cookieBalance = round((cookieBalance - clickerCost), 2)

    pygame.display.update()


def main():
    """Main game function"""
    run = True
    while run:
        CLOCK.tick(FPS)
        update_balances()
        draw_window()

        # Event handler
        for event in pygame.event.get():

            # Quit game
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


# Will only run main() from this file
if __name__ == "__main__":
    main()
