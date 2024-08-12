
waiting_list: list[str] = ['sen', 'ben', 'john']

waiting_list.sort() # Sorting the items alphabetically


for index, item in enumerate(waiting_list):
    row = f"{index + 1}. {item.capitalize()}"
    print(row)
