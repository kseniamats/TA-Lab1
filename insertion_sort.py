def insertion_sort(arr):
    n = len(arr)
    comparisons = 0
    assignments = 0

    for i in range(1, n):
        key = arr[i]
        assignments += 1
        j = i - 1
        assignments += 1

        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            assignments += 1
            j -= 1
            assignments += 1

        if j >= 0:
            comparisons += 1

        arr[j + 1] = key
        assignments += 1

    return arr, comparisons, assignments

# Тест для варіанту 14
my_list = [10, 90, 95, 30, 45, 60, 57, 28, 5]
print("Insertion Sort для варіанту 14:")
print("Початковий масив:", my_list)
sorted_list, comps, assigns = insertion_sort(my_list.copy())
print("Відсортований масив:", sorted_list)
print(f"Порівнянь: {comps}, Присвоєнь: {assigns}")