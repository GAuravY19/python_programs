import phonenumbers 
from phonenumbers import carrier, geocoder, timezone

    
def phone_num(number):
    phone = phonenumbers.parse(number)
    time = timezone.time_zones_for_number(phone)
    car = carrier.name_for_number(phone, "en")
    reg = geocoder.country_name_for_number(phone, "en")
    print(phone)
    print(time)
    print(car)
    print(reg)


number = input("Enter Your number :- ")
phone_num(number)
