# Example:
# values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]
# string_factory(values)
# ["Hi, I'm Michelangelo and I love to eat PIZZA!", "Hi, I'm Garfield and I love to eat lasagna!"]

template = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(val):
    new = []
    for v in val:
        new.append(template.format(**v))
        # new.append(template + ".format(**v)")
    return new
values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]
print(string_factory(values))
