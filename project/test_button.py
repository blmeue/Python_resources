import pytest
import pygame
from button import Button

# Mocking the necessary pygame initializations
@pytest.fixture(scope="module", autouse=True)
def pygame_init():
    """初始化"""
    pygame.init()
    pygame.display.set_mode((800, 600))

# Mocking a game class with a screen attribute
class MockGame:
    """创建MockGame类"""
    def __init__(self):
        self.screen = pygame.display.get_surface()

@pytest.mark.parametrize("msg, expected", [
    pytest.param("Play", (0, 135, 0), id="happy-path-play-button"),
    pytest.param("Quit", (0, 135, 0), id="happy-path-quit-button"),
])
def test_button_creation(msg, expected):
    """测试按键的创建"""
    # Arrange
    ai_game = MockGame()

    # Act
    button = Button(ai_game, msg)

    # Assert
    assert button.msg_image is not None
    assert button.rect.width == 200
    assert button.rect.height == 50
    assert button.button_color == expected

@pytest.mark.parametrize("msg, color, font_size", [
    pytest.param("Play", (255, 0, 0), 48, id="happy-path-different-color"),
    pytest.param("Quit", (0, 255, 0), 36, id="happy-path-different-font-size"),
])
def test_button_visuals(msg, color, font_size):
    """测试按键的可视化"""
    # Arrange
    ai_game = MockGame()
    button = Button(ai_game, msg)
    button.button_color = color
    button.font = pygame.font.SysFont(None, font_size)
    button._prep_msg(msg)

    # Act
    button.draw_button()

    # Assert
    assert button.msg_image_rect.center == button.rect.center
    assert button.msg_image.get_width() > 0
    assert button.msg_image.get_height() > 0

