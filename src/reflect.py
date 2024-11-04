# reflect.py

from colorama import Fore
from utils import completions_create

def reflect_on_response(client, model, reflection_history, verbose=0):
    output = completions_create(client, reflection_history, model)
    
    if verbose > 0:
        print(Fore.GREEN, f"\n\nREFLECTION\n\n{output}")
    
    return output
