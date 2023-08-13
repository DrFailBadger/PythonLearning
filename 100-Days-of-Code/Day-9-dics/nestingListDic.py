# capitals ={
#     "france": "Paris",
#     "Germany": "Berlin"
# }
# travel_log = {
#     "France": ["Paris","Lille","Dijon"]
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }

# ["A","B",["C","D"]]

#Nest Dic in Dic

travel_log = {
    "France": {"Cities_Visited": ["Paris","Lille","Dijon"], "Total_Visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}
print(travel_log)



#nestin dic in a list
travel_log1 = [
    {
        "Country": "France",
        "Cities_Visited": ["Paris","Lille","Dijon"], 
        "Total_Visits": 12
    },
    {
        "Country": "Germany", 
        "Cities_Visited": ["Berlin","Hamburg","Stuttgart"], 
        "Total_Visits": 5
    },
]
print(travel_log1)
