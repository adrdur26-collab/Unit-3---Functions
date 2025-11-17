def generate_hashtag(phrase):
    titled = phrase.title()
    no_spaces = titled.replace(" ", "")
    hashtag = "#" + no_spaces

    if len(hashtag) > 20:
        return"TOO LONG"
    return hashtag


print(generate_hashtag("hello world"))
print(generate_hashtag("python is fun"))



def battle_cry(hero, weapon, damage):
    message = f"{hero.upper()} swings {weapon.upper()} for {damage} damage!" 
    if damage > 80:
        message += " CRITICAL HIT!"
    return message


print(battle_cry("Draco", "Fire Sword", 95))
print(battle_cry("Luna", "Ice Dagger", 65))




def weather_alert(temp, wind_speed):
    alert = ""
    if temp > 30:
        alert += "STAY HYDRATED"
    if temp < 5:
        if alert:
            alert += " + "
        alert += "BUNDLE UP"
    if wind_speed > 40:
        if alert:
            alert += " + "
        alert += "HOLD ON TO YOUR HAT"

    if not alert:
        return "ENJOY THE WEATHER"
    return alert

print(weather_alert(35, 15))
print(weather_alert(2, 50))