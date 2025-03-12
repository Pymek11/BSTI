import random

alphabet_dict = {letter: [] for letter in 'abcdefghijklmnopqrstuvwxyz '}

liczby = []
for i in range(0, 988):
    liczby.append(f"{i:03}")

letters = list('abcdefghijklmnopqrstuvwxyz ')
letter_index = 0

while len(liczby) > 0:
    random_number = random.choice(liczby)
    liczby.remove(random_number)

    current_letter = letters[letter_index]

    alphabet_dict[current_letter].append(random_number)

    letter_index = (letter_index + 1) % len(letters)

print("Contents of alphabet_dict:")
for letter, numbers in alphabet_dict.items():
    print(f"{letter}: {numbers}")

tekst = "tematy bezpieczenstwa i niebezpieczenstwa w systemach teleinformatycznych poruszamy na laboratoriach"

numerical_tekst = ""

for char in tekst:
    if char in alphabet_dict and len(alphabet_dict[char]) > 0:
        random_number = random.choice(alphabet_dict[char])
        numerical_tekst += str(random_number)
    else:
        numerical_tekst += '000'

print("Resulting string of random numbers:")
print(numerical_tekst)

inverse_tekst = ""
i = 0
while i < len(numerical_tekst):
    num_str = numerical_tekst[i:i+3]
    for letter, numbers in alphabet_dict.items():
        if num_str in numbers:
            inverse_tekst += letter
            break
    i += 3

print("Numerical tekst:")
print(numerical_tekst)

print("(converted back to letters):")
print(inverse_tekst)

# WXQOWK LXCFRXBCXUAWJO R URXLXCFRXBCXUAWJO J AKAWXQOBM WXNXRUSDEQOWKBCUKBM FDEPACOQK UO NOLDEOWDEROBM
#
# x=a?e?i?o?
#
# o=a?e?i?o?
#
# r=i?w?
#
# j=i?w?
#
# test1
# o=a, j=w? ,r=i? ,x=e?
#
# z Ua -> na?
# U=n
#
# b/c=o - > b=o?
# WeQaWK LeCFieBCenAWwa i nieLeCFieBCenAWwa w AKAWXQaBM WXNXinSDeQaWKBCUKBM FDEPACOQK na NaLDEaWDEiaBM
# 			niebezpieczenstwa
# 			L=B C=Z F=P B=C C=Z A=S W=T
# teQatk bezpieczenstwa i niebezpieczenstwa w systemach teleninformatycznych
# tematy
# Q=m
# k=Y
# tematy bezpieczenstwa i niebezpieczenstwa w systemach teleninformatycznych pDEPszOmy na NabDEatDEiach
# M=h
#
#
# abiwenobzpcstmyh
# tematy bezpieczenstwa i niebezpieczenstwa w systemach teleninformatycznych porPszOmy na laboratoriach
# D=O
# E=r
#
# tematy bezpieczenstwa i niebezpieczenstwa w systemach teleinformatycznych poruszamy na laboratoriach
