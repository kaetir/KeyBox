# -*- coding: utf-8 -*-

import random


def gen_phrase(nbMot: int =5)-> str:
    """
    @summary genere une phrase aléatoire a partir d'un dico
    @param int: nbMot
    @return str: la phrase de sortie 
    """
    return " ".join(random.choices(open('liste_francais.txt', 'r').read().split('\n'),k=nbMot))
    

if __name__ == "__main__":
    print(gen_phrase(3))