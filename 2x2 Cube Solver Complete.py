import tkinter as tk
from tkinter import *
#track each moves changes the position
def moves(a, b):
    x = a
    match x:
        case 'R':
            c = [b[0], b[5], b[2], b[7], b[4], b[21], b[6], b[23], b[10], b[8], b[11], b[9], b[3], b[13], b[1], b[15],
                 b[16], b[17], b[18], b[19], b[20], b[14], b[22], b[12]]
            return c
        case 'L':
            c = [b[15], b[1], b[13], b[3], b[0], b[5], b[2], b[7], b[8], b[9], b[10], b[11], b[12], b[22], b[14], b[20],
                 b[18], b[16], b[19], b[17], b[4], b[21], b[6], b[23]]
            return c

        case 'U':
            c = [b[2], b[0], b[3], b[1], b[8], b[9], b[6], b[7], b[12], b[13], b[10], b[11], b[16], b[17], b[14], b[15],
                 b[4], b[5], b[18], b[19], b[20], b[21], b[22], b[23]]
            return c

        case 'F':
            c = [b[0], b[1], b[19], b[17], b[6], b[4], b[7], b[5], b[2], b[9], b[3], b[11], b[12], b[13], b[14], b[15],
                 b[16], b[20], b[18], b[21], b[10], b[8], b[22], b[23]]
            return c

        case 'B':
            c = [b[9], b[11], b[2], b[3], b[4], b[5], b[6], b[7], b[8], b[23], b[10], b[22], b[14], b[12], b[15], b[13],
                 b[1], b[17], b[0], b[19], b[20], b[21], b[16], b[18]]
            return c

        case "'":
            return '' ##

#how each algorithm changes the position
def position(current_pos, algo):
    default = current_pos
    for x in range(0, len(algo)):
        a = moves(algo[x], default)
        default = a

    return default
#process the final solution
def process_string(input_str):
    # Initialize an empty list to store the processed characters
    processed_chars = []

    # Iterate through the characters in the input string
    i = 0
    while i < len(input_str):
        char = input_str[i]

        # Check if there are at least four consecutive common letters
        if i + 3 < len(input_str) and all(char == input_str[i + j] for j in range(4)):
            # Skip these four characters
            i += 4
        # Check if there are at least three consecutive common letters
        elif i + 2 < len(input_str) and all(char == input_str[i + j] for j in range(3)):
            # Remove two of them and add a single quote ' beside it
            processed_chars.append(char + "'")
            i += 3
        # Check if there are at least two consecutive common letters
        elif i + 1 < len(input_str) and char == input_str[i + 1]:
            # Remove one of them and add the number 2 beside it
            processed_chars.append(char + "2")
            i += 2
        else:
            # No consecutive common letters, just add the character
            processed_chars.append(char)
            i += 1

    # Combine the processed characters to form the final string
    processed_str = ''.join(processed_chars)

    return processed_str

def remove_consecutive_four_common(input_str):
    # Initialize an empty list to store the processed characters
    processed_chars = []

    # Iterate through the characters in the input string
    i = 0
    while i < len(input_str):
        char = input_str[i]

        # Check if there are at least four consecutive common letters
        if i + 3 < len(input_str) and all(char == input_str[i + j] for j in range(4)):
            # Skip these four characters
            i += 4
        else:
            # No consecutive four common letters, add the character
            processed_chars.append(char)
            i += 1

    # Combine the processed characters to form the final string
    processed_str = ''.join(processed_chars)

    return processed_str

#solve the 2x2 cube
def solve(color):
    f1 = ""
    f2 = ""
    R1 = ""
    i = 0
    while i < 24:
        if (color[i] == color[20]):
            f1 = i
            break
        if (i == 5):
            i = i + 2
        elif (i == 18):
            i = i + 3
        else:
            i = i + 1

    if (f1 == 0):
        R = "URR"
    elif (f1 == 1):
        R = "RR"
    elif (f1 == 2):
        R = "UURR"
    elif (f1 == 3):
        R = "UUURR"
    elif (f1 == 4):
        R = "UUURURRR"
    elif (f1 == 5):
        R = "RRR"
    elif (f1 == 7):
        R = "RUUURR"
    elif (f1 == 8):
        R = "RURRR"
    elif (f1 == 9):
        R = "URRR"
    elif (f1 == 10):
        R = "RRURRR"
    elif (f1 == 11):
        R = "RRRURRR"
    elif (f1 == 12):
        R = "FFFUF"
    elif (f1 == 13):
        R = "UURRR"
    elif (f1 == 14):
        R = "R"
    elif (f1 == 15):
        R = "BR"
    elif (f1 == 16):
        R = "FFFUUF"
    elif (f1 == 17):
        R = "UUURRR"
    elif (f1 == 18):
        R = "BBBURR"
    elif (f1 == 21):
        R = ""
    elif (f1 == 22):
        R = ""
    elif (f1 == 23):
        R = ""

    #print(R)
    # position after second corner solved
    color2 = position(color, R)

    # second corner right back
    i2 = 0
    while i2 < 24:
        if (color2[i2] == color2[20]):
            f2 = i2
            break
        if (i2 == 5):
            i2 = i2 + 3
        elif (i2 == 9):
            i2 = i2 + 2
        elif (i2 == 18):
            i2 = i2 + 4
        else:
            i2 = i2 + 1

    if (f2 == 0):
        R1 = "BB"
    elif (f2 == 1):
        R1 = "UUUBB"
    elif (f2 == 2):
        R1 = "UBB"
    elif (f2 == 3):
        R1 = "UUBB"
    elif (f2 == 4):
        R1 = "RRRUUR"
    elif (f2 == 5):
        R1 = "UUUBBB"
    elif (f2 == 8):
        R1 = "URRRUUR"
    elif (f2 == 9):
        R1 = "RRRUUUR"
    elif (f2 == 11):
        R1 = "BUUUBB"
    elif (f2 == 12):
        R1 = "BUBBB"
    elif (f2 == 13):
        R1 = "UBBB"
    elif (f2 == 14):
        R1 = "BBUBBB"
    elif (f2 == 15):
        R1 = "BBBUBBB"
    elif (f2 == 16):
        R1 = "RRRUR"
    elif (f2 == 17):
        R1 = "UUBBB"
    elif (f2 == 18):
        R1 = "B"
    elif (f2 == 22):
        R1 = ""
    elif (f2 == 23):
        R1 = ""
    else:
        error_message('The colors are not entered properly')
        return ''

    # print(R1)
    # position after third pair solved

    color3 = position(color2, R1)
    # print(color3)
    i3 = 0
    while i3 < 23:
        if (color3[i3] == color3[20]):
            f3 = i3
            break
        if (i3 == 18):
            i3 = i3 + 4
        else:
            i3 = i3 + 1

    if (f3 == 0):
        R2 = "BBBUBLUULLL"
    elif (f3 == 1):
        R2 = "UUUBBBUBLUULLL"
    elif (f3 == 2):
        R2 = "UBBBUBLUULLL"
    elif (f3 == 3):
        R2 = "UUBBBUBLUULLL"
    elif (f3 == 4):
        R2 = "BBBUB"
    elif (f3 == 5):
        R2 = "LUULLL"
    elif (f3 == 8):
        R2 = "BBBUUB"
    elif (f3 == 9):
        R2 = "LUUULLL"
    elif (f3 == 12):
        R2 = "UUULULLL"
    elif (f3 == 13):
        R2 = "BBBUUUB"
    elif (f3 == 15):
        R2 = "LUUULLLBBBUUUB"
    elif (f3 == 16):
        R2 = "LULLL"
    elif (f3 == 17):
        R2 = "UUULUULLL"
    elif (f3 == 18):
        R2 = "LULLLUUULULLL"
    elif (f3 == 22):
        R2 = ""
    else:
        error_message('The colors are not entered properly')
        return ''
    # print(R2)

    # Fix the first layer corner
    color4 = position(color3, R2)
    # print(color4)
    if ((color4[6] != color4[7]) and (color4[14] != color4[15]) and (color4[10] != color4[11]) and (
            color4[18] != color4[19])):
        R3 = "RRBBRR"
    elif (color4[6] == color4[7] and color4[10] == color4[11]):
        R3 = ""
    elif (color4[6] == color[7] and color4[14] == color[15]):
        R3 = "RRRUUURRBRRUUUR"
    elif (color4[10] == color4[11]):
        R3 = "FUUUFFLFFUUUFFF"
    elif (color4[18] == color4[19]):
        R3 = "FFFUUUFFRFFUUUF"
    elif (color4[14] == color4[15]):
        R3 = "RUUURRFRRUUURRR"
    elif (color4[6] == color4[7]):
        R3 = "FUFFLLLFFUFFF"
    else:
        error_message('The colors are not entered properly')
    R4 = R + R1 + R2 + R3
    # print(R4)

    color5 = position(color4, R3)
    # print(color5)
    # set the upper color target
    if (color5[20] == 'white'):
        upper = 'yellow'
    elif (color5[20] == 'yellow'):
        upper = 'white'
    elif (color5[20] == 'blue'):
        upper = 'green'
    elif (color5[20] == 'green'):
        upper = 'blue'
    elif (color5[20] == 'red'):
        upper = 'orange'
    elif (color5[20] == 'orange'):
        upper = 'red'
    else:
        error_message('The colors are not entered properly')
        return ''

    # last layer oll
    Fish1 = 'RURRRURUURRR'
    Fish2 = 'RUURRRUUURUUURRR'

    upperface = color5[0] + color5[1] + color5[2] + color5[3]
    upper_count = upperface.count(upper)
    # print(upper)
    if (upper_count == 1 and color5[0] == upper and color5[17] == upper):
        oll = 'FUFFFUFUUFFF'
    elif (upper_count == 1 and color5[0] == upper and color5[4] == upper):
        oll = 'RRRUUURUUURRRUUR'
    elif (upper_count == 1 and color5[1] == upper and color5[13] == upper):
        oll = 'LULLLULUULLL'
    elif (upper_count == 1 and color5[1] == upper and color5[16] == upper):
        oll = Fish2
    elif (upper_count == 1 and color5[2] == upper and color5[5] == upper):
        oll = Fish1
    elif (upper_count == 1 and color5[2] == upper and color5[8] == upper):
        oll = 'LUULLLUUULUUULLL'
    elif (upper_count == 1 and color5[3] == upper and color5[9] == upper):
        oll = 'RRRUURURRRUR'
    elif (upper_count == 1 and color5[3] == upper and color5[12] == upper):
        oll = 'LLLUUULUUULLLUUL'

    elif (upper_count == 2 and color5[4] == upper and color5[5] == upper):
        oll = 'RBUBBBUUURRR'
    elif (upper_count == 2 and color5[16] == upper and color5[17] == upper):
        oll = 'FRURRRUUUFFF'
    elif (upper_count == 2 and color5[12] == upper and color5[13] == upper):
        oll = 'LFUFFFUUULLL'
    elif (upper_count == 2 and color5[8] == upper and color5[9] == upper):
        oll = 'FURUUURRRFFF'

    elif (upper_count == 2 and color5[4] == upper and color5[13] == upper):
        oll = 'RURRRUUURRRFRFFF'
    elif (upper_count == 2 and color5[17] == upper and color5[8] == upper):
        oll = 'BUBBBUUUBBBRBRRR'
    elif (upper_count == 2 and color5[5] == upper and color5[12] == upper):
        oll = 'LLLUUULULFFFLLLF'
    elif (upper_count == 2 and color5[9] == upper and color5[16] == upper):
        oll = 'FUFFFUUUFFFLFLLL'

    elif (upper_count == 2 and color5[4] == upper and color5[9] == upper):
        oll = 'FRRRFFFRURUUURRR'
    elif (upper_count == 2 and color5[8] == upper and color5[13] == upper):
        oll = 'RBBBRRRBUBUUUBBB'
    elif (upper_count == 2 and color5[5] == upper and color5[16] == upper):
        oll = 'FFFRURRRUUURRRFR'
    elif (upper_count == 2 and color5[12] == upper and color5[17] == upper):
        oll = 'LLLFUFFFUUUFFFLF'

    elif (upper_count == 0 and color5[4] == upper and color5[5] == upper and color5[12] == upper and color5[
        13] == upper):
        oll = 'RRUURUURR'
    elif (upper_count == 0 and color5[8] == upper and color5[9] == upper and color5[16] == upper and color5[
        17] == upper):
        oll = 'FFUUFUUFF'

    elif (upper_count == 0 and color5[5] == upper and color5[12] == upper):
        oll = 'RUURRUUURRUUURRUUR'
    elif (upper_count == 0 and color5[9] == upper and color5[16] == upper):
        oll = 'BUUBBUUUBBUUUBBUUB'
    elif (upper_count == 0 and color5[4] == upper and color5[13] == upper):
        oll = 'LUULLUUULLUUULLUUL'
    elif (upper_count == 0 and color5[8] == upper and color5[17] == upper):
        oll = 'FUUFFUUUFFUUUFFUUF'
    elif (upper_count == 4 ):
        oll = ''
    else:
        error_message('The colors are not entered properly')
        return ''
    #print(oll)

    color6 = position(color5, oll)
    # print(color6)

    if (color6[4] == color6[5] and color6[12] == color6[13]):
        pll = ''
    elif (color6[4] == color6[5]):
        pll = 'LLLBLLLFFLBBBLLLFFLL'
    elif (color6[8] == color6[9]):
        pll = 'FFFLFFFRRFLLLFFFLLFF'
    elif (color6[12] == color6[13]):
        pll = 'RRRFRRRBBRFFFRRRBBRR'
    elif (color6[16] == color6[17]):
        pll = 'BBBRBBBLLBRRRBBBLLBB'
    else:
        pll = 'FUUURUFFFRRFFFUUURRRURR'

    color7 = position(color6, pll)

    if (color7[4] == color7[10]):
        lm = 'UUU'
    elif (color7[4] == color7[14]):
        lm = 'UU'
    elif (color7[4] == color7[18]):
        lm = 'U'
    else:
        lm = ''

    total_solution = R + R1 + R2 + R3 + oll + pll + lm

    final_solution = remove_consecutive_four_common(total_solution)
    final_solution2 = remove_consecutive_four_common(final_solution)
    s.insert(0,process_string(final_solution2))
    return process_string(final_solution2)

def error_message(message):
    s.insert(0,message)

def change_color(color_name, button):
    color_options = ['red', 'blue', 'yellow', 'white', 'orange', 'green']
    current_index = color_options.index(color_name)
    new_index = (current_index + 1) % len(color_options)
    button['bg'] = color_options[new_index]
    return color_options[new_index]
def count_word_occurrences(word, word_list):
    count = 0
    for w in word_list:
        if w == word:
            count += 1
    return count

def print_colors():
    colors = [A['bg'], B['bg'], C['bg'], D['bg'], E['bg'], F['bg'], G['bg'], H['bg'], I['bg'], J['bg'], K['bg'],
              L['bg'], M['bg'], N['bg'], O['bg'], P['bg'], Q['bg'], R['bg'], S['bg'], T['bg'], U['bg'], V['bg'],
              W['bg'], X['bg']]
    r=count_word_occurrences('red',colors)
    b = count_word_occurrences('blue', colors)
    y = count_word_occurrences('yellow', colors)
    g = count_word_occurrences('green', colors)
    w = count_word_occurrences('white', colors)
    o = count_word_occurrences('orange', colors)
    if(r==b==y==g==w==o):
        solve(colors)
    else:
        return error_message('The colors are not entered properly')




root = tk.Tk()
root.geometry("700x400")
# Upper Phase
A = tk.Button(root, text="", bg='white', padx=10, pady=6, command=lambda: change_color(A['bg'], A))
A.grid(row=10, column=10)

B = tk.Button(root, text="", bg='white', padx=10, pady=6, command=lambda: change_color(B['bg'], B))
B.grid(row=10, column=12)

C = tk.Button(root, text="", bg='white', padx=10, pady=6, command=lambda: change_color(C['bg'], C))
C.grid(row=12, column=10)

D = tk.Button(root, text="", bg='white', padx=10, pady=6, command=lambda: change_color(D['bg'], D))
D.grid(row=12, column=12)
# Front phase

E = tk.Button(root, text="", bg='green', padx=10, pady=6, command=lambda: change_color(E['bg'], E))
E.grid(row=14, column=10)

F = tk.Button(root, text="", bg='green', padx=10, pady=6, command=lambda: change_color(F['bg'], F))
F.grid(row=14, column=12)

G = tk.Button(root, text="", bg='green', padx=10, pady=6, command=lambda: change_color(G['bg'], G))
G.grid(row=16, column=10)

H = tk.Button(root, text="", bg='green', padx=10, pady=6, command=lambda: change_color(H['bg'], H))
H.grid(row=16, column=12)
# Right phase

I = tk.Button(root, text="", bg='red', padx=10, pady=6, command=lambda: change_color(I['bg'], I))
I.grid(row=14, column=14)

J = tk.Button(root, text="", bg='red', padx=10, pady=6, command=lambda: change_color(J['bg'], J))
J.grid(row=14, column=16)

K = tk.Button(root, text="", bg='red', padx=10, pady=6, command=lambda: change_color(K['bg'], K))
K.grid(row=16, column=14)

L = tk.Button(root, text="", bg='red', padx=10, pady=6, command=lambda: change_color(L['bg'], L))
L.grid(row=16, column=16)

# Left phase

Q = tk.Button(root, text="", bg='orange', padx=10, pady=6, command=lambda: change_color(Q['bg'], Q))
Q.grid(row=14, column=6)

R = tk.Button(root, text="", bg='orange', padx=10, pady=6, command=lambda: change_color(R['bg'], R))
R.grid(row=14, column=8)

S = tk.Button(root, text="", bg='orange', padx=10, pady=6, command=lambda: change_color(S['bg'], S))
S.grid(row=16, column=6)

T = tk.Button(root, text="", bg='orange', padx=10, pady=6, command=lambda: change_color(T['bg'], T))
T.grid(row=16, column=8)
# Back phase

M = tk.Button(root, text="", bg='blue', padx=10, pady=6, command=lambda: change_color(M['bg'], M))
M.grid(row=14, column=2)

N = tk.Button(root, text="", bg='blue', padx=10, pady=6, command=lambda: change_color(N['bg'], N))
N.grid(row=14, column=4)

O = tk.Button(root, text="", bg='blue', padx=10, pady=6, command=lambda: change_color(O['bg'], O))
O.grid(row=16, column=2)

P = tk.Button(root, text="", bg='blue', padx=10, pady=6, command=lambda: change_color(P['bg'], P))
P.grid(row=16, column=4)
# Down Phase

U = tk.Button(root, text="", bg='yellow', padx=10, pady=6, command=lambda: change_color(U['bg'], U))
U.grid(row=18, column=10)

V = tk.Button(root, text="", bg='yellow', padx=10, pady=6, command=lambda: change_color(V['bg'], V))
V.grid(row=18, column=12)

W = tk.Button(root, text="", bg='yellow', padx=10, pady=6, command=lambda: change_color(W['bg'], W))
W.grid(row=20, column=10)

X = tk.Button(root, text="", bg='yellow', padx=10, pady=6, command=lambda: change_color(X['bg'], X))
X.grid(row=20, column=12)

b5 = tk.Button(root, text="Solve", command=print_colors)
b5.grid(row=5, column=0, columnspan=2)

solves=""
solves = StringVar()

s = Entry(root, textvariable=solves,font=10, width=40)
s.grid(row=40,padx=10, pady=10)


#la=Label(root, text=sol)
root.mainloop()
