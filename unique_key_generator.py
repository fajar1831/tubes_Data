import json
import itertools

list_com = [] #list menampung key hasil generate (string)
temp_perm = [] #list untuk menampung key hasil generate (raw permutation)

def generate():
    h = itertools.permutations('123456789', 8)
    xa = list(h)
    temp_perm = xa
    y = 0
    for items in temp_perm:
        a1 = temp_perm[y][0]
        a2 = temp_perm[y][1]
        a3 = temp_perm[y][2]
        a4 = temp_perm[y][3]
        a5 = temp_perm[y][4]
        a6 = temp_perm[y][5]
        a7 = temp_perm[y][6]
        a8 = temp_perm[y][7]
        b1 = str(a1)
        b2 = str(a2)
        b3 = str(a3)
        b4 = str(a4)
        b5 = str(a5)
        b6 = str(a6)
        b7 = str(a7)
        b8 = str(a8)
        concatt = b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8
        list_com.append(concatt)
        y = y+1
def main_ex():

    generate()

    unique_key = {
        "key_av" : list_com
    }
    with open('data_unique_key.json', 'w') as f:
        json.dump(unique_key, f)

main_ex()