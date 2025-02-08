from bs4 import BeautifulSoup

def parse_weather():
    with open("weather.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        
    weather_data = []
    rows = soup.find("tbody").find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        day = cols[0].text
        temp = int(cols[1].text.replace("C", ""))
        condition = cols[2].text
        weather_data.append({"day": day, "temperature": temp, "condition": condition})
    
    for entry in weather_data:
        print(f"{entry['day']}: {entry['temperature']}C, {entry['condition']}")

    hottest_day = max(weather_data, key=lambda x: x['temperature'])
    print(f"\nHottest day: {hottest_day['day']} ({hottest_day['temperature']}C)")

    sunny_days = [entry['day'] for entry in weather_data if entry['condition'] == "Sunny"]
    print("Sunny days:", ", ".join(sunny_days))

    avg_temp = sum(entry['temperature'] for entry in weather_data) / len(weather_data)
    print(f"Average Temperature: {avg_temp:.2f}C")

if __name__ == "__main__":
    parse_weather()
