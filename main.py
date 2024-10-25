# Напишите программу, в которой создадите и заполните список,
# а затем посчитаете количество уникальных элементов в нём и выведите на экран.

def filling_in_the_list():
    print("Заполните список элементами.\n"
          "Для завершения заполнения введите три нуля (000).")
    list_elements = []
    while True:
        input_element = input("Введите элемент:\n")
        if input_element == "000":
            break
        list_elements.append(input_element)
    return list_elements


def print_unique_elements(completed_list):
    unique_elements = set(completed_list)
    print(f"\nКоличество уникальных элементов в списке: {len(unique_elements)}")


print_unique_elements(filling_in_the_list())
