from lottery import Lottery




class LotteryApp(Lottery):
    def __init__(self):
    #    Lottery.__init__(self,numb=6)

        Lottery.__init__(self,6)  # constructor inheritance


    def money_won(self):
        a = self.add_numbers()
        b = self.generate_numbers()
        #a = Lottery.add_numbers(self)
        #b = Lottery.generate_numbers(self)
        print("The added numbers are:", a)
        print("The randomly generated numbers are", b)
        #y = #len
        y= len(a.intersection(b)) * 10

        return y


a = LotteryApp()
print(a.money_won())
