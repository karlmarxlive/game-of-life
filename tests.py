from life import next_board_state


# TODO: there's a lot of repeated code here. Can
# you move some of into reusable functions to
# make it shorter and neater?

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
    actual_next_state1 = next_board_state(init_state1)

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
    actual_next_state2 = next_board_state(init_state2)

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
    actual_next_state3 = next_board_state(init_state3)

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
    actual_next_state4 = next_board_state(init_state4)

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
    actual_next_state5 = next_board_state(init_state5)

    test_result(5, expected_next_state5, actual_next_state5)