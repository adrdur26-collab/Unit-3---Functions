def generate_username(first, last):
    username = first[0].lower() + last.lower()
    if len(last) < 5:
        username += "1"
    return username

print(generate_username("Alex", "Chen"))
print(generate_username("Sam", "Li"))
print(generate_username("Jordan", "Kim"))


def playlist_length(songs, avg_duration):
    total_minutes = len(songs) * avg_duration
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)
    return f"{hours}h {minutes}m"

print(playlist_length(["Thunder", "Believer"], 3.5)) 
print(playlist_length(["Shape of You", "Despacito", "Closer"], 4))



def battle_cry(hero, weapon, damage):
    return f"{hero.upper()} swings {weapon.upper()} for {damage} damage!"

print(battle_cry("Draco", "Fire Sword", 95))