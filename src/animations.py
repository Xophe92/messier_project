# https://drive.google.com/drive/folders/0BwDJQBs1OukNaDMtVG9JU2M1cjA


from platform import python_version
print(python_version())

import pygame
from pygame.locals import *


# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

# define display surface
W, H = 640, 480
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Sprite Sheets")
FPS = 30

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

class Spritesheet:
    def __init__(self, filename, cols, rows):
        self.sheet = pygame.image.load(filename).convert_alpha()

        self.cols = cols
        self.rows = rows
        self.totalCellCount = cols * rows

        self.rect = self.sheet.get_rect()
        w = self.cellWidth = self.rect.width / cols
        h = self.cellHeight = self.rect.height / rows
        hw, hh = self.cellCenter = (w / 2, h / 2)

        self.cells = list([(index % cols * w, index // cols * h, w, h) for index in range(self.totalCellCount)])
        self.handle = list([
            (0, 0), (-hw, 0), (-w, 0),
            (0, -hh), (-hw, -hh), (-w, -hh),
            (0, -h), (-hw, -h), (-w, -h), ])

    def draw(self, surface, cell_index, x, y, handle=0):
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cell_index])


s = Spritesheet("../assets/Catalog.jpg", 10, 11)

index = 0

CENTER_HANDLE = 4

while True:
    events()

    s.draw(DS, index % s.totalCellCount, index*5 % W, index*5 % H, CENTER_HANDLE)
    index += 1


    pygame.display.update()
    CLOCK.tick(FPS)
    #DS.fill(BLACK)