# Напишите программу, в которой создадите и заполните список,
# а затем посчитаете количество уникальных элементов в нём и выведите на экран.

def filling_in_the_list():
    print("Заполните список элементами.\n"
          "Для завершения заполнения введите три нуля (000).")
    list_elements = []
    while True:
        input_element = input("Введите элемент:\n")
        list_elements.append(input_element)
        if input_element == "000":
            list_elements.remove("000")
            break
    return list_elements


def print_unique_elements(completed_list):
    unique_elements = set(completed_list)
    print(f"\nКоличество уникальных элементов в списке: {len(unique_elements)}\n"
          f"\nУникальные элементы:")
    for element in unique_elements:
        print(element)


print_unique_elements(filling_in_the_list())
