# Write your solution here
def oldest_person(people: list):
    oldest_person = ""
    max_age = 0
    for person in people:
        age = 2026 - person[1]
        if age > max_age:
            max_age = age
            oldest_person = person[0]
    return oldest_person

if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))