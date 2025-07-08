from life import next_board_state, generate_random_zombie, is_state_has_zombie, next_board_state_zombies


def test_result(test_number: int, expected: list, actual: list) -> None:
    if expected == actual:
        print(f'PASSED {test_number}')
    else:
        print(f'FAILED {test_number}!')
        print('Expected:')
        print(expected)
        print('Actual:')
        print(actual)

if __name__ == "__main__":
    game_mode = 'normal'
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    actual_next_state1 = next_board_state(init_state1, game_mode)

    test_result(1, expected_next_state1, actual_next_state1)

    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    actual_next_state2 = next_board_state(init_state2, game_mode)

    test_result(2, expected_next_state2, actual_next_state2)


    # TEST 3: Alive cells with exactly 3 neighbors
    # should stay alive.
    init_state3 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state3 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    actual_next_state3 = next_board_state(init_state3, game_mode)

    test_result(3, expected_next_state3, actual_next_state3)

    # TEST 4: Alive cells with more than 3 neighbors
    # should become dead
    init_state4 = [
        [1,1,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state4 = [
        [1,0,1],
        [1,0,1],
        [0,0,0]
    ]
    actual_next_state4 = next_board_state(init_state4, game_mode)

    test_result(4, expected_next_state4, actual_next_state4)

    # TEST 5: Edge cases
    init_state5 = [
        [1,1,0],
        [1,1,1],
        [0,1,1]
    ]
    expected_next_state5 = [
        [1,0,1],
        [0,0,0],
        [1,0,1]
    ]
    actual_next_state5 = next_board_state(init_state5, game_mode)

    test_result(5, expected_next_state5, actual_next_state5)
    
    game_mode = 'neumann'
    #TEST 6 NEUMANN: dead cells with no live neighbors
    # should stay dead.
    init_state6 = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ]
    expected_next_state6 = [
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ]
    actual_next_state6 = next_board_state(init_state6, game_mode)

    test_result(6, expected_next_state6, actual_next_state6)

    # TEST 7 NEUMANN: dead cells with exactly 3 neighbors
    # should come alive.
    # Alive cells with exactly 2 neighbors stay alive.
    # Alive cell with < 2 neighbors become dead.
    init_state7 = [
        [0,1,1,1,0],
        [1,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ]
    expected_next_state7 = [
        [1,1,1,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
    ]
    actual_next_state7 = next_board_state(init_state7, game_mode)

    test_result(7, expected_next_state7, actual_next_state7)

    # TEST 8 NEUMANN: Edge cases
    init_state8 = [
        [0,1,1,1,0],
        [0,0,0,0,0],
        [0,1,1,1,0],
        [0,0,0,0,0],
        [0,1,1,1,0],
    ]
    expected_next_state8 = [
        [0,1,1,1,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,1,1,1,0],
    ]
    actual_next_state8 = next_board_state(init_state8, game_mode)

    test_result(8, expected_next_state8, actual_next_state8)
    
    # TEST 9 ZOMBIE: find zombie in a state
    state9 = [
        [0,0,0],
        [0,0,0],
        [2,0,0],
    ]
    expected_result9 = True
    actual_result9 = is_state_has_zombie(state9)
    
    test_result(9, expected_result9, actual_result9)
    
    # TEST 10 ZOMBIE: do not find any zombie
    state10 = [
        [0,0,0],
        [0,0,0],
        [0,0,0],
    ]
    expected_result10 = False
    actual_result10 = is_state_has_zombie(state10)
    
    test_result(10, expected_result10, actual_result10)
    
    # TEST 11 ZOMBIE: must create zombie at random place
    init_state11 = [
        [0,0,0],
        [0,0,0],
        [0,0,0],
    ]
    expected_result11 = True
    zombie_state11 = generate_random_zombie(init_state11)
    actual_result11 = is_state_has_zombie(zombie_state11)
    
    test_result(11, expected_result11, actual_result11)
    print(zombie_state11)
    
    # TEST 12 ZOMBIE: zombie changed its position
    init_state12 = [
        [2,0,0]
    ]
    expected_next_state12 = [
        [0,2,0]
    ]
    actual_next_state12 = next_board_state(init_state12, 'zombies')
    
    test_result(12, expected_next_state12, actual_next_state12)
    
    # TEST 13 ZOMBIE: zombie created new zombie and stayed in place
    init_state13 = [
        [0,2,0],
        [0,1,0],
        [0,0,0],
    ]
    expected_next_state13 = [
        [0,2,0],
        [0,2,0],
        [0,0,0]
    ]
    actual_next_state13 = next_board_state(init_state13, 'zombies')
    
    test_result(13, expected_next_state13, actual_next_state13)