import numpy as np

# Створення масиву 3x3
array = np.random.randint(1, 101, size=(3, 3))
print("Початковий масив 3x3:")
print(array)

# Сума всіх елементів
total_sum = array.sum()
print(f"\nСума всіх елементів: {total_sum}")

# Максимум, мінімум та їхні індекси
max_value = array.max()
min_value = array.min()

max_index = np.unravel_index(np.argmax(array), array.shape)
min_index = np.unravel_index(np.argmin(array), array.shape)

print(f"\nМаксимальне значення: {max_value}  →  індекс: {max_index}")
print(f"Мінімальне значення:  {min_value}  →  індекс: {min_index}")

# Сортування по кожному рядку
sorted_array = np.sort(array, axis=1)

print("\nМасив після сортування кожного рядка:")
print(sorted_array)