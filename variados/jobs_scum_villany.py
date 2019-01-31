# Job Generator Scum and Villany
import random


Jobs = ["Abduction", "Assassination", "Assault", "Assault", "Burglary", "Espionage",
        "Exploration", "Hijacking", "Investigation", "Repair", "Rescue", "Robbery",
        "Sabotage", "Salvage", "Salvage", "Scam", "Shipjacking", "Smuggling", "Smuggling", "Smuggling"]

for x in range(1, 10):
    k = random.randrange(1, 20)
    print(Jobs[k])
