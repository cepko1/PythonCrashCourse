guests = ['newton','tesla','edisson']
for name in guests:
	print (f"Hello {name.capitalize()}. Wellcome at the party.")
cantbe = 'tesla'
guests.remove(cantbe)
print ()
print (f"{cantbe.capitalize()} is busy and can't come.")
for name in guests:
	print(f"Welcome {name.capitalize()}")
new1 = "einstain"
new2 = "elon mask"
new3 = "bill gates"
print ("Atention for all. We found bigger table and we'll have more guests")
guests.insert(0,new1)
guests.insert (2,new2)
guests.append(new3)
print ("Welcome")
for n in guests:
	print(n.title())
print ("Oh, we so sorry, but we have not enough space for all guests. Only two place avaliable")
while len(guests) >2:
	poped = guests.pop()
	print (f"{poped.title()} sorry, but see you another time")
for n in guests:
	print(f"{n.title()} we still wait for you")
while len(guests) > 0:
	del guests[0]
print (guests, len(guests))