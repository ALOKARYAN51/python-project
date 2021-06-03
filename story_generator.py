import random
when = ['A few year ago', 'Yesterday','Last night', 'A long time ago', 'On 3rd Jun']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']
name = ['Aman', 'Alok', 'Aditya' , 'Deep', 'Abhilasha']
residence = ['India', 'USA', 'England','Germany','Nepal']
went = ['college', 'school', 'cinema','laundary']
happend = ['made a lot of friends', 'Eats Burger', 'solve maths', 'found mystery', 'wrote book']
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happend))
