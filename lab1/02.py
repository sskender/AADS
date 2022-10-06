person_data = {
    "Ana": 1995,
    "Zoran": 1978,
    "Lucija": 2001,
    "Anja": 1997
}

for key in person_data:
    person_data[key] -= 1

print(person_data)

year_age = []
for key in person_data:
    tpl = (person_data[key], 2022 - person_data[key])
    year_age.append(tpl)

print(year_age)
