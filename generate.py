# generate.py
from colorama import Fore
from utils import completions_create


def generate_response(client, model, generation_history, verbose=0):
    output = completions_create(client, generation_history, model)
    
    if verbose > 0:
        print(Fore.BLUE, f"\n\nGENERATION\n\n{output}")
    
    return output
