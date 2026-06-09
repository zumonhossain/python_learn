
cities = ['Tokyo', 'Osaka', 'Kyoto']
seasons = ['Spring', 'Summer', 'Autumn', 'Winter']

# 3D List: [city][season][measurement]
# measurement = [temperature, humidity, rainfall]

weather = [
    [   
        [18, 60, 120],
        [34, 80, 180],
        [22, 65, 140],
        [8, 50, 60]
    ],
    [   
        [20, 62, 110],
        [36, 82, 170],
        [24, 64, 130],
        [9, 52, 55]
    ],
    [   
        [19, 61, 105],
        [35, 79, 165],
        [23, 63, 125],
        [7, 51, 50]
    ]
]

print("==========================================")
print("WEATHER REPORT")
print("==========================================")

c = 0

highest_rainfall = 0
highest_rain_city = ""

while c < len(weather):
    print(f"City: {cities[c]}")

    s = 0
    hottest_temp = 0
    hottest_season = ""

    total_rain = 0

    while s < len(weather[c]):
        temp = weather[c][s][0]
        humidity = weather[c][s][1]
        rain = weather[c][s][2]

        print(f"{seasons[s]} | Temp: {temp}C Humidity: {humidity}% Rain: {rain}mm")

        # Hottest season check
        if temp > hottest_temp:
            hottest_temp = temp
            hottest_season = seasons[s]

        # Total rainfall
        total_rain += rain

        s += 1

    print(f"Hottest season: {hottest_season} ({hottest_temp}C)")

    # Check highest rainfall city
    if total_rain > highest_rainfall:
        highest_rainfall = total_rain
        highest_rain_city = cities[c]

    c += 1

print(f"City with highest annual rainfall: {highest_rain_city} ({highest_rainfall}mm)")