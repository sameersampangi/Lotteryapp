#usert inputs the numbers, if match found, multiply it with 10
import random
import logging


#class Value_smallError(object):
 #   pass


class Lottery(object):

    def __init__(self, numb):
        self.numb = numb


    def add_numbers(self):
        y = set()
        z = len(y)

        while z < self.numb:
            #print(self.numb)
            try:
                x = int(input("Play:Enter a number in range (1,20):"))
                if x<=20:
                    y.add(x)
                    z = len(y)
                else:
                    raise Value_small
                    #print(("z:",z))
            except Value_small:
                    print("Enter value less than 20")

            #y.add(x)


        return y



    def generate_numbers(self):

        a = set()

        while len(a) <6:
            y = random.randint(1,20)
            a.add(y)
            print(len(a))

        return a





'''
    def money_won(self):
        a = self.addnumbers()
        b = self.generate_numbers()
        print("The added numbers are:", a)
        print("The randomly generated numbers are", b)
        y = len(a.intersection(b)) * 10

        return y
'''

#a = Lottery(6)
#print(a.money_won())


class Value_small(Exception):
    pass



