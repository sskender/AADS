names = ["Ana", "Petar", "Ana", "Lucija", "Vanja", "Pavao", "Lucija"]

def reverse_sort(names: list) -> list:
    return sorted(names)[::-1]

names_desc = reverse_sort(names)
print(names_desc)

selected_names = reverse_sort(names)[:-1]
print(selected_names)

unique_selected_names = set(selected_names)
print(unique_selected_names)

pass_names = []
for name in unique_selected_names:
    new_name = name + " - pass"
    pass_names.append(new_name)
print(pass_names)
