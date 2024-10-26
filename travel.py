from tabulate import tabulate
import requests
import dest

def main():
    print("\n\nHello and Welcome to Travel Booker!\n\n")
    print(tabulate(dest.dict, tablefmt="double_grid"), "\n")

    choice = destination()
    for item in dest.dict:
        if item[0] == choice: location = (item[1])
    print(f"\nYou've selected **{location}**")

    home = start()
    airport_name = dest.airports[home]['name']
    print(f"You've selected **{airport_name}** as your starting airport.")
    
    depart, arrive = dates()
    a, c, i = person()
    interior = cabin()
    key = dest.key

    airport_info = next((item for item in dest.list if item[0] == choice), None)
    if airport_info: 
        away = airport_info[1]
    
    link = (f'https://serpapi.com/search.json?engine=google_flights&departure_id={home}&arrival_id={away}&gl=us&hl=en&currency=USD&type=1&outbound_date={depart}&return_date={arrive}&travel_class={interior}&adults={a}&children={c}&infants_in_seat={i}&api_key={key}')
    resp = requests.get(link)
    dict = resp.json()

    flight_choice = flights(dict)

    city, country = location.split(",")
    city = city.replace(" ", "+") 
    co, sort, minp, maxp = hotelprompt()
    
    hlink = (f"https://serpapi.com/search.json?engine=google_hotels&q={city}&gl=us&hl=en&currency=USD&check_in_date={arrive}&check_out_date={co}&adults={a}&sort_by={sort}&min_price={minp}&max_price={maxp}&api_key={key}")
    hresp = requests.get(hlink)
    hdict = hresp.json()

    hotel_choice = hotels(hdict)

    print(f"Congratulations! You have made your travel arrangements! Here is a reminder of what you selected\n\n{flight_choice}\n\n{hotel_choice}\n\nHappy Travels!")

def destination():
    choice = input("Where would you like to travel to? (Pick a number 1-15) ")
    while True:
        try:
            if 1 <= int(choice) <= 15:
                return int(choice)
            else:
                choice = input("Please pick a number 1 - 15 that corresponds to where you would like to go! ")
        except:
            choice = input("Please pick a number 1 - 15 that corresponds to where you would like to go! ")

def start():
    homeport = input("Please enter the IATA code of your home airport (For example: John F. Kennedy International Airport is JFK) ").upper()
    while True:
        try:
            if homeport in dest.airports:
                return homeport
            else:
                homeport = input("No US airport seems to match that airport code. Please re-enter your home airport's IATA code: ").upper()
        except:
            homeport = input("No US airport seems to match that airport code. Please re-enter your home airport's IATA code: ").upper()

def dates():
    departure = input("Please enter date of departure (YYYY-MM-DD) ")
    arrival = input("Please enter date of arrival (YYYY-MM-DD) ")
    return departure, arrival

def person():
    adult = input("Please enter the number of adults: ")
    child = input("Please enter the number of children: ")
    infant = input("Please enter the number of infants: ")
    return adult, child, infant

def cabin():
    print("Please enter the class of the seat\n(1) Economy\n(2) Premium Economy\n(3) Business\n(4) First ")
    cabin = input('Please enter "1", "2", "3", or "4" to select your choice: ') 
    return cabin

def flights(data):
    mess1 = ""
    airline1 = data["best_flights"][0]["flights"][1]["airline"]
    num1 = data["best_flights"][0]["flights"][1]["flight_number"]
    mins = data["best_flights"][0]["flights"][1]["duration"]
    dur1 = int(mins/60)
    dur1 = f"{dur1} Hours, {mins%60} Minutes"        
    time1 = data["best_flights"][0]["flights"][1]["departure_airport"]["time"][-5:]
    feat1 = data["best_flights"][0]["flights"][1]["extensions"]
    for x in feat1: mess1 += f"{x}, "
    price1 = data["best_flights"][0]["price"]
    flight1 = f"\nFlight Option 1:\n - Airline: {airline1}\n - Flight Number: {num1}\n - Time: {[time1]}\n - Duration: {dur1}\n - Features: {mess1}\n - Price: ${price1}\n\n"
    print(flight1)

    mess2 = ""
    airline2 = data["best_flights"][1]["flights"][0]["airline"]
    num2 = data["best_flights"][1]["flights"][0]["flight_number"]
    mins2 = data["best_flights"][1]["flights"][0]["duration"]
    dur2 = int(mins2/60)
    dur2 = f"{dur2} Hours, {mins2%60} Minutes"  
    time2 = data["best_flights"][1]["flights"][0]["departure_airport"]["time"][-5:]
    feat2 = data["best_flights"][1]["flights"][0]["extensions"]
    for x in feat2: mess2 += f"{x}, "
    price2 = data["best_flights"][1]["price"]
    flight2 = f"Flight Option 2:\n - Airline: {airline2}\n - Flight Number: {num2}\n - Time: {[time2]}\n - Duration: {dur2}\n - Features: {mess2}\n - Price: ${price2}\n\n"
    print(flight2)

    mess3 = ""
    airline3 = data["best_flights"][2]["flights"][0]["airline"]
    num3 = data["best_flights"][2]["flights"][0]["flight_number"]
    mins3 = data["best_flights"][2]["flights"][0]["duration"]
    dur3 = int(mins3/60)
    dur3 = f"{dur3} Hours, {mins3%60} Minutes"  
    time3 = data["best_flights"][2]["flights"][0]["departure_airport"]["time"][-5:]
    feat3 = data["best_flights"][2]["flights"][0]["extensions"]
    for x in feat3: mess3 += f"{x}, "
    price3 = data["best_flights"][2]["price"]
    flight3 = f"Flight Option 3:\n - Airline: {airline3}\n - Flight Number: {num3}\n - Time: {[time3]}\n - Duration: {dur3}\n - Features: {mess3}\n - Price: ${price3}\n\n"
    print(flight3)

    answer = input("Which flight would you like to select? (1, 2, or 3): ")
    
    if answer == 1: return flight1
    elif answer == 2: return flight2
    else: return flight3

def hotelprompt():
    miniumum = input("Enter a minimum price (Do not include dollar signs): ")
    maxiumum = input("Enter a maximum price (Do not include dollar signs): ")
    checkout = input("When would you like to checkout of the hotel? (YYYY-MM-DD) ")

    sort = input("Would you like to sort by lowest price (1), highest rating (2), or most reviewed (3): ")
    if sort == 3: sort = 13
    elif sort == 2: sort = 8
    else: sort = 3

    return checkout, sort, miniumum, maxiumum

def hotels(data):
    name1 = data["properties"][0]["name"]
    description1 = data["properties"][0]["description"] 
    checkin1 = data["properties"][0]["check_in_time"] 
    checkout1 = data["properties"][0]["check_out_time"] 
    rating1 = data["properties"][0]["overall_rating"] 
    reviews1 = data["properties"][0]["reviews"] 
    hotelclass1 = data["properties"][0]["hotel_class"]
    totalprice1 = data["properties"][0]["total_rate"]["lowest"] 
    rateprice1 = data["properties"][0]["rate_per_night"]["lowest"]  
    amenities1 = data["properties"][0]["amenities"] 
    link1 = data["properties"][0]["link"]
    hotel1 = f"\Hotel Option 1:\n - Name: {name1}\n - Description: {description1}\n - Check-In: {checkin1}\n - Check-Out: {checkout1}\n - Rating: {rating1}\n - Reviews: {reviews1}\n - Class: {hotelclass1}\n - Total Price: ${totalprice1}\n - Rate per Night: ${rateprice1}\n - Features: {amenities1}\n - Link: {link1}\n\n"
    print(hotel1)

    name2 = data["properties"][1]["name"]
    description2 = data["properties"][1]["description"] 
    checkin2 = data["properties"][1]["check_in_time"] 
    checkout2 = data["properties"][1]["check_out_time"] 
    rating2 = data["properties"][1]["overall_rating"] 
    reviews2 = data["properties"][1]["reviews"] 
    hotelclass2 = data["properties"][1]["hotel_class"]
    totalprice2 = data["properties"][1]["total_rate"]["lowest"] 
    rateprice2 = data["properties"][1]["rate_per_night"]["lowest"]  
    amenities2 = data["properties"][1]["amenities"] 
    link2 = data["properties"][1]["link"]
    hotel2 = f"\Hotel Option 1:\n - Name: {name2}\n - Description: {description2}\n - Check-In: {checkin2}\n - Check-Out: {checkout2}\n - Rating: {rating2}\n - Reviews: {reviews2}\n - Class: {hotelclass2}\n - Total Price: ${totalprice2}\n - Rate per Night: ${rateprice2}\n - Features: {amenities2}\n - Link: {link2}\n\n"
    print(hotel2)

    name3 = data["properties"][1]["name"]
    description3 = data["properties"][1]["description"] 
    checkin3 = data["properties"][1]["check_in_time"] 
    checkout3 = data["properties"][1]["check_out_time"] 
    rating3 = data["properties"][1]["overall_rating"] 
    reviews3 = data["properties"][1]["reviews"] 
    hotelclass3 = data["properties"][1]["hotel_class"]
    totalprice3 = data["properties"][1]["total_rate"]["lowest"] 
    rateprice3 = data["properties"][1]["rate_per_night"]["lowest"]  
    amenities3 = data["properties"][1]["amenities"] 
    link3 = data["properties"][1]["link"]
    hotel3 = f"\Hotel Option 1:\n - Name: {name3}\n - Description: {description3}\n - Check-In: {checkin3}\n - Check-Out: {checkout3}\n - Rating: {rating3}\n - Reviews: {reviews3}\n - Class: {hotelclass3}\n - Total Price: ${totalprice3}\n - Rate per Night: ${rateprice3}\n - Features: {amenities3}\n - Link: {link3}\n\n"
    print(hotel3)

    answer = input("Which hotel would you like to select? (1, 2, or 3): ")
    
    if answer == 1: return hotel1
    elif answer == 2: return hotel2
    else: return hotel3

if __name__ == "__main__":
    main()