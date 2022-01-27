# By Kami Bigdely
# PEP8 - whitespaces and variable names.


class Pizza:

    def __init__ (obj, my_bread_type, cheese_type, meat_type, pizza_toppings, size):
        self.bread_type = my_bread_type
        self.cheese_type = cheese_type
        self.meat_type = meat_type
        self.toppings = pizza_toppings
        self.size = size        

    @classmethod
    def create_chicago_pizza (class_type, size):
        bread = 'deep-dish bread'
        cheese = 'mozzarella cheese'
        meat_type = 'Italian sausage'
        toppings = ['green bell pepper', 'mushroom', 'chunky tomato sauce', 'onion']
        return class_type (bread, cheese, meatType, toppings, size) 

    @classmethod
    def create_california_pizza(ct, meat_type, size):
        self.bread_type = 'thin crust'
        self.cheese_type = 'feta cheese'
        self.toppings = ['garlic', 'spinach', 'broccoli', 'olives', 'red onion', 'red bell pepper']
        return ct(bread, cheese_type, meat_Type, toppings, size) 

    @classmethod
    def print_info(obj):
        print('bread type is: ', obj.bread_type)
        print('cheese type is: ', obj.cheese_type)
        print('meat type is: ', obj.meat_type)
        print('Toppings are: ', end = '')
        print(', '.join(map(str, obj.toppings)))

    
my_pizza = pizza.create_california_pizza('chicken', 'large')
my_pizza.print_info()