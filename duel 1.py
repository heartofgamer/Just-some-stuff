import pygame
import os
import random
import math
'''                     Player1                   Player2
               
Movement            WASD                      Arrow-keys
Gun                 SPACE                     right-ctrl
Launch missile      left-shift                right-shift
Detonate missile    left-shift                right-shift'''


def initPygame():
    global window, BLACK, ORANGE, WHITE, RED, GREEN, BLUE, GRAY, PURPLE, YELLOW, font, windowWidth, windowHeight
    print("initializing..."),

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    windowWidth = 700
    windowHeight = 600
    window = pygame.display.set_mode((windowWidth, windowHeight), 0, 32)
    pygame.display.set_caption('* DUEL GUNGAME *')
    GRAY = (100, 100, 100)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)
    RED = (255, 0, 0)
    PURPLE = (128, 0, 128)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    ORANGE = (255, 100, 0)
    font = pygame.font.SysFont(None, 24)
    print("done")



class Player:
    def __init__(self, name, x, y, color, movementKeys, shootKey, missileKey, direction):
        self.name = name
        self.maxHp = 15
        self.hp = self.maxHp
        self.x = x
        self.y = y
        self.w = 50
        self.h = 50
        self.color = color
        self.movementKeys = movementKeys
        self.shootKey = shootKey
        self.missileKey = missileKey
        self.shooting = False
        self.shootingMissile = False
        self.moveKeysDown = []
        self.direction = direction
        self.moveSpeed = 1.6
        self.gunPos = (
        self.x + self.w / 2 + self.direction[0] * self.w / 4, self.y + self.h / 2 + self.direction[1] * self.h / 4)
        self.shootCooldown = 200
        self.missileCooldown = 1500
        self.cooldownLeft = 0
        self.bulletSpeed = 4
        self.bulletRadius = 4
        self.powerup = None
        self.timeUntilLosePowerup = 0
        self.enemy = None
        self.missile = None
        self.maxMissiles = 3
        self.numMissiles = self.maxMissiles
        self.timeUntilNextMissile = 5000

    def gainPowerup(self, powerup):
        self.losePowerup()
        self.powerup = powerup
        powerupSound.play()
        if powerup.type == "SPEED":
            self.moveSpeed = self.moveSpeed * powerup.multiplier
            self.timeUntilLosePowerup = powerup.duration;
        elif powerup.type == "HP":
            self.gainHp(3)
        elif powerup.type == "ATKSPEED":
            self.shootCooldown *= powerup.multiplier
            self.timeUntilLosePowerup = powerup.duration
        elif powerup.type == "AIM":
            self.timeUntilLosePowerup = powerup.duration
        elif powerup.type == "DEATH":
            spawnDeathBullet(self)

    def losePowerup(self):

        if self.powerup != None:
            if self.powerup.type == "SPEED":
                self.moveSpeed = self.moveSpeed / self.powerup.multiplier
            elif self.powerup.type == "ATKSPEED":
                self.shootCooldown /= self.powerup.multiplier
        self.timeUntilLosePowerup = 0
        self.powerup = None

    def draw(self):
        rect = (self.x, self.y, self.w, self.h)
        pygame.draw.rect(window, self.color, rect)
        pygame.draw.circle(window, BLACK, self.gunPos, 5)
        if self.powerup != None:
            powerupRect = (self.x - 4, self.y - 4, self.w + 8, self.h + 8)
            pygame.draw.rect(window, self.powerup.color, powerupRect, 4)
        if self.missile != None:
            self.missile.draw()

    def move(self, dx, dy):
        dx *= self.moveSpeed
        dy *= self.moveSpeed
        if self.x + dx > 0 and self.x + self.w + dx < windowWidth and self.y + dy > 20 and self.y + self.h + dy < windowHeight:
            self.x += dx
            self.y += dy
            self.gunPos = (int(self.x + self.w / 2 + self.direction[0] * self.w / 4),
                           int(self.y + self.h / 2 + self.direction[1] * self.h / 4))
            self.x = int(self.x)
            self.y = int(self.y)

    def update(self, dt):
        self.timeUntilNextMissile -= dt
        if self.timeUntilNextMissile <= 0:
            self.numMissiles = min(self.maxMissiles, self.numMissiles + 1)
            self.timeUntilNextMissile = 5000
        if self.powerup != None:
            self.timeUntilLosePowerup -= dt
            if self.timeUntilLosePowerup <= 0:
                self.losePowerup()
        self.cooldownLeft -= dt
        key = getLast(self.moveKeysDown)
        if self.missile != None:
            self.missile.update(dt)
        # if self.missile != None and key in self.movementKeys:
        # 	self.missile.move(self.movementKeys[key][0]*self.moveSpeed*3, self.movementKeys[key][1]*self.moveSpeed*3)
        # 	self.missile.direction = self.movementKeys[key]
        if self.cooldownLeft <= 0:
            if key in self.movementKeys:
                if self.missile == None:
                    self.move(self.movementKeys[key][0] * self.moveSpeed, self.movementKeys[key][1] * self.moveSpeed)
                    self.direction = self.movementKeys[key]
            if self.shooting and self.missile == None:
                self.shoot()
            if self.shootingMissile:
                if self.missile == None:
                    if self.numMissiles > 0:
                        self.shootMissile()
                        self.numMissiles -= 1

                else:
                    self.missile.explode()
                    self.missile = None
                self.shootingMissile = False

    def loseHp(self, amount):
        global running, winner
        self.hp -= amount
        hurtSound.play()
        if self.hp <= 0:
            winner = self.enemy
            running = False

    def gainHp(self, amount):
        self.hp = min(self.hp + amount, self.maxHp)

    def shootMissile(self):
        self.missile = SeekerMissile(self.gunPos[0], self.gunPos[1], self, self.direction)

    def shoot(self):
        bulletRandomness = 0.01
        shootSound.play()
        if (self.powerup != None and self.powerup.type == "AIM"):
            direction = directionBetween([self.x, self.y], [self.enemy.x, self.enemy.y])
        else:
            direction = list(self.direction)
        bullet = Bullet(self.gunPos[0], self.gunPos[1], self.color, self.bulletRadius, direction, self.bulletSpeed,
                        self, bulletRandomness)
        bullets.append(bullet)
        self.cooldownLeft = self.shootCooldown


class Bullet:
    def __init__(self, x, y, color, radius, direction, speed, player, randomness):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.direction = direction
        self.speed = speed
        self.player = player
        self.randomness = randomness

    def update(self, dt):
        self.direction[0] += (random.random() - 0.5) * self.randomness * dt
        self.direction[1] += (random.random() - 0.5) * self.randomness * dt
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed

    def checkCollisions(self):
        r = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        if self.x < 0 or self.x > windowWidth or self.y < 0 or self.y > windowHeight:
            bullets.remove(self)
            return
        for player in players:
            if player != self.player:
                playerR = pygame.Rect(player.x, player.y, player.w, player.h)
                if r.colliderect(playerR):
                    bullets.remove(self)
                    player.loseHp(1)

    def draw(self):
        pygame.draw.circle(window, BLACK, (int(self.x), int(self.y)), self.radius)


class Powerup:
    def __init__(self, x, y, color, powerupType):
        self.x = x
        self.y = y
        self.color = color
        self.type = powerupType
        self.radius = 12
        if self.type == "SPEED":
            self.multiplier = 1.3
        elif self.type == "ATKSPEED":
            self.multiplier = 0.5
        self.duration = 2000

    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

    def checkCollisions(self):
        for player in players:
            if pygame.Rect(player.x, player.y, player.w, player.h).collidepoint((self.x, self.y)):
                powerups.remove(self)
                player.gainPowerup(self)


class SeekerMissile:
    def __init__(self, x, y, player, direction):
        self.x = x
        self.y = y
        self.player = player
        self.direction = direction

    def draw(self):
        pygame.draw.circle(window, ORANGE, (int(self.x), int(self.y)), 5)

    def update(self, dt):
        self.x += self.direction[0] * dt * 0.6
        self.y += self.direction[1] * dt * 0.6

    def explode(self):
        explRadius = 120
        drawables.append(DrawCircle(self.x, self.y, explRadius, WHITE, 80))
        dist = math.hypot(self.player.enemy.x - self.x, self.player.enemy.y - self.y)
        if dist < explRadius:
            self.player.enemy.loseHp(3)


class DrawCircle:
    def __init__(self, x, y, radius, color, duration):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.timeLeft = duration

    def update(self, dt):
        self.timeLeft -= dt
        if self.timeLeft <= 0:
            drawables.remove(self)

    def draw(self):
        pygame.draw.circle(window, self.color, (int(self.x), int(self.y)), self.radius)


def drawInterface():
    for player_i, player in enumerate(players):
        for i in range(player.maxHp):
            w = 16
            h = 20
            y = 5
            x = 20 + player_i * windowWidth / 2 + i * (w + 6)
            frame = 2
            if i < player.hp:
                pygame.draw.rect(window, player.color, [x, y, w, h])
            pygame.draw.rect(window, BLACK, [x - frame, y - frame, w + frame * 2, h + frame * 2], frame)
        for i in range(player.maxMissiles):
            w = 16
            h = 20
            y = 35
            x = 20 + player_i * windowWidth / 2 + i * (w + 6)
            frame = 2
            if i < player.numMissiles:
                pygame.draw.rect(window, ORANGE, [x, y, w, h])
            pygame.draw.rect(window, BLACK, [x - frame, y - frame, w + frame * 2, h + frame * 2], frame)

        text = player.name + "  " + str(player.hp) + " / " + str(player.maxHp)
        label = font.render(text, 1, WHITE)
        window.blit(label, (170 + i * windowWidth / 2, 10))


def getInput():
    events = pygame.event.get()
    for event in events:
        for player in players:
            if event.type == pygame.KEYDOWN:
                if event.key in player.movementKeys:
                    player.moveKeysDown.append(event.key)
                elif event.key == player.shootKey:
                    player.shooting = True
                elif event.key == player.missileKey:
                    player.shootingMissile = True
            elif event.type == pygame.KEYUP:
                if event.key in player.movementKeys:
                    player.moveKeysDown.remove(event.key)
                elif event.key == player.shootKey:
                    player.shooting = False

        if event.type == pygame.KEYDOWN and event.key in globalKeys:
            globalKeysDown.append(event.key)
        elif event.type == pygame.KEYUP and event.key in globalKeys:
            globalKeysDown.remove(event.key)


def getLast(list):
    if len(list) > 0:
        return list[-1]
    return None


def pressedQuit():
    if getLast(globalKeysDown) == pygame.K_ESCAPE:
        print
        "Pressed ESC. Quitting ..."
        return True
    return False


def spawnPowerup():
    x = int(random.random() * windowWidth)
    y = 20 + int(random.random() * (windowHeight - 20))
    r = random.random()
    if len(powerups) >= 3:
        return
    if r < 0.2:
        powerup = Powerup(x, y, GREEN, "HP")
    elif r < 0.4:
        powerup = Powerup(x, y, YELLOW, "ATKSPEED")
    elif r < 0.6:
        powerup = Powerup(x, y, PURPLE, "SPEED")
    elif r < 0.8:
        powerup = Powerup(x, y, WHITE, "AIM")
    else:
        powerup = Powerup(x, y, BLACK, "DEATH")
    powerups.append(powerup)


def gameLoop():
    global prevTime, timeUntilPowerup
    dt = pygame.time.get_ticks() - prevTime

    getInput()
    if running:
        timeUntilPowerup -= dt
        if timeUntilPowerup <= 0:
            spawnPowerup()
            timeUntilPowerup = 1500 + random.random() * 3000
        for player in players:
            player.update(dt)
        for bullet in bullets:
            bullet.update(dt)
        for drawable in drawables:
            drawable.update(dt)
        for bullet in bullets:
            bullet.checkCollisions()
        for powerup in powerups:
            powerup.checkCollisions()

        window.fill(GRAY)
        for player in players:
            player.draw()
        for bullet in bullets:
            bullet.draw()
        for powerup in powerups:
            powerup.draw()
        for drawable in drawables:
            drawable.draw()
        drawInterface()
        pygame.display.update()
        prevTime = pygame.time.get_ticks()
        pygame.time.wait(10)
    else:
        window.fill(BLACK)
        text = winner.name + " won! Press RETURN to start game."
        label = font.render(text, 1, WHITE)
        window.blit(label, (windowWidth / 2 - 130, 300))
        pygame.display.update()
        if getLast(globalKeysDown) == pygame.K_RETURN:
            start()
    return pressedQuit()


def initGame():
    global p1Movement, p2Movement, globalKeysDown, globalKeys, shootSound, powerupSound, hurtSound
    p1Movement = {
        pygame.K_a: [-1, 0],
        pygame.K_d: [1, 0],
        pygame.K_s: [0, 1],
        pygame.K_w: [0, -1]
    }
    p2Movement = {
        pygame.K_LEFT: [-1, 0],
        pygame.K_RIGHT: [1, 0],
        pygame.K_DOWN: [0, 1],
        pygame.K_UP: [0, -1]
    }
    globalKeys = [pygame.K_ESCAPE, pygame.K_RETURN]
    globalKeysDown = []
    shootSound = pygame.mixer.Sound("shoot.mp3")
    powerupSound = pygame.mixer.Sound("powerup.mp3")
    hurtSound = pygame.mixer.Sound("hurt.mp3")


def directionBetween(point1, point2):
    direction = [point2[0] - point1[0], point2[1] - point1[1]]
    vecLen = math.sqrt(math.pow(direction[0], 2) + math.pow(direction[1], 2))
    direction[0] /= vecLen
    direction[1] /= vecLen
    return direction


def spawnDeathBullet(player):
    direction = directionBetween([player.x, player.y], [player.enemy.x, player.enemy.y])
    deathBullet = Bullet(player.gunPos[0], player.gunPos[1], BLACK, 30, direction, 1.9, player, 0.005)
    bullets.append(deathBullet)


def start():
    global p1, p2, players, bullets, prevTime, running, timeUntilPowerup, powerups, drawables
    prevTime = pygame.time.get_ticks()
    running = True
    p1 = Player("Blue", 200, 400, BLUE, p1Movement, pygame.K_SPACE, pygame.K_LSHIFT, [1, 0])
    p2 = Player("Red", 500, 400, RED, p2Movement, pygame.K_RCTRL, pygame.K_RSHIFT, [-1, 0])
    p1.enemy = p2
    p2.enemy = p1
    players = [p1, p2]
    bullets = []
    powerups = []
    drawables = []
    timeUntilPowerup = 2000 + random.random() * 2000


initPygame()
initGame()
start()
while True:
    quit = gameLoop()
    if (quit):
        break