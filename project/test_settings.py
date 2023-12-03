import pytest
from settings import Settings

# Test initialization of Settings
@pytest.mark.parametrize("test_id", [1])
def test_settings_initialization(test_id):
    """测试settings类的初始化"""
    # Act
    settings = Settings()

    # Assert
    assert settings.screen_width == 1200
    assert settings.screen_height == 800
    assert settings.bg_color == (255, 255, 255)
    assert settings.ship_limit == 3
    assert settings.bullet_width == 3
    assert settings.bullet_height == 15
    assert settings.bullet_color == (60, 60, 60)
    assert settings.bullets_allowed == 3
    assert settings.fleet_drop_speed == 10
    assert settings.speedup_scale == 1.1
    assert settings.score_scale == 1.5
    assert settings.ship_speed == 1.5
    assert settings.bullet_speed == 2.5
    assert settings.alien_speed == 1.0
    assert settings.fleet_direction == 1
    assert settings.alien_points == 50

# Test initialize_dynamic_settings method
@pytest.mark.parametrize("test_id", [5])
def test_initialize_dynamic_settings(test_id):
    """测试settings类的initialize_dynamic_settings 方法"""
    # Arrange
    settings = Settings()
    settings.ship_speed = 0
    settings.bullet_speed = 0
    settings.alien_speed = 0
    settings.fleet_direction = 0

    # Act
    settings.initialize_dynamic_settings()

    # Assert
    assert settings.ship_speed == 1.5
    assert settings.bullet_speed == 2.5
    assert settings.alien_speed == 1.0
    assert settings.fleet_direction == 1
    
# Test increase_speed method
@pytest.mark.parametrize("test_id, speedup_scale, score_scale, expected_ship_speed, expected_bullet_speed, expected_alien_speed, expected_alien_points", [
    (4, 0.5, 0.5, 0.75, 1.25, 0.5, 25),
])
def test_increase_speed(test_id, speedup_scale, score_scale, expected_ship_speed, expected_bullet_speed, expected_alien_speed, expected_alien_points, capsys):
    """测试settings类的 increase_speed 方法"""
    # Arrange
    settings = Settings()
    settings.speedup_scale = speedup_scale
    settings.score_scale = score_scale

    # Act
    settings.increase_speed()

    # Assert
    captured = capsys.readouterr()
    assert settings.ship_speed == expected_ship_speed
    assert settings.bullet_speed == expected_bullet_speed
    assert settings.alien_speed == expected_alien_speed
    assert settings.alien_points == expected_alien_points
    assert captured.out.strip() == str(expected_alien_points)


