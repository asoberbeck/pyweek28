#!/usr/bin/env python

import random
import pygame.display
import pygame.font
import pygame.time

class Movable(object): 
    pass

class PlayerTower(object):
    pass

class Enemy(object):
    def __init__(self): 
        self.enemy = pygame.rect.Rect(100, 100, 10, 10)    

class Zeppelin(object):
    pass

class GameWorld(object):
    def __init__(self):
        self.game_time_s = 0

    def update(self, delta_t):
        self.game_time_s += delta_t

    def format_time(self, time_s=None):
        if time_s is None:
            time_s = self.game_time_s
        return '%02d:%02d' % (time_s // 60, time_s % 60)

class PygameUserInterface(object):
    def __init__(self):
        self.game_exit = False
        self.surface = pygame.display.get_surface()
        self.clock = pygame.time.Clock() # https://www.pygame.org/docs/ref/time.html
        self.desired_fps = 30
        self.font = pygame.font.Font(None, 30) # https://www.pygame.org/docs/ref/font.html
        self.game_world = GameWorld()

        # demo stuff
        self.desired_color = (0, 0, 0)
        self.keys_letter = [0, 0]
        self.mouse_letter = [0, 0] # drag letter with cursor TODO-1 
        #self.enemy = Enemy()

    def frame_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_exit = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # https://www.pygame.org/docs/ref/surface.html
                    self.desired_color = (random.randrange(255), random.randrange(255), random.randrange(255))
                elif event.key == pygame.K_UP:
                    self.keys_letter[1] -= 1
                    # self.enemy.move_ip(5, 0)
                elif event.key == pygame.K_DOWN:
                    self.keys_letter[1] += 1
                elif event.key == pygame.K_LEFT:
                    self.keys_letter[0] -= 1
                elif event.key == pygame.K_RIGHT:
                    self.keys_letter[0] += 1
            elif event.type == pygame.MOUSEMOTION:
                #TODO-1 
                self.mouse_letter = event.pos
        pressed_keys = pygame.key.get_pressed()
        # if pressed_keys[pygame.K_q]:
        #     stuff_when_q_pressed_and_held()

    def frame_logic(self):
        self.game_world.update(1/self.desired_fps)

    def frame_graphics(self):
        self.surface.fill(self.desired_color)
        max_row, max_column = self.surface.get_size()
        letter_surface = self.font.render('L', True, (255, 255, 255))
        # https://www.pygame.org/docs/ref/surface.html
        self.surface.blit(letter_surface, self.keys_letter)
        mouse_surface = self.font.render('M', True, (255, 255, 255))
        self.surface.blit(mouse_surface, self.mouse_letter)

        # draw map objects

        # draw overlaid text
        time_surface = self.font.render(self.game_world.format_time(),
                                        True,
                                        (255, 255, 255))
        self.surface.blit(time_surface, (max_row/2 - time_surface.get_width()/2,
                                         max_column/2 - time_surface.get_height()/2))

        pygame.display.flip()

    def main_loop(self):
        while self.game_exit is False:
            self.frame_events()
            self.frame_logic()
            self.frame_graphics()
            self.clock.tick(self.desired_fps)

def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_mode((640, 480))
    ui = PygameUserInterface()
    ui.main_loop()
    pygame.quit()

if __name__ == '__main__':
    main()
