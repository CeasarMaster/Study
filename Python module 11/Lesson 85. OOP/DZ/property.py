class Property:

    def __init__(self, worth):
        self.worth = worth

    def calc_taxes(self):
        return 0


class Apartment(Property):
    def calc_taxes(self):
        return self.worth / 1000


class Car(Property):
    def calc_taxes(self):
        return self.worth / 200


class CountryHouse(Property):
    def calc_taxes(self):
        return self.worth / 500


money = int(input('How much money?: '))
sum_taxes = 0

apartment_worth = int(input('How much is the apartment worth?'))
apartment = Apartment(apartment_worth)
apartment_tax = apartment.calc_taxes()
print(f'Apartment tax: {apartment_tax}')
sum_taxes += apartment_tax

car_worth = int(input('How much is the car worth?'))
car = Car(car_worth)
car_tax = car.calc_taxes()
print(f'Car tax: {car_tax}')
sum_taxes += car_tax

country_worth = int(input('How much is the country house worth?'))
country_house = CountryHouse(country_worth)
country_house_tax = country_house.calc_taxes()
print(f'Country House tax: {country_house_tax}')
sum_taxes += country_house_tax
print(f'Sum of taxes: {sum_taxes}')
if money < sum_taxes:
    print('Not enough money to pay the taxes! Go work!')
