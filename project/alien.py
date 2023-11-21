import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """表示单个外星人并设置其初始位置"""
    
    def __int__(self,ai_game):
        """初始化外星人并设置其初始位置"""
        super().__init__()
        self.screen = ai_game.screen
        
        #加载