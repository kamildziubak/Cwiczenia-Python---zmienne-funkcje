# Zadanie 1.
# Proszę utworzyć listę liczb od 1 do 57 , których reszta z dzielenia przez 7
# wynosi 3. Proszę wyświetlić tę listę

lista = [n for n in range(58) if n%7==3]
lista

# Zadanie 2.
# Mając do dyspozycji trzy napisy:
# miau = "Miau"
# przecinek = ", "
# hau = "Hau"
# proszę z nich wynerować napis: "MiauMiauMiau, HauHau"

miau = "Miau"
przecinek = ", "
hau = "Hau"

print(miau+miau+miau+przecinek+hau+hau)

# Zadanie 3
# Ze zdania:
# zdanie = "Studenci Vistuli są utalentowani, inteligentni i mili"
# zdanie += ", ale nie zaliczą tego kursu"
# proszę wyciąć część w oczywisty sposób nieprawdziwą i wyświetlić
# część pozostałą.
# Najpierw proszę utworzyć listę słów zawartych w zdaniu 'zdanie'.

zdanie = "Studenci Vistuli są utalentowani, inteligentni i mili"
zdanie += ", ale nie zaliczą tego kursu"
zdanie=zdanie[:-28]
slowa = zdanie.split()
slowa

# Zadanie 4
# Proszę utworzyć listę 'rośliny' zawierającą trzy krotki:
# ssaki = ('chomiki', 'jelenie', 'jaguary')
# ptaki = ('gołębie', 'jastrzębie', 'strusie')
# gady = ('węże', 'krokodyle', 'warany')
# Proszę wyświetlić nazwy wszystkich zwierząt jedną po drugiej

ssaki = ('chomiki', 'jelenie', 'jaguary')
ptaki = ('gołębie', 'jastrzębie', 'strusie')
gady = ('węże', 'krokodyle', 'warany')
rośliny = [ssaki, ptaki, gady]

for krotka in rośliny:
  for zwierzę in krotka:
    print(zwierzę)

# Zadanie 5
# Proszę napisać programik, który będzie prosił użytkownika o podanie liczby
# całkowitej N, a następnie obliczał: (a) cos(pi*N/6), jeśli N < 0,
# (b) cos(pi*N/4), jeśli N > 0, oraz cos(pi*N/3) w pozostałych przypadkach :-).

from math import cos
from math import pi

n = int(input('Podaj liczbę całkowitą: '))

if n<0:
  print(cos(pi*n/6))
elif n>0:
  print(cos(pi*n/4))
else:
  print(cos(pi*n/3))