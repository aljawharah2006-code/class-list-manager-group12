
# Class List Manager - Group 12
# MIS 211 Bonus Assignment (GitHub Teamwork)

names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]

# ===== Each student adds her function BELOW this line =====

# Written by: Your aljawharah almotawa (Task 1)
def count_names(names):
    return len(names)


# Written by: Layan alshahrani (Task 6)
def to_upper(names):
    upper_names = []
    for name in names:
        upper_names.append(name.upper())
    return upper_names


# Written by: sarah alshbibi (Task 3)
def sort_names(names):
    return sorted(names)
    
# ===== Each student adds her function ABOVE this line =====



def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Number of names:", count_names(names))
    print("Sorted names:", sort_names(names))
    # Each student calls her function here
    print("Uppercase names:", to_upper(names))

main()

