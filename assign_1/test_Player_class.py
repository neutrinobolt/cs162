from Player_class import Player

def player_test ():
    test_player = Player()

    expected_name = "Player"
    expected_elem_type = "Water"
    expected_level = 1
    expected_skills = [10,1,1,1,1,1,1]
    expected_xp_current = 0
    expected_pvs = [0,0,0,0,0,0,0]
    expected_armor_equipped: list = []
    expected_inventory: list = []

    assert test_player.name == expected_name
    assert test_player.type == expected_elem_type
    assert test_player.level == expected_level
    assert test_player.skills == expected_skills 
    assert test_player.xp == expected_xp_current
    assert test_player.pvs == expected_pvs
    assert test_player.armor == expected_armor_equipped
    assert test_player.inventory == expected_inventory

    print("Player test successful.")

def obtain_test():
    test_player = Player()
    test_player.obtain("Test Object")

    expected_inv = ["Test Object"]

    assert test_player.inventory == expected_inv
    print("Obtain test successful.")

player_test()
obtain_test()
