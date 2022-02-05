# by Kami Bigdely
# Inline method.
LEGAL_DRINKING_AGE = 18


class Person:
    def __init__(self, my_age):
        self.age = my_age
        

def enter_night_club(person):
  
    if person.age > LEGAL_DRINKING_AGE:
      print("Allowed to enter.")
    else:
      print("Enterance of minors is denited.")
    
person = Person(17.9)
enter_night_club(person)