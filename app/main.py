class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = [Person(person["name"], person["age"]) for person in people]

    for index, person in enumerate(people):
        if person.get("wife"):
            wife_name = person["wife"]
            persons_list[index].wife = Person.people[wife_name]
        if person.get("husband"):
            husband_name = person["husband"]
            persons_list[index].husband = Person.people[husband_name]

    return persons_list
