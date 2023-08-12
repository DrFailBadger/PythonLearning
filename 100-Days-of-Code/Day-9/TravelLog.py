travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]





def add_new_country(coun, vis, citi):
    print(coun, vis, citi)
    travel_log.append({"Country": coun, "visits": vis, "cities":[citi]})

#### tutors solution
def add_new_country(country_visited, times_visited, cities_visited):
    
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

#travel_log.append({"country" : "Russia", "visits": 10, "Cities":["St pete","Mos"]})


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

add_new_country("United Kingdom", 1, ["London"])
print(travel_log)
