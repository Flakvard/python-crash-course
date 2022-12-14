def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first':first_name, 'last': last_name}
    return person
musician = build_person('jimi','henrix')
print(musician)


def get_formatted_name(first_name, last_name):
    """return a full name, neatly formatted."""
    full_name = (f"{first_name} {last_name}")
    return full_name.title()

#this is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


