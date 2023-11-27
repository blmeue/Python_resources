from alien_invasion import AlienInvasion
import pygame 
import pytest
import sys

def test_keyup_event_moving_right():
    """测试按键松开向右键事件的处理"""
    ai_game=AlienInvasion()
    event=pygame.event.Event(pygame.KEYUP,key=pygame.K_RIGHT)
    ai_game._check_keyup_events(event)
    
    #在这里添加断言来检查按键事件的处理逻辑是否符合预期
    assert ai_game.ship.moving_right is False
    
def test_keyup_event_moving_left():
    """测试按键松开向左键事件的处理"""
    ai_game=AlienInvasion()
    event=pygame.event.Event(pygame.KEYUP,key=pygame.K_LEFT)
    ai_game._check_keyup_events(event)
    
    #在这里添加断言来检查按键事件的处理逻辑是否符合预期
    assert ai_game.ship.moving_left is False
