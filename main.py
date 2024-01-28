MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ':' '}
Message = input('Please enter your message below \n')
Morse_msg = ''
Morse_msg_list = []
for i in Message:
    Morsed_letter = MORSE_CODE_DICT[i.capitalize()]
    Morse_msg_list.append(Morsed_letter)
    Morse_msg += Morsed_letter
print(Morse_msg)
Question = input('Do you want to decode previous message? Enter "Y" or "N" \n')
Question = Question.capitalize()
if Question == 'Y':
    Unmorsed_msg = ""
    for keys in Morse_msg_list:
        Unmorsed_letter = [key for key, morsed in MORSE_CODE_DICT.items() if morsed == keys]
        Unmorsed_msg += Unmorsed_letter[0]
    print(Unmorsed_msg.lower().capitalize())




