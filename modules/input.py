from pathlib import Path

def read_input(challenge_name):
    input_name = f'./input/{Path(challenge_name).stem}.txt'
    lines = []
    with open(input_name) as f:
        lines = f.read().splitlines()
    return lines