import sys


Inventory = dict[str, int]


def parse_parameter(parameter: str, inventory: Inventory) -> None:
    if ":" not in parameter:
        print(f"Error - invalid parameter '{parameter}'")
        return
    item_name, quantity_text = parameter.split(":", 1)
    if item_name == "" or quantity_text == "":
        print(f"Error - invalid parameter '{parameter}'")
        return
    if item_name in inventory:
        print(f"Redundant item '{item_name}' - discarding")
        return
    try:
        inventory[item_name] = int(quantity_text)
    except ValueError as error:
        print(f"Quantity error for '{item_name}': {error}")


def get_inventory() -> Inventory:
    inventory: Inventory = {}
    for parameter in sys.argv[1:]:
        parse_parameter(parameter, inventory)
    return inventory


def display_percentages(inventory: Inventory, total: int) -> None:
    for item_name in inventory:
        percentage = round(inventory[item_name] * 100 / total, 1)
        print(f"Item {item_name} represents {percentage}%")


def display_abundant_items(inventory: Inventory) -> None:
    most_item = ""
    least_item = ""
    first_item = True
    for item_name in inventory:
        if first_item:
            most_item = item_name
            least_item = item_name
            first_item = False
        if inventory[item_name] > inventory[most_item]:
            most_item = item_name
        if inventory[item_name] < inventory[least_item]:
            least_item = item_name
    most_quantity = inventory[most_item]
    least_quantity = inventory[least_item]
    print(f"Item most abundant: {most_item} with quantity {most_quantity}")
    print(f"Item least abundant: {least_item} with quantity {least_quantity}")


def display_inventory(inventory: Inventory) -> None:
    item_list = list(inventory.keys())
    total = sum(inventory.values())
    print(f"Got inventory: {inventory}")
    print(f"Item list: {item_list}")
    print(f"Total quantity of the {len(item_list)} items: {total}")
    if len(item_list) == 0 or total == 0:
        print("No positive quantity to analyze")
        return
    display_percentages(inventory, total)
    display_abundant_items(inventory)


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = get_inventory()
    display_inventory(inventory)
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
