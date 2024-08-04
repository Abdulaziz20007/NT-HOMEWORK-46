import json

class Cars():
    def __init__(self) -> None:
        file = open('data.json')
        data = json.load(file)
        file.close()
        self.cars = []
        self.cars.extend(data)
    
    def add(self, ls):
        self.cars.append(ls)

    def get(self):
        print(self.cars)
    
    def persentage(self):
        males = 0
        females = 0
        for person in self.cars:
            gender = person['gender'].lower()
            if gender == 'm' or gender == 'male':
                males += 1
            elif gender == 'f' or gender == 'female':
                females += 1
        if males + females > 0:
            print((males / males+females) * 100)
            print((females / males+females) * 100)
    
    def most_car_country(self):
            brand_count = {}
            country_count = {}

            for car in self.cars:
                brand = car['brand']
                country = car['country']

                if brand not in brand_count:
                    brand_count[brand] = 0
                    country_count[brand] = {}

                brand_count[brand] += 1

                if country not in country_count[brand]:
                    country_count[brand][country] = 0

                country_count[brand][country] += 1

            most_brand = max(brand_count, key=brand_count.get)
            country_counts = country_count[most_brand]

            most_country = max(country_counts, key=lambda k: country_counts[k])
            least_country = min(country_counts, key=lambda k: country_counts[k])

            print(f"Eng ko'p mashinasi bor brend: {most_brand}.")
            print(f"Eng ko'p {most_brand} si bor davlat: {most_country}.")
            print(f"Eng kam {most_brand} si bor davlat:  {least_country}.")
    
    def message_for_old_car_drivers(self):
        for i in self.cars:
            y = i['year']
            if y < 2005:
                file = open(f"./messages/{i['first_name']}_{i['last_name']}_{i['id']}.txt", 'w')
                file.write("Kimdan: Auto Test Corp.\n")
                file.write(f"Kimga: {i['first_name']} {i['last_name']}\n")
                file.write(f"Joriy davlat: {i['country']}\n")
                file.write(f"Hurmatli {i['first_name']} {i['last_name']}! {i['brand']} tomonidan {y}da ishlab chiqarilgan {i['color']} rangli avtoulovingiz Texnik Holatini tekshirtirsh maqsadida mahalliy Auto Test Corp. ofisiga murojaat qilishingizni so’raymiz!\n")
                file.close()

def add_car_to_cars():
    car = {
        'id': int(input("Id: ")),
        'first_name': input("First name: "),
        'last_name': input("Last name: "),
        'gender': input("Gender: "),
        'brand': input("Brand: "),
        'year': int(input("Year: ")),
        'color': input("Color: "),
        'country': input("Country: ")
    }
    return car


carrrr = Cars()

carrrr.add(add_car_to_cars())
carrrr.get()
carrrr.persentage()
carrrr.message_for_old_car_drivers()