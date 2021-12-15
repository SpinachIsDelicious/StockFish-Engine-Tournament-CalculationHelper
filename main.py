from os import system, name
from time import sleep
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
try:
    from colorama import Fore
except Exception as err:
    if isinstance(err,ModuleNotFoundError):
        quit("YOU HAVE NOT RAN \"pip install colorama\" which is a vital part of the program. Please install colorama and run the file again.")
# exchanges: 
print(Fore.CYAN + "Exchanges values below! TOTAL EQUAL TO 1000" + Fore.RESET)
global pawn
global knight
global bishop
global rook
global queen
pawn = int(input("Exchange value for pawn: "))
knight = int(input("Exchange value for knight: "))
bishop = int(input("Exchange value for bishop: "))
rook = int(input("Exchange value for rook: "))
queen = int(input("Exchange value for queen: "))
clear()
print(Fore.LIGHTMAGENTA_EX + "Values intercepted!" + Fore.RESET)
# above total: 1000
# hunt:
print(Fore.CYAN + "Hunt values below! TOTAL EQUAL TO 1000" + Fore.RESET)
global King
global Knight
global Queen
global Bishop
global Rook
King= int(input("Hunt value for king: "))
Knight= int(input("Hunt vaue for knight: "))
Queen = int(input("Hunt value for queen: "))
Bishop= int(input("Hunt value for bishop: "))
Rook= int(input("Hunt value for rook: "))
clear()
print(Fore.LIGHTMAGENTA_EX + "Values intercepted!" + Fore.RESET)
#above total: 1000
# thingy:
print(Fore.CYAN + "Attack area values below! TOTAL EQUAL TO 30, NEGATIVE IS DOUBLED" + Fore.RESET)
global attack_center
global attack_base
attack_center = int(input("Attack center value: "))
attack_base = int(input("Attack base value: "))
clear()
print(Fore.LIGHTMAGENTA_EX + "Values intercepted!" + Fore.RESET)
#above total: 30, negative is doubled
# pawn thingy:
print(Fore.CYAN + "Pawn movement values below! TOTAL EQUAL TO 100, NEGATIVE IS DOUBLED" + Fore.RESET)
global pawn_forward
global pawn_chain
pawn_forward = int(input("Pawn forward value: "))
pawn_chain = int(input("Pawn chain value: "))
clear()
print(Fore.LIGHTMAGENTA_EX + "Values intercepted!" + Fore.RESET)
#above total: 100
if pawn_forward < 0:
  pawn_forward = abs(pawn_forward) * 2
if pawn_chain < 0:
  pawn_chain = abs(pawn_chain) *2
if pawn_forward+pawn_chain == 100:
    print(Fore.BLUE + "Valid Pawn Movement" + Fore.RESET)
else:
    print(Fore.RED +f"Invalid Pawn Movement, Pawn Movement is equal to {pawn_forward+pawn_chain}" + Fore.RESET)
if King + Knight + Queen + Bishop + Rook == 1000:
    print(Fore.BLUE + "Valid Hunt" + Fore.RESET)
else:
    print(Fore.RED + f"Invalid Hunt, Hunt is equal to {King + Knight + Queen + Bishop + Rook}" + Fore.RESET)
Total = abs(pawn) + abs(knight) + abs(bishop) + abs(rook) + abs(queen)
if Total == 1000:
    print(Fore.GREEN + "Valid Exchange" + Fore.RESET)
else:
    print(Fore.RED + f"Invalid Exchange, Exchange is equal to {Total}" + Fore.RESET)
if attack_center < 0:
  attack_center = abs(attack_center) * 2
if attack_base < 0:
  attack_base = abs(attack_base) *2
if attack_center + attack_base == 30:
  print(Fore.GREEN + "Valid center and base attack" + Fore.RESET)
else:
  print(Fore.RED + f"Invalid center and base attack, Center and Base Attack is equal to {attack_center+attack_base}")
