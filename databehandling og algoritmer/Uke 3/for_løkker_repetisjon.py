actors = [
    {"name": "Tom Hanks", "age": 66},
    {"name": "Meryl Streep", "age": 73},
    {"name": "Leonardo DiCaprio", "age": 48},
    {"name": "Julia Roberts", "age": 55},
    {"name": "Denzel Washington", "age": 67},
    {"name": "Nicole Kidman", "age": 55},
    {"name": "Brad Pitt", "age": 59},
    {"name": "Charlize Theron", "age": 47},
    {"name": "Johnny Depp", "age": 59},
    {"name": "Emma Stone", "age": 34},
]

# oppgaver:
# 1: print navnet til tom hanks
# print(actors[0]["name"])
# # print alderen til tom hanks
# print(actors[0]["age"])

# brukerinput = int(input("gi meg et nummer:"))
# print(actors[brukerinput]["name"])

størst = float("-inf")
størst_navn = "kai cenat"

for actor in actors:
    print(f"{actors['name']} er {actor['age']} år gammel")
    if actor["age"] > størst:
        størst = actor["age"]
        størst_navn = actor["navn"]

print(f"Den eldste skuespilleren er {størst_navn} som er {størst} år gammel")

eldst = actors[0]
for actor in actors:
    if actor['age'] > eldst['age']:
        eldst = actor

print(f"den eldste skuespilleren er {eldst['name']}")


actor = actors[1]
print(actor)
actor = actors[2]
print(actor)
actor = actors[3]
print(actor)