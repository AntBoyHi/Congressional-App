import random
import pygame
import sys
import time
#___________________________________
Start = pygame.event.get
pygame.init()
pygame.font.init()
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont("merriweather", 30)
reasofont = pygame.font.SysFont("merriweather", 20)
responsefont = pygame.font.SysFont("merriweather", 50)
pygame.display.set_caption("... ___ ...")
active = True
choice = random.randint(0, 2)
rise = False
guess = True

SMP = 42931.6
DOW = 5853.98
NASDAQ = 20174.05

print(f"SMP: {SMP} points \nDOW: {DOW} points \nNASDAQ: {NASDAQ} points")

perc = random.randrange(95, 105) / 100
perc2 = random.randrange(95, 105) / 100
perc3 = random.randrange(95, 105) / 100

print(f"\n{perc}\n{perc2}\n{perc3}")

human = ["SMP", "DOW", "NASDAQ"]
man = [SMP, DOW, NASDAQ]
woman = [perc, perc2, perc3]
between = [round(SMP*perc, 2), round(DOW*perc2, 2), round(NASDAQ*perc3, 2)]
print(f"\n{between[0]}\n{between[1]}\n{between[2]}")

bdt = [
    "Corporate scandal enrages public, ", 
    "Reliable CEO of major conglomerate steps down, public antsy about replacement. ",
    "A viral piece of media leaves a companies reputation in pieces, "
]
sdt = [
    "Stockholders get cold feet, ", 
    "Accident in the industry leaves many shaken, ",
    "Reputable economists claim a bear market soon, "
]
sut = [
    "Major technology breakthrough increase productivity, ",
    "Government expands financial programs, ",
    "Government lowers interest rates, "
]
but = [
    "Government passes laws to protect againsteconomic downturns, public hopeful. ", 
    "Conglomerate extensively increasing manpower, stimulating workforce. ",
    "New international trade deals revitalize struggling industries, "
]

#_________________________________________________________________________________________________________


def draw_button(screen, text, x, y, width, height, inactive_color,
                active_color):
  mouse = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()

  if x < mouse[0] < x + width and y < mouse[1] < y + height and active:
    pygame.draw.rect(screen, active_color, (x, y, width, height))
    if click[0] == 1:  
      return True
  else:
    pygame.draw.rect(screen, inactive_color, (x, y, width, height))

  text_surface = font.render(text, True, (0, 0, 0))
  screen.blit(text_surface, (x + (width - text_surface.get_width()) // 2, y +
                             (height - text_surface.get_height()) // 2))

  return False


def draw_text(screen, text, x, y, width, height, color):

  pygame.draw.rect(screen, color, (x, y, width, height), 0, 1, 1, 1, 1, 1)

  text_surface = reasofont.render(text, True, (0, 0, 0))
  screen.blit(text_surface, (x + (width - text_surface.get_width()) // 2, y +
                             (height - text_surface.get_height()) // 2))

  return False

def respond(screen, text, x, y, width, height, color):

  pygame.draw.rect(screen, color, (x, y, width, height))

  text_surface = responsefont.render(text, True, (255, 255, 255))
  screen.blit(text_surface, (x + (width - text_surface.get_width()) // 2, y +
                           (height - text_surface.get_height()) // 2))

  return False


def stonkchooser(e):
  return man[e]


def stonkperc(e):
  return woman[e]

def stonktrue(change):
  w = False
  if change < 1.00:
    if change <= 0.97:
      w = False
    elif change >= 0.98:
      w = False
  elif change > 1.00:
    if change >= 1.03:
      w = True
    elif change <= 1.02:
      w = True
  return w

def support_diff(e):
  return f"{man[e]} --> {between[e]}"


custom = "null"


def headline(mess, stock, custom):
  return (mess[random.randint(0, 2)] + stock + custom)


def analyze(change, stock, num):
  if change < 1.00:
    if change <= 0.97:
      custom = f" {support_diff(num)}"
      bor = headline(bdt, stock, custom)  #goo
    elif change >= 0.98:
      custom = f" {support_diff(num)}"
      bor = headline(sdt, stock, custom)
  elif change > 1.00:
    if change >= 1.03:
      custom = f" {support_diff(num)}"
      bor = headline(but, stock, custom)
    elif change <= 1.02:
      custom = f" {support_diff(num)}"
      bor = headline(sut, stock, custom)
  else:
    print(change)
    bor = f"A calm peaceful day for {stock}. {support_diff(num)}"
  return (bor)


#_________________________________________________________________________________________________________
reaso = analyze(stonkperc(choice), f" {human[choice]}", choice)
rise = stonktrue(stonkperc(choice))
print(reaso)
running = True
show = 1000
ye = "I failed at coding if you're seeing this words on the screen, suck it"
while running:
  screen.fill((60, 60, 60))

  draw_text(screen, reaso, 50, 50, 700, 100, (200, 200, 200))

  if show < 1000:
    respond(screen, ye, 50, 250, 700, 100, (60, 60, 60))
    show += 1

  # Draw the button
  if draw_button(screen, 'Rises', 200, 200, 140, 50, (0, 200, 0), (0, 55, 0)):
    print('Yipee')
    active = False
    guess = True

  if draw_button(screen, 'Falls', 460, 200, 140, 50, (200, 0, 0), (55, 0, 0)):
    print('Boo')
    active = False
    guess = False

  if not active:
    print(guess)
    print(rise)
    if guess == rise:
      ye = "Correct"
    else:
      ye = "Failure"
    perc = random.randrange(95, 105) / 100
    perc2 = random.randrange(95, 105) / 100
    perc3 = random.randrange(95, 105) / 100
    woman = [perc, perc2, perc3]
    man = [between[0], between[1], between[2]]
    between = [round(SMP*perc, 2), round(DOW*perc2, 2), round(NASDAQ*perc3, 2)]
    choice = 2 #random.randint(0, 2)
    reaso = analyze(stonkperc(choice), f" {human[choice]}", choice)
    rise = stonktrue(stonkperc(choice))
    time.sleep(.5)
    active = True
    show = 0;

  # Event handling
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
#______________________________________________________________________________________________________
