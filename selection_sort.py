def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    for i in range(n - 1):
        min_index = i  # ← ВИПРАВЛЕНО
        assignments += 1

        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
                assignments += 1

        comparisons += 1
        if min_index != i:  # ← ВИПРАВЛЕНО
            arr[i], arr[min_index] = arr[min_index], arr[i]
            assignments += 3

    return arr, comparisons, assignments

# Тест для варіанту 14
my_list = [10, 90, 95, 30, 45, 60, 57, 28, 5]
print("Selection Sort для варіанту 14:")
print("Початковий масив:", my_list)
sorted_list, comps, assigns = selection_sort(my_list.copy())  # ← ВИПРАВЛЕНО
print("Відсортований масив:", sorted_list)
print(f"Порівнянь: {comps}, Присвоєнь: {assigns}")  # ← ВИПРАВЛЕНО
print()