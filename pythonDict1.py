phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

# 1
phonebook_Elizabeth = phonebook_dict['Elizabeth']
print(phonebook_Elizabeth)

# 1a Don't need variable phonebook_Elizabeth
print(phonebook_dict['Elizabeth'])

# 2 Add Entry. Kareem 938-489-1234
phonebook_dict['Kareem'] = '938-489-1234'

# 3 Delete Alice's phone entry
del phonebook_dict['Alice']

# 4 Change Bob to 968-345-2345
phonebook_dict['Bob'] = '968-345-2345'

# 5 Print all phone entries
print(phonebook_dict)
