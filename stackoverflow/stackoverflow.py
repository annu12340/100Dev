import requests
import webbrowser
from subprocess import Popen, PIPE
from termcolor import cprint


def stackoverflow_soln(error):
    cprint('Searching in stackoverflow for the error '+error, 'blue')
    response = requests.get(
        "https://api.stackexchange.com/2.2/search?order=desc&tagged=python&sort=activity&intitle="+error+"&site=stackoverflow")
    res = response.json()['items']
    i = 0
    for data in res:
        i += 1
        if i <= 5:
            if data['is_answered']:
                cprint('Opening the solution in the browser', 'cyan')
                webbrowser.open(data['link'])


def execute_actual_program(file):
    print('\n\n *********************************************\n')
    cprint('Executing the code', 'white', 'on_green')
    print("\n\n")
    response, err = Popen(file, stdout=PIPE, stderr=PIPE).communicate()
    return response, err


if __name__ == "__main__":
    response, err = execute_actual_program("python test.py")
    error = err.decode("utf-8").strip().split("\r\n")[-1]

    if error:
        cprint('An error has occurred', 'white', 'on_red')
        stackoverflow_soln(error)
    else:
        cprint('The program is running successfully', 'blue')

    print('\n\n *********************************************\n')
