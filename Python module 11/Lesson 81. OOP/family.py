class Family:

    def __init__(self, family_name: str, family_funds: int, house: str):
        self.family_name = family_name
        self.family_funds = family_funds
        self.house = house

    def information(self):
        print(f'Family name: {family.family_name}\nFamily funds: {family.family_funds}\nHaving a house: {family.house}')

    def earn(self, earn):
        self.family_funds += earn
        print(f'Earned money! Current value: {self.family_funds}')

    def buy_house(self):
        print('Try to buy a house')

        if self.family_funds < 900000:

            print('Not enough money!')
        else:
            print('House purchased!')
            self.family_funds -= 900000
            family.house = 'True'


family = Family('Common family', 100000, 'False')
family.information()
family.buy_house()
family.earn(800000)
family.buy_house()
family.information()
