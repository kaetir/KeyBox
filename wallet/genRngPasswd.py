import string
import random


def random_string(string_length: int = 10) -> str:
    """
    @summary genere un mot de passe aléatoire avec minuscules majuscules et ponctuation
    @param string_length: int -> nombre de lettres
    @return str: la phrase de sortie
    """
    letters = string.ascii_letters + string.punctuation
    return ''.join(random.choice(letters) for i in range(string_length))


def gen_phrase(nb_mot: int = 10) -> str:
    """ 
    @summary genere une phrase aléatoire a partir d'un dico
    @param nb_mot: int ->  nbMot
    @return str: la phrase de sortie
    """
    with open('liste_francais.txt', 'r') as f:
        return " ".join(random.choices(f.read().split('\n'), k=nb_mot))


if __name__ == "__main__":
    print(random_string(10))
    print(gen_phrase())
