a = 4
b = 11
print('nilai :', a,'dalam biner: ', format(a,'08b'))
print('nilai :', b,'dalam biner: ', format(b,'08b'))

c = a | b
print('Bitwise OR nilai : ', c, ', biner :', format(c,'08b'))

c = a >> b
print('Bitwise right shift nilai : ', c, ', biner :', format(c,'08b'))

c = a ^ b
print('Bitwise XOR nilai : ', c, ', biner :', format(c,'08b'))

c = ~a
print('Bitwise NOT nilai : ', c, ', biner :', format(c,'08b'))

c = b & a
print('Bitwise AND nilai : ', c, ', biner :', format(c,'08b'))