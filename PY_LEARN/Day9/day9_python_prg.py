gaurav_dictonary = {
    "Gaurav" : "Husband of Anjula",
    "Anjula" : "Wife of Gaurav",
    "Atharva" : "Elder Son of Gaurav and Anjula",
    "Yatharth" : "Youngest son of Gaurav and Anjula"
}

gaurav_dictonary["Gaurav"] = "Smartest husband as per Anjula"

# print(gaurav_dictonary)


# for dict in gaurav_dictonary:
    # print(dict)
    # print(gaurav_dictonary[dict])

travel_log = {
    "India":{
        "cities_visited": ["Varanasi", "Hyderabad","Chennai"],
        "total_visits" : 12
        },
    "United States" : {
        "cities_visited":["California", "New York", "Utah"], 
        "total_visits": 5
        }
}

travel_log1 = [
    {
        "country" : "France",
        "cities_visited": ["Varanasi", "Hyderabad","Chennai"],
        "total_visits" : 12
    },
    {
        "country" : "United States",
        "cities_visited": ["California", "New York", "Utah"],
        "total_visits" : 5
    }
]

for i in travel_log1:
    print(i)