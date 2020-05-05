from EBD.models import (
        EBDUser, 
        EBDClass, 
        ClassRegister, 
        EBD
    )

print("[LOG] Criando turmas...", end="")

class_data = [
    ["crianças", True],
    ["jovens", True],
    ["adultos", True]
]

print("Ok!")

for data in class_data:
    ebd, created = EBDClass.objects.get_or_create(
        name=data[0],
        is_active=data[1]
    )

print("[LOG] Criando usuários...", end="")

user_data = [
    ["a1", "Áquilas A.", "crianças", False],
    ["a2", "Abel A.", "crianças", False],
    ["a3", "Abigail A.", "crianças", False],
    ["a4", "Abiude A.", "crianças", False],
    ["a5", "Abraão A.", "crianças", True],
    ["b1", "Barnabé B.", "jovens", False],
    ["b2", "Beaulah B.", "jovens", False],
    ["b3", "Benjamim B.", "jovens", False],
    ["b4", "Betsabé B.", "jovens", False],
    ["b5", "Betânia B.", "jovens", True],
    ["c1", "Cam C.", "adultos", False],
    ["c2", "Carmela C.", "adultos", False],
    ["c3", "Carmelo C.", "adultos", False],
    ["c4", "Cefas C.", "adultos", False],
    ["c5", "Caleb C.", "adultos", True],
]

for data in user_data:
    
    user, created = EBDUser.objects.get_or_create(
        nickname=data[0],
        name=data[1],
        ebd_class=EBDClass.objects.get(name=data[2]),
        teacher=data[3]
    )

print("Ok!")