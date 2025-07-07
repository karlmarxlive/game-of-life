import random
import time

DEAD = 0
ALIVE = 1


def dead_state(width: int, height: int) -> list:
    state = [[] for _ in  range(height)]
    for h in range(height):
        for w in range(width):
            state[h].append(0)
    return state

def random_state(width: int, height: int) -> list:
    state = dead_state(width, height)

    for h in range(height):
        for w in range(width):
            if random.random() >= 0.5:
                state[h][w] = ALIVE
            else:
                state[h][w] = DEAD
    return state

def render(state: list) -> None:
    print('-' * (len(state[0]) + 2))
    for i in range(len(state)):
        print('|', end='')
        for j in range(len(state[i])):
            if state[i][j] == ALIVE:
                print('#', end='')
            else:
                print('.', end='')
        print('|')

def next_board_state(state: list) -> list:
    rows = len(state)
    cols = len(state[0])
    new_state = dead_state(rows, cols)

    for i in range(rows):
        for j in range(cols):
            neighbors = 0
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    ni, nj = i + dy, j + dx
                    if 0 <= ni < rows and 0 <= nj < cols:
                        neighbors += state[ni][nj]

            if state[i][j] == ALIVE:
                new_state[i][j] = ALIVE if 2 <= neighbors <= 3 else DEAD
            if state[i][j] == DEAD:
                new_state[i][j] = ALIVE if neighbors == 3 else DEAD
    
    return new_state


def main():
    width = 10
    height = 10
    state = random_state(width, height)
    while True:
        render(state)
        time.sleep(0.2)
        state = next_board_state(state)

if __name__ == '__main__':
    main()