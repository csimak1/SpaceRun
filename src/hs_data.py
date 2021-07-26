import json
import pygame
import re
def enter_score(score):
    fref = open('data/high_score.data', 'a')
    fref.write(str(score)+ '\n')
    fref.close()


def top_five():
    fref = open('data/high_score.data', 'r').read()
    data = re.findall("[0-9]+",fref)
    top = []
    for i in range(len(data)):
        top.append(int(data[i]))
    top.sort(reverse = True)
    return top[0:5]


