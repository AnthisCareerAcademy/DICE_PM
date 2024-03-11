import pytest
from Dice import Dice


@pytest.fixture
def our_dice():
    """ Dice that will be used for all tests """
    our_dice = Dice()
    return our_dice


def test_hold_when_false(our_dice):
    """ Make sure holding works """
    our_dice.is_held = False
    our_dice.hold()
    assert our_dice.is_held == True


def test_hold_when_true(our_dice):
    """ Make sure holding works """
    our_dice.is_held = True
    our_dice.hold()
    assert our_dice.is_held == False


def test_roll(our_dice):
    """ Make sure holding works """
    amt = our_dice.roll()
    assert 6 >= amt >= 1


def test_roll_when_held(our_dice):
    our_dice.is_held = True
    amt = our_dice.roll()
    assert not amt
