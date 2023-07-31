name = "ivan"
print(f"Hello {name.capitalize()}, have a nice day")
print(name.lower())
print(name.upper())
print(f'{name.capitalize()} say "Have a nice day".')
spaced = "    ivan spaced   "
unspaced = spaced.strip()
print (f"This is without strip {spaced} hoho")
print (f"This is leftstrip strip {spaced.lstrip()} hoho")
print (f"This is rightstrip {spaced.rstrip()} hoho")
print (f"This is left and rightstrip {spaced.strip()} hoho")
print (f"This is capitalized and strip and newline \n{unspaced.capitalize()} hoho")