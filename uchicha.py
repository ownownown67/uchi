import datetime

# Ввод задач пользователем
tasks = []
print("Для завершения ввода, введите 'exit'")
while True:
    task = input("Введите задачу: ")
    if task == 'exit':
        break
    else:
        tasks.append(task)

# Запись задач в файл с именем текущей даты
current_date = datetime.datetime.now().strftime("%Y-%m-%d")
file_name = current_date + "_TODO_list.txt"
with open(file_name, 'w') as file:
    for task in tasks:
        file.write(task + "\n")

print("Файл", file_name, "успешно создан.")