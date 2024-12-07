#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        if not hasattr(self, 'movimento'):
            self.movimento = 0
        if self.name == 'Enemy3':
            self.rect.centerx -= ENTITY_SPEED[self.name]

            if self.movimento == 0:
                if self.rect.centery < 304:
                    self.rect.centery += ENTITY_SPEED[self.name] + ENTITY_SPEED[self.name]
                else:
                    self.movimento = 1

            elif self.movimento == 1:
                if self.rect.centery > 20:
                    self.rect.centery -= ENTITY_SPEED[self.name]
                else:
                    self.movimento = 0
        else:
            self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
