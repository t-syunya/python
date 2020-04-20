# -*-coding:utf-8-*-
import pygame
from pygame.locals import *
import sys

SCR = Rect(0, 0, 300, 500)


class Main:
    def __init__(self):
        # pygame起動
        pygame.init()
        # 基本設定
        pygame.display.set_caption("I'ts a Shooting Game")
        self.screen = pygame.display.set_mode(SCR.size)
        self.clock = pygame.time.Clock()

        # 画像読み込み、スプライト管理
        self.bg = pygame.image.load("background.jpg").convert_alpha()
        self.bg_rect = self.bg.get_rect()
        Player.image = pygame.image.load("player.png")
        self.all_sprite = pygame.sprite.RenderUpdates()
        self.player = pygame.sprite.Group()
        Player.containers = self.all_sprite, self.player

        # ループ開始
        Player()
        self.main()

    def main(self):
        while True:
            self.clock.tick(60)
            self.update()
            self.draw()
            pygame.display.update()
            self.key_handler()

    def update(self):
        self.all_sprite.update()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, self.bg_rect)
        self.all_sprite.draw(self.screen)

    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()


# class Enemy:
#   def __init__(self):

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        self.rect.bottom = SCR.bottom  # プレイヤーは画面の一番下からスタート
        self.rect.left = (SCR.width - self.rect.width) // 2
        self.speed = 5

    def update(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if pressed_key[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if pressed_key[K_UP]:
            self.rect.move_ip(0, -self.speed)
        if pressed_key[K_DOWN]:
            self.rect.move_ip(0, self.speed)
        # 画面からはみ出さないようにする
        self.rect = self.rect.clamp(SCR)


if __name__ == '__main__':
    Main()
