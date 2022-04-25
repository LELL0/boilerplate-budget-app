class Category:

    def __init__(self, categoryName):
        self.categoryName = categoryName
        self.ledger = list()
        self.balance = 0

    def deposit(self, amount, description=''):
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, categ):
        if(self.check_funds(amount)):
            self.withdraw(amount, "Transfer to "+categ.categoryName)
            categ.deposit(amount, "Transfer from "+self.categoryName)
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.balance

    def __repr__(self):
        output = self.categoryName.center(30, '*') + '\n'
        for data in self.ledger:
            output += data["description"][:23].ljust(23, ' ') + str(
                format(data["amount"], '.2f'))[:7].rjust(7, ' ')+'\n'
        output += 'Total: '+format(self.balance, '.2f')
        return output


def create_spend_chart(categories):
    categoryWithdraw = list()
    catNames = list()
    totalAmount = 0
    bar_chart = 'Percentage spent by category'

    for category in categories:
        catNames.append(category.categoryName)
        totalWithdrawTemp = 0
        for data in category.ledger:
            if(data['amount'] < 0):
                totalWithdrawTemp -= int(data['amount'])
        categoryWithdraw.append(totalWithdrawTemp)
        totalAmount += totalWithdrawTemp

    for i in range(len(categories)):
        categoryWithdraw[i] = int(categoryWithdraw[i]*10/totalAmount)*10

        # adding the purcentages
    for purcentage in range(10, -1, -1):
        purcentage *= 10

        bar_chart += '\n' + str(purcentage).rjust(3)+'| '
        for i in range(len(categoryWithdraw)):
            if(categoryWithdraw[i] >= purcentage):
                bar_chart += 'o  '
            else:
                bar_chart += '   '

        # adding the ------
    bar_chart += '\n    '+'---'*len(categoryWithdraw)+'-'

    # adding the cat names vertically
    longestwordLen = len(max(catNames, key=len))
    for i in range(len(catNames)):
        catNames[i] = list(catNames[i].ljust(longestwordLen, ' '))

    for i in range(longestwordLen):
        bar_chart += '\n    '
        for j in range(len(catNames)):
            bar_chart += ' '+catNames[j][i]+' '
        bar_chart += ' '

    return bar_chart
