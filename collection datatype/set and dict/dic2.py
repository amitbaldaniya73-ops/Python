person = {
    "name" :"amit",
    "rollno":10,
    "std":"3rd sem",
    }
print(person)
person['city']="surat"
print(person)
print(person["name"])
print(person.get("school"))
person.pop('city')
print(person)
del person['rollno']
print(person)

print(person.keys())
print(person.values())
