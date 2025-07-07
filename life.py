import random
import time
import sys

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

def get_initial_state() -> list:
    if len(sys.argv) < 2:
        print('Provide path to initial state .txt file or skip to get random initial state.')
        ans = input()
        if ans != '':
            return load_board_state(ans)
        else:
            return random_state(10, 10)
    else:
        return load_board_state(sys.argv[1])

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
        
def load_board_state(file_path: str) -> list:
    state = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
            for line in lines:
                state.append(list(map(int, line)))
    except FileNotFoundError:
        print(f'File {file_path} was not found.')
        print('Use: >python life.py pattern.txt game-mode')
        quit()
    except IOError:
        print('An error occurred while reading the file.')
        quit()
    
    return state

def get_game_mode() -> str:
    available_gamemods = [
    'normal',
    'neumann',
    'no-death',
    'walking-dead',
    'zombies'
    ]
    
    game_modes_description = """normal - using standard Conway's Game of Life.
              neumann - using extended Von Neumann Neighborhood with r = 2.
              no-death - living cells cannot die.
              walking-dead - dead cells have 20% chance to become living each round.
              zombies - add third type of cell that will wonder and eat its neighbors."""
    
    if len(sys.argv) < 3:
        print('Select in which game mode to start the game:')
        print(game_modes_description)
        game_mode = input('Type selected game-mode name: ')
    else:
        game_mode = sys.argv[2]

    if game_mode not in available_gamemods:
        print(f'Game mode "{game_mode}" does not exist.')
        print('Use: >python life.py pattern.txt game-mode')
        print('Available game modes:')
        print(game_modes_description)
        quit()
        
    return game_mode

def next_board_state(state: list, game_mode: str) -> list:
    game_mode_funcs = {
        'normal': next_board_state_normal,
        'neumann': next_board_state_neumann,
        'no-death': next_board_state_no_death,
        'walking-dead': next_board_state_walking_dead,
    }
    
    return game_mode_funcs[game_mode](state)


def next_board_state_normal(state: list) -> list:
    rows = len(state)
    cols = len(state[0])
    new_state = dead_state(cols, rows)
    
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

def next_board_state_neumann(state: list) -> list:
    rows = len(state)
    cols = len(state[0])
    new_state = dead_state(cols, rows)
    
    for i in range(rows):
        for j in range(cols):
            neighbors = 0
            for dy in range(-2, 3):
                for dx in range(-2, 3):
                    if (dx == 0 and dy == 0) or (dx != 0 and dy != 0):
                        continue
                    ni, nj = i + dy, j + dx
                    if 0 <= ni < rows and 0 <= nj < cols:
                        neighbors += state[ni][nj]

            if state[i][j] == ALIVE:
                new_state[i][j] = ALIVE if 2 <= neighbors <= 3 else DEAD
            if state[i][j] == DEAD:
                new_state[i][j] = ALIVE if neighbors == 3 else DEAD
                
    return new_state

def next_board_state_no_death(state: list) -> list:
    rows = len(state)
    cols = len(state[0])
    new_state = dead_state(cols, rows)
    
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
                new_state[i][j] = ALIVE
            if state[i][j] == DEAD:
                new_state[i][j] = ALIVE if neighbors == 3 else DEAD
                
    return new_state

def next_board_state_walking_dead(state: list) -> list:
    rows = len(state)
    cols = len(state[0])
    new_state = dead_state(cols, rows)
    
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
                new_state[i][j] = ALIVE if (neighbors == 3) or (random.random() <= 0.2) else DEAD
                
    return new_state

def main() -> None:
    state = get_initial_state()
    game_mode = get_game_mode()
    while True:
        render(state)
        time.sleep(0.2)
        state = next_board_state(state, game_mode)

if __name__ == '__main__':
    main()