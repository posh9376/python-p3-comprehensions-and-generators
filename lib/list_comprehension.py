#!/usr/bin/env python3

def return_evens(num_list):
    even_nums = [n for n in num_list if n%2 == 0]
    return even_nums

def make_exclamation(sentence_list):
    if not sentence_list:
        return[]
    else:
        new_list = [f"{str}!" for str in sentence_list]
        return new_list
