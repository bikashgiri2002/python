Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = 'bikash'
name
'bikash'
first_char = name[0]
print(first_char)
b
name
'bikash'
first_char
'b'
name = 'bikash kumar giri'
middle_name = name[7:12]
middle_name
'kumar'
name[:2:]
'bi'
name[::2]
'bks ua ii'
name
'bikash kumar giri'
name.lower()
'bikash kumar giri'
name.upper()
'BIKASH KUMAR GIRI'
name
'bikash kumar giri'
name.capitalize()
'Bikash kumar giri'
name = name.capitalize()
name
'Bikash kumar giri'
name.strip()
'Bikash kumar giri'
name.replace('Bikash', 'Bhagya)
             
SyntaxError: unterminated string literal (detected at line 1)
name.replace('Bikash', 'Bhagya')
             
'Bhagya kumar giri'
name_list = 'Bhagya, Bikash, Jinu, Laxmi'
             
name_list.split(', ')
             
['Bhagya', 'Bikash', 'Jinu', 'Laxmi']
name_list.split(', ').reverse()
             
name_list
             
'Bhagya, Bikash, Jinu, Laxmi'
print(name_list.split(', ').reverse())
             
None
reverse_name_list = name_list.split(', ').reverse()
             
reverse_name_list
             
reverse_name_list = list(name_list.split(', ').reverse())
             
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    reverse_name_list = list(name_list.split(', ').reverse())
TypeError: 'NoneType' object is not iterable
reverse_name_list = name_list.split(', ')
             
reverse_name_list
             
['Bhagya', 'Bikash', 'Jinu', 'Laxmi']
reverse_name_list.reverse()
             
reverse_name_list
             
['Laxmi', 'Jinu', 'Bikash', 'Bhagya']
name
             
'Bikash kumar giri'
name.find('i')
             
1
name.count('i')
             
3
