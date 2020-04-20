# -*-coding:utf-8-*-
import pygame
from pygame.locals import *
import sys, random

SCR = Rect(0, 0, 300, 500)


class Main:
    def __init__(self):
        # pygame起動
        pygame.init()
        pygame.mixer.init()
        # 基本設定
        pygame.display.set_caption("I'ts a Shooting Game")
        self.screen = pygame.display.set_mode(SCR.size)
        self.clock = pygame.time.Clock()
        self.enemy_prob = 60

        # 画像読み込み、スプライト管理
        self.bg = pygame.image.load("Textures/background.jpg").convert_alpha()
        self.bg_rect = self.bg.get_rect()
        Player.image = pygame.image.load("Textures/player.png")
        Enemy1.image = pygame.image.load("Textures/enemy1.png")
        Bullet1.image = pygame.image.load("Textures/bullet1.png")
        self.all_sprite = pygame.sprite.RenderUpdates()
        self.player = pygame.sprite.Group()
        self.enemy1 = pygame.sprite.Group()
        self.bullet1 = pygame.sprite.Group()
        Player.containers = self.all_sprite, self.player
        Enemy1.containers = self.all_sprite, self.enemy1
        Bullet1.containers = self.all_sprite, self.bullet1

        # BGMを再生
        pygame.mixer.music.load("Audio/bgm_maoudamashii_orchestra15.ogg")
        pygame.mixer.music.play(-1)

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
        if not random.randrange(self.enemy_prob):
            Enemy1()
        self.all_sprite.update()
        self.collision_detection()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, self.bg_rect)
        self.all_sprite.draw(self.screen)

    # キーイベントによる処理
    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.mixer.music.stop()
                pygame.quit()
                sys.exit()

    def collision_detection(self):
        x = 1


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        self.rect.bottom = SCR.bottom  # プレイヤーは画面の一番下からスタート
        self.rect.left = (SCR.width - self.rect.width) // 2
        self.speed = 4

    def update(self):
        # playerの動作
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


class Enemy1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        self.rect.center = (150, 0)  # プレイヤーは画面の一番下からスタート
        self.speed = 5

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCR.height:
            self.kill()


class Bullet1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()


if __name__ == '__main__':
    Main()
