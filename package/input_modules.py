import requests
import os


def write_input(year: int, day: int):
    session_cookie = os.environ.get('AOC_cookie')
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    headers = {
        'Cookie': f'session={session_cookie}'
    }

    response = requests.get(url, headers=headers)
    day = f"0{day}" if day < 10 else str(day)

    if response.status_code == 200:
        input_path = f'C:/Users/AvivTurg/Advent-Of-Code/{year}/inputs/{day}.txt'
        try:
            with open(input_path, 'w') as file:
                file.write(response.text)
        
        except:
            raise ValueError(f"'{input_path}' not found")
        
    else:
        print(response.text)