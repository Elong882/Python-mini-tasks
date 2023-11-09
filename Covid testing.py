name = input('Name?    ').upper()  # could use('Name?'.ljust(9)).upper()
data = []  # stores our columns
unicode_list = []  # stores our third column
for character in name:
    unicode = ord(character)  # ensures we can increment easier
    unicode_list.append(unicode)  # char-->unicode,store as list
    
keytext = input('Keytext? ')
KEY = [('A', '0'), ('B', '1'), ('C', '2'), ('D', '3'), ('E', '4'),
       ('F', '5'), ('G', '6'), ('H', '7'), ('I', '8'), ('J', '9'),
       ('K', '10'), ('L', '11'),
       ('M', '12'), ('N', '13'), ('O', '14'), ('P', '15'),
       ('Q', '16'), ('R', '17'), ('S', '18'), ('T', '19'),
       ('U', '20'), ('V', '21'), ('W', '22'),
       ('X', '23'), ('Y', '24'), ('Z', '25')]  # converts middle column
for letter, number in KEY:
    keytext = keytext.replace(letter, number)  # keytext-->numbers
  
    new_number = keytext.replace(letter, number)  
keytext_list = list(new_number)  # list of char--> list of no
keytext_list = [int(integer) for integer in keytext_list]  
conversion = [a + b for a, b in zip(unicode_list, keytext_list)]  
updated_keytext = [chr(c) for c in conversion]  # no-->char

data.append(name)  # name stays the same on first column
data.append(keytext)  # second column shows updated numbers
data.append(updated_keytext)  # last column shows the updated keytext
for i in zip(*data):
    print(*i)  # print all contents of data in a column
