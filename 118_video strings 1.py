
#video deep dive strings


def l():
  print(" ")
l()

hoppa="hoppa"
hups="hups"

print ("multiline strings heb een zin gemaakt van twee regels")
bericht="""
hallo 
daar gaan we weer
"""
print(bericht)
l()

print("de lengte van een string de lengte van bericht")
print(f"de lengte van bericht is ",len(bericht))
print("")

print("indexing")

print(f"hoppa[0]  de eerste letter van de string hoppa is ", hoppa[0])
l()

print("negative indexing begint bij laatste karakter")
print(f"de laatste letter van de string hoppa is ", hoppa[-1])
l()

print("slicing let op van tot de tot is de positie van de laatste p in dit geval")
print(f"de eerste drie letters van hoppa zijn ",hoppa[0:3], "en de laatste twee ",hoppa[3:])
l()

print("slicing with a step eerste nummer zit er in tweede nummer zit er niet in hoppa [1:4]")
print(f"wil opp   hebben van hoppa        ", hoppa[1:4])
l()

print(f"hoppa[::-1])  geeft reverse hoppa > ",hoppa[::-1])
l()

o=1
a=4
print(f"o=1 a=4 hoppa[o:a])  geeft opp > ",hoppa[o:a])
l()

aanmoediging=hoppa+" "+hups
print(f"mijn aanmoediging > ",aanmoediging)
l()

print(f"vergelijking van hups en hoppa print(hups == hoppa)  >",hups == hoppa )
print(f"zit ups in hups? >  geeft True","ups" in hups )
l()

haps=hups.replace('u','a')
print(f"haps=hups.replace('u','a') dus van hups naar haps > ",haps)
l()

hups=haps
print(f"hups=haps  hups wordt haps > ",hups)
l()

