user = {
    "name": "Miguelangel",
    "lastname":"Restrepo", 
    "age": 18, 
    "city": "Medellín",
    "ocupation": "Estudiante",
    "email": "migue200707@gmail.com",
    }

print(user["lastname"])
print(f"Hola, mi nombre es {user["name"]} {user["lastname"]}, tengo {user["age"]} años, vivo en {user["city"]}, soy {user["ocupation"]} y mi correo es {user["email"]}.")

lang = ["Python", 10,   "JavaScript", "C++", "Java", "Ruby", "Go"]

print(lang[0])
print(lang[1])
print(lang[2])
print(lang[3])
print(lang[4])

for x in lang:
    print(x)

print(type(lang))
print(type(user))

x = 10
y = 3.5
z = "Hola"

print(type(x), type(y), type(z))