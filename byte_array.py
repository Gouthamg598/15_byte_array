'''bytes datatype
bytes is a immutable'''
# d=b'python'
# print(type(d),d)#<class 'bytes'> b'python'

'''bytearray data type it is a mutable'''

# a=bytearray(b'pythom')
# print(a.index(b'm'))# index position of m=5 
'''in python ASCII(american standard code for information interchange) values for
a--->97 to z--->122 and 
A--->65 to Z--->90 and
0--->48 to 9--->57
'''
# print(ord("n"))
# a[5]=110
# print(a)
# print(chr(0))#null
# print(ord('0'))#48
# print(chr(48))#0
# print(chr(32))#blank line

# '''\u give emojis from 0001 to 0006  ,0007 and 0008 gives blank lines'''
# print('\u0001')
# print('\u0002')
# print('\u0003')
# print('\u0004')
# print('\u0005')
# print('\u0006')
# print('\u0007')

'''to print binary code(2) use --bin, binary value interms of -->0b____ '''
# print(bin(56))#0b111000
# print(0b111000)#56  
# print(bin(6))#0b110
# print(0b110)#6
# print(bin(1))#0b1

'''to print octal number(8)---oct , binary value interms of-->0o_____'''
# print(oct(56))#0o70
# print(0o70)#56
# print(oct(2))#0o2
# print('0o2')#2
# print(oct(7899))#0o17333
# print(0o17333)#7899

'''hex decimal value(16)--->hex, binary value interms of--->0x____'''
# print(hex(56))#0x38
# print(0x38)#56
# print(hex(46))#0x2e
# print(0x2e)#46
# a=0.1+0.2
# b=0.7+0.2
# print(a,b)#0.30000000000000004 ,0.8999999999999999
# print('%.1f,%.1f'%(a,b))#0.3,0.9

# print(7/0)#ZeroDivisionError: division by zero
