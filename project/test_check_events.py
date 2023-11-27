from alien_invasion import AlienInvasion
import pygame 
import pytest
import sys

def test_keydown_event_moving_right():
    """测试按键按下向右键事件的处理"""
    ai_game=AlienInvasion()
    event=pygame.event.Event(pygame.KEYDOWN,key=pygame.K_RIGHT)
    ai_game._check_keydown_events(event)
    
    #在这里添加断言来检查按键事件的处理逻辑是否符合预期
    assert ai_game.ship.moving_right is True
    
def test_keydown_event_moving_left():
    """测试按键按下向左键事件的处理"""
    ai_game=AlienInvasion()
    event=pygame.event.Event(pygame.KEYDOWN,key=pygame.K_LEFT)
    ai_game._check_keydown_events(event)
    
    #在这里添加断言来检查按键事件的处理逻辑是否符合预期
    assert ai_game.ship.moving_left is True
