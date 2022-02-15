# By Kami Bigdely
# Decompose conditional: You have a complicated conditional(if-then-else) statement. Extract
# methods from the condition, then part, and else part(s).

def make_alert_sound():
    print('made alert sound.')
def make_accept_sound():
    print('made acceptance sound')
def check_ingredients(chemicals, ingredients):
    for c in chemicals:
        if c in ingredients:
            return True
        return False

ingredients = ['sodium benzonate']
chemicals = ['sodium nitrate', 'sodium benzonate', 'sodium oxide']
if check_ingredients(chemicals, ingredients):
    print('!!!')
    print('there is a toxin in the food!')    
    print('!!!')
    make_alert_sound()
else:
    print('***')
    print('Toxin Free')
    print('***')
    make_accept_sound()