class Bot:
    def __init__(self):
        self.boughtPrice = 0
        self.soldPrice = 0
        self.money = 100
        self.previousStock = ""
        self.id = 0
        self.dontBuy = False

    def buy(self, price):
        if self.dontBuy == True:
            pass

        else:
            self.boughtPrice = 0
            self.previousStock = ""
            self.previousStock += price[self.id][1]
            self.money -= int(price[self.id][0])
            self.boughtPrice += int(price[self.id][0])
            self.dontBuy = True

    def sell(self, price):
        if self.boughtPrice * 1.01 == int(price[self.id][0]):
            self.money += int(price[self.id][0])
            self.dontBuy = False

    def findLowest(self, prices):
        if prices[0][1] == self.previousStock:
            self.dontBuy = True

        else:
            self.id = 0
            self.dontBuy = False

        # Python3 program for Bubble Sort Algorithm Implementation

    def sortStocks(self, arr):
        n = len(arr)

        # For loop to traverse through all
        # element in an array
        for i in range(n):
            for j in range(0, n - i - 1):
                # Range of the array is from 0 to n-i-1
                # Swap the elements if the element found
                # is greater than the adjacent element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
