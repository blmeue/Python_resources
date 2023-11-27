import pytest
from alien_invasion import AlienInvasion
from unittest.mock import Mock

# Assuming Alien and Settings are classes used within AlienInvasion
from alien import Alien
from settings import Settings

@pytest.fixture
def alien_invasion_setup():
    # Mock the settings and ship_hit method to isolate _check_aliens_bottom
    settings = Mock(screen_height=600)
    alien_invasion = AlienInvasion()
    alien_invasion.settings = settings
    alien_invasion._ship_hit = Mock()
    return alien_invasion

@pytest.mark.parametrize("alien_bottom, screen_height, expected_call_count, test_id", [
    (599, 600, 0, "happy_path_just_above_bottom"),
    (600, 600, 1, "happy_path_at_bottom"),
    (601, 600, 1, "happy_path_just_below_bottom"),
    (0, 600, 0, "edge_case_at_top"),
    (1000, 600, 1, "edge_case_far_below_bottom"),
])
def test_check_aliens_bottom(alien_invasion_setup, alien_bottom, screen_height, expected_call_count, test_id):
    """测试check_aliens_bottom"""
    # Arrange
    alien_invasion = alien_invasion_setup
    alien_invasion.settings.screen_height = screen_height
    alien = Alien(alien_invasion)
    alien.rect.bottom = alien_bottom
    alien_invasion.aliens = Mock()
    alien_invasion.aliens.sprites.return_value = [alien]

    # Act
    alien_invasion._check_aliens_bottom()

    # Assert
    assert alien_invasion._ship_hit.call_count == expected_call_count
