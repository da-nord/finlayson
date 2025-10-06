#video deep dive strings

def l():
  print(" ")
l()

print(f"4>3? ",4>3)
print(f"is een komma groter dan een punt? ", ",">".")
print(f"ord(a) geeft ascii code van a   4:56", ord("a"))

hoppa="hoppa"
hups="hups"
string="123456789"

print("of string 123456789 result must be 678    6789 is -4 -3 -2 -1   TO 9")
print(f"string 123456789 slicing from the end: ",string[-4:-1])
l()

print(f"hoppa<hups   klopt dat   ja want ho komt voor hu", hoppa<hups)
print(f"hoppa==hups   klopt dat   nee want hoppa is niet gelijk aan hups", hoppa==hups)
l()

print("7:40")
print(f"membership tests zit C in Code?  geeft TRUE ","C" in "Code")
print(f"membership tests zit c in Code?  geeft FALSE","c" in "Code")
print(f"membership tests zit c niet in code?  geeft FALSE","c" not in "code")
print(f"is hups hoppa? ", hups==hoppa)
l()

print("12:00")
print("datum 1/1/1984 hiervan worden drie variabelen gemaakt day month year")
print("dan kun je de dag printen met print(day)")
datum=input("geef een datum met format d m y " )
day,month,year=datum.split(" ")
print(f"de dag is ",day,"en de maand is ",month)
l()

print("12:30")
print("print(dir(string)) geeft alle methods available",dir(string))
l()

print("14:00")
print("methods")
hupper=hups.upper()
print(f"verander hups in HUPS   ",hups.upper())
print(f"hups.capitalize() verandert hups in Hups   ",hups.capitalize())
print(f"hupper=hups.upper()  print(hupper) ", hupper )
l()

print("14:30  kat door hond vervangen")
kat="ik heb een kat"
kat_r=kat.replace("kat","hond")
print(f"van kat naar hond",kat,kat_r)
l()

print("15:00  text find")
print(f"kat.find('had'))",kat.find("heb"))
l()

print("17:00  datum")
datum=input("geef een datum in formaat dd mm yyyy of d m yyyy bij voorbeeld 16 7 1931 ")
dag=datum.find(" ")
maand=datum.find(" ",dag+1)
jaar=datum[maand+1:]
print(f"het ingegeven jaar is ",jaar)
l()


naam="john"
leeftijd=30
print("ik heet {} en ben {} jaar oud")
print("gevolgd door")
print(".format(naam,leeftijd)")
print("ik heet {} and ben {} jaar oud".format(naam,leeftijd))
l()