from selection_sort import selection_sort
from insertion_sort import insertion_sort

# Твоя послідовність
my_list = [10, 90, 95, 30, 45, 60, 57, 28, 5]

print("=== ЛАБОРАТОРНА РОБОТА 1 ===")
print("Варіант 14:", my_list)
print()

# Selection Sort
sorted_sel, comps_sel, assigns_sel = selection_sort(my_list.copy())
print(f"Selection Sort: {sorted_sel}")
print(f"Порівнянь: {comps_sel}, Присвоєнь: {assigns_sel}")
print()

# Insertion Sort
sorted_ins, comps_ins, assigns_ins = insertion_sort(my_list.copy())
print(f"Insertion Sort: {sorted_ins}")
print(f"Порівнянь: {comps_ins}, Присвоєнь: {assigns_ins}")
print()

print("=== ПОРІВНЯННЯ ===")
print(f"Selection Sort: {comps_sel} порівнянь, {assigns_sel} присвоєнь")
print(f"Insertion Sort: {comps_ins} порівнянь, {assigns_ins} присвоєнь")