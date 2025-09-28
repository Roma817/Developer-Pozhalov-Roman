def get_numbers():
    while True:
        user_input = input("Введіть 10 дійсних чисел через кому (роздільник — крапка):\n")
        parts = user_input.strip().split(',')
        if len(parts) != 10:
            print("Помилка: потрібно ввести рівно 10 чисел, розділених комами.")
            continue
        try:
            numbers = [float(x.replace(' ', '')) for x in parts]
        except ValueError:
            print("Помилка: всі значення мають бути дійсними числами з крапкою як роздільником.")
            continue
        if not all(10 <= num <= 1000 for num in numbers):
            print("Помилка: кожне число має бути в межах від 10 до 1000.")
            continue
        return numbers

if __name__ == "__main__":
    numbers = get_numbers()
    min_num = min(numbers)
    max_num = max(numbers)
    avg_num = round(sum(numbers) / len(numbers), 2)

    print("\n=== Результати ===")
    print(f"Мінімум: {min_num}") 
    print(f"Максимум: {max_num}") 
    print(f"Середнє: {avg_num}")
    print(f"Розробник: Пожалов Роман")