import random

polish_alphabet_freq = {
    'a': 10.503, 'i': 8.812, 'o': 8.340, 'e': 7.352, 'z': 6.998, 'n': 6.223,
    's': 4.911, 'c': 4.520, 'r': 4.423, 'w': 4.208, 'y': 3.998, 'd': 2.854,
    'k': 2.798, 'm': 2.724, 't': 2.452, 'p': 2.083, 'u': 1.990, 'j': 1.836,
    'l': 1.821, 'g': 1.731, 'b': 1.134, 'h': 0.940, 'f': 0.260, 'v': 0.034, ## przypisanie do liter ich odpowiadajacayh procentow wystepowania
    'q': 0.014, 'x': 0.014, ' ': 15.000
}

total_codes = 988
all_codes = [f"{i:03}" for i in range(total_codes)] ## zapis liczby 1 jako 001 itd
random.shuffle(all_codes)

alphabet_dict = {letter: [] for letter in polish_alphabet_freq}  ## arraye wszystkich liter

for letter in polish_alphabet_freq:
    num_codes = round((polish_alphabet_freq[letter] / 100) * total_codes)
    if len(all_codes) < num_codes:
        num_codes = len(all_codes)
    alphabet_dict[letter] = [all_codes.pop() for _ in range(num_codes)]  ##  zapis losowych liczb do arrayi , ilosc liczb wpisywana za pomoca czestotliwosci

if all_codes:
    alphabet_dict[' '] += all_codes ## wpis do " " -( spacji ) pozostalych liczb

def encode_text(text, code_dict):
    encoded_text = ""
    for char in text:
        if char in code_dict and code_dict[char]:
            encoded_text += random.choice(code_dict[char])  ##zakodowanie tekstu w liczby dopasowane w arrayiu
        else:
            encoded_text += "000"
    return encoded_text

def decode_text(encoded_text, code_dict):
    decoded_text = ""
    for i in range(0, len(encoded_text), 3):
        code = encoded_text[i:i+3]
        for letter, codes in code_dict.items():  ## dekodowanie tekstu
            if code in codes:
                decoded_text += letter
                break
        else:
            decoded_text += '?'
    return decoded_text

# for letter, numbers in alphabet_dict.items():
#     print(f"{letter}: {', '.join(numbers)}") ## sprawdzenie tabeli liczb

tekst = "tematy bezpieczenstwa i niebezpieczenstwa w systemach teleinformatycznych poruszamy na laboratoriach"
numerical_tekst = encode_text(tekst, alphabet_dict)
decoded_tekst = decode_text(numerical_tekst, alphabet_dict)

print("Original text:")
print(tekst)
print("\nEncoded numerical text:")
print(numerical_tekst)
print("\nDecoded text:")
print(decoded_tekst)
