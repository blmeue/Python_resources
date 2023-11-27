import pytest
from alien_invasion import AlienInvasion
from unittest.mock import Mock, call

# Assuming Alien class has a method check_edges and _change_fleet_direction is a method of AlienInvasion

@pytest.mark.parametrize("edge_status, expected_calls", [
    pytest.param([False, False, False], [], id="no_aliens_at_edge"),
    pytest.param([False, True, False], [call()._change_fleet_direction()], id="one_alien_at_edge"),
    pytest.param([True, True, True], [call()._change_fleet_direction()], id="all_aliens_at_edge"),
], ids=["happy_no_edge", "happy_one_edge", "happy_all_edges"])
def test_check_fleet_edges(edge_status, expected_calls):
    """测试_check_fleet_edges"""
    # Arrange
    game = AlienInvasion()
    game.aliens = Mock()
    game.aliens.sprites.return_value = [Mock(check_edges=Mock(return_value=status)) for status in edge_status]
    game._change_fleet_direction = Mock()

    # Act
    game._check_fleet_edges()

    # Assert
    assert game._change_fleet_direction.mock_calls == expected_calls

@pytest.mark.parametrize("edge_status, change_direction_exception, expected_exception", [
    pytest.param([False, True, False], Exception("Error"), Exception, id="exception_on_change_direction"),
], ids=["error_change_direction"])
def test_check_fleet_edges_exceptions(edge_status, change_direction_exception, expected_exception):
    """测试_check_fleet_edges"""
    # Arrange
    game = AlienInvasion()
    game.aliens = Mock()
    game.aliens.sprites.return_value = [Mock(check_edges=Mock(return_value=status)) for status in edge_status]
    game._change_fleet_direction = Mock(side_effect=change_direction_exception)

    # Act / Assert
    with pytest.raises(expected_exception):
        game._check_fleet_edges()
