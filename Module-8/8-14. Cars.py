def make_car(manufacturer, model, **car_information):
    """Create a dictionary for info about a car"""
    car_information['manufacturer'] = manufacturer
    car_information['model'] = model
    return car_information

car = make_car('bmw', 'm3', 
				color='silver',
				sunroof=True)
print(car)
