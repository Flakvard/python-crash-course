guestlist = ['James', 'Edward', 'Richard','Fred']
nr1message = f"Hello {guestlist[0].title()}, I would like to invite you to dinner."
nr2message = f"Hello {guestlist[1].title()}, I would like to invite you to dinner."
nr3message = f"Hello {guestlist[2].title()}, I would like to invite you to dinner."
nr4message = f"Hello {guestlist[3].title()}, I would like to invite you to dinner."
print(nr1message)
print(nr2message)
print(nr3message)
print(nr4message)

print(f"\n{guestlist[0].title()}, could not make it to the dinner")

del(guestlist[0])

print (guestlist)
print(nr2message)
print(nr3message)
print(nr4message)

guestlist.insert(0,'Peter')
guestlist.insert(2,'Jakup')
guestlist.append('Matthew')
print (guestlist)

for guest in guestlist[:]:
    print(f"{guest}, is invited to the dinner")

