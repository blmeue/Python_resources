import pytest
import pygame
from alien import Alien


class MockAIGame:
    """ Mocking the ai_game object that is expected to be passed to Alien"""
    def __init__(self, screen, settings):
        """初始化"""
        self.screen = screen
        self.settings = settings

class MockSettings:
    """ Mocking the settings object that is expected to be passed to Alien"""
    def __init__(self, alien_speed, fleet_direction):
        """初始化"""
        self.alien_speed = alien_speed
        self.fleet_direction = fleet_direction

@pytest.fixture
def ai_game():
    """ 返回一个mock的ai_game对象"""
    screen = pygame.display.set_mode((800, 600))
    settings = MockSettings(alien_speed=1.0, fleet_direction=1)
    return MockAIGame(screen, settings)

@pytest.mark.parametrize("alien_speed, fleet_direction, expected_x", [
    # ID: HappyPath-MovingRight
    (1.0, 1, 31.0),
    # ID: HappyPath-MovingLeft
    (1.0, -1, 29.0),
])
def test_alien_update(ai_game, alien_speed, fleet_direction, expected_x):
    """测试Alien类的update"""
    # Arrange
    ai_game.settings.alien_speed = alien_speed
    ai_game.settings.fleet_direction = fleet_direction
    alien = Alien(ai_game)
    alien.x = 30.0  # Starting from 30 for testing

    # Act
    alien.update()

    # Assert
    assert alien.x == expected_x
    assert alien.rect.x == int(expected_x)

@pytest.mark.parametrize("alien_position, fleet_direction, expected", [
    # ID: HappyPath-NotAtEdge
    ((100, 100), 1, False),
    # ID: EdgeCase-AtRightEdge
    ((770, 100), 1, True),
])
def test_alien_check_edges(ai_game, alien_position, fleet_direction, expected):
    """测试Alien类的_check_edges"""
    # Arrange
    ai_game.settings.fleet_direction = fleet_direction
    alien = Alien(ai_game)
    alien.rect.x, alien.rect.y = alien_position

    # Act
    at_edge = alien.check_edges()

    # Assert
    assert at_edge == expected
