ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# Get ramit's email addy
print(ramit['email'])

# Get ramit's 1st interest
print(ramit['interests'][0])

# Get email addy for Jasmine
print(ramit['friends'][0]['email'])

# Get Jan's 2nd interest
print(ramit['friends'][1]['interests'][1])