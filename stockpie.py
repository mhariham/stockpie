#!/usr/bin/env python

# Author: mhariham
# Date: 03-10-2021

# ==========================================
#                  MEMORY
# ==========================================
# Error Handling Array
not_string = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Dictionary containing customize letters
letters = {
    'A': '..######..\n..#....#..\n..######..\n..#....#..\n..#....#..\n\n',
    'B': '..######..\n..#....#..\n..#####...\n..#....#..\n..######..\n\n',
    'C': '..######..\n..#.......\n..#.......\n..#.......\n..######..\n\n',
    'D': '..#####...\n..#....#..\n..#....#..\n..#....#..\n..#####...\n\n',
    'E': '..######..\n..#.......\n..#####...\n..#.......\n..######..\n\n',
    'F': '..######..\n..#.......\n..#####...\n..#.......\n..#.......\n\n',
    'G': '..######..\n..#.......\n..#####...\n..#....#..\n..#####...\n\n',
    'H': '..#....#..\n..#....#..\n..######..\n..#....#..\n..#....#..\n\n',
    'I': '..######..\n....##....\n....##....\n....##....\n..######..\n\n',
    'J': '..######..\n....##....\n....##....\n..#.##....\n..####....\n\n',
    'K': '..#...#...\n..#..#....\n..##......\n..#..#....\n..#...#...\n\n',
    'L': '..#.......\n..#.......\n..#.......\n..#.......\n..######..\n\n',
    'M': '..#....#..\n..##..##..\n..#.##.#..\n..#....#..\n..#....#..\n\n',
    'N': '..#....#..\n..##...#..\n..#.#..#..\n..#..#.#..\n..#...##..\n\n',
    'O': '..######..\n..#....#..\n..#....#..\n..#....#..\n..######..\n\n',
    'P': '..######..\n..#....#..\n..######..\n..#.......\n..#.......\n\n',
    'Q': '..######..\n..#....#..\n..#.#..#..\n..#..#.#..\n..######..\n\n',
    'R': '..######..\n..#....#..\n..#.##...\n..#...#...\n..#....#..\n\n',
    'S': '..######..\n..#.......\n..######..\n.......#..\n..######..\n\n',
    'T': '..######..\n....##....\n....##....\n....##....\n....##....\n\n',
    'U': '..#....#..\n..#....#..\n..#....#..\n..#....#..\n..######..\n\n',
    'V': '..#....#..\n..#....#..\n..#....#..\n...#..#...\n....##....\n\n',
    'W': '..#....#..\n..#....#..\n..#.##.#..\n..##..##..\n..#....#..\n\n',
    'X': '..#....#..\n...#..#...\n....##....\n...#..#...\n..#....#..\n\n',
    'Y': '..#....#..\n...#..#...\n....##....\n....##....\n....##....\n\n',
    'Z': '..######..\n......#...\n.....#....\n....#.....\n..######..\n\n',
    ' ': '..........\n..........\n..........\n..........\n\n',
    '.': '----..----\n\n'
}

# ==========================================
#                  FUNCTIONS
# ==========================================

# ===============Start======================
def start_program():
    print('''
======================= STOCKPIE NAME DECORATOR =================================
||  This program accepts any string from the user,                             ||
||  Each letter in the string(s) is first capitalize,                          ||
||  Then compare with a decorated format using fullstop(.) and naira symbol(#) ||
||  FInally, the result is printed to the User.                                ||
=================================================================================
''')
    collect_data()

# ======Accept input from User function======
def collect_data():
    print('Enter your name: \n')
    user_val = input()
    user_val = str(user_val)
    result(user_val)
    
# ========Customize letter function==========
def customize(each):
    each = each.upper()
    return letters[each]

# =============Result function===============
def result(name):
    # As long as user input is an integer, do this:
    while name in not_string:
        print('Sorry! Only letters can make a name.')
        collect_data()

    # else, print customize result
    for each in name:
        print(customize(each))
    recustomize()

# ====================Replay================
def recustomize():
    print('Still interested in customization? (1 for Yes or any input to exit):')
    val = int(input())
    if (val == 1):
        start_program()
    else:
        print('Program Ends')



# ==========================================
#               START PROGRAM
# ==========================================
# ====Call function to collect user name====
start_program()

# ===============Program Ends===============
print("______________________________________________________")
print("================== Stockpile =========================")
