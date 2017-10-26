def hotel_cost(nights):
    return(70 * nights)


def plane_ticket_cost(city,seat_class):
    ticket_cost = 0
    multiplier = 0

    if city = "New York":
        return("The ticket costs £2000")
    elif city = "Auckland":
        return("The ticket costs £790")
    elif city ="Venice":
        return ("The ticket costs £154")
    elif city = "Glasgow":
        return ("The ticket costs £65")
    else: "We do not offer other destinations"

    if seat_class == "Economy class":
        multiplier = 1
    elif seat_class == "Premium class":
        multiplier = 1.3
    elif seat_class == "Business class"
        multiplier = 1.6
    elif seat_class == "First class":
        multiplier = 1.9

    ticket_cost *= multiplier
    return (ticket_cost)

def rental_car_cost(days):
    daily_cost = 30
    total_cost = days * daily_cost
    if days > 7:
        total_cost-=50
    elif days > 3:
        total_cost-=30
    return(total_cost)

def total_cost (city,days)
