# Name: Zachary Phillips
# Date: October 6, 2026
# Purpose: Create an online shopping cart program


def format_money(amount):
    """Show whole-dollar amounts without decimals (e.g. $189),
    otherwise show two decimals (e.g. $1.50)."""
    if amount == int(amount):
        return f'${int(amount)}'
    return f'${amount:.2f}'


class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0,
                 item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        item_cost = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ '
              f'{format_money(self.item_price)} = {format_money(item_cost)}')


class ShoppingCart:
    def __init__(self, customer_name="none",
                 current_date="January 1, 2025"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return

        print('Item not found in cart. Nothing removed.')

    def modify_item(self, item):
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                cart_item.item_quantity = item.item_quantity
                return

        print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):
        total_items = 0

        for item in self.cart_items:
            total_items += item.item_quantity

        return total_items

    def get_num_items(self):
        return self.get_num_items_in_cart()

    def get_cost_of_cart(self):
        total_cost = 0

        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity

        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")

        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
            return 0

        for item in self.cart_items:
            item.print_item_cost()

        print(f'Number of Items: {self.get_num_items_in_cart()}')
        print()

        total_cost = self.get_cost_of_cart()
        print(f'Total: {format_money(total_cost)}')

        return total_cost


def print_menu():
    print('MENU')
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity')
    print('o - Output shopping cart')
    print('q - Quit')


def execute_menu(menu_op, the_cart):
    if menu_op == 'a':
        print('ADD ITEM TO CART')

        item_name = input('Enter the item name: ')
        item_price = float(input('Enter the item price: '))
        item_quantity = int(input('Enter the item quantity: '))

        the_cart.add_item(
            ItemToPurchase(item_name, item_price, item_quantity)
        )

    elif menu_op == 'r':
        print('REMOVE ITEM FROM CART')

        item_name = input('Enter name of item to remove:\n')
        the_cart.remove_item(item_name)

    elif menu_op == 'c':
        print('CHANGE ITEM QUANTITY')

        item_name = input('Enter the item name:\n')
        new_quantity = int(input('Enter the new quantity:\n'))

        modified_item = ItemToPurchase(item_name, 0, new_quantity)
        the_cart.modify_item(modified_item)

    elif menu_op == 'o':
        print('OUTPUT SHOPPING CART')
        the_cart.print_total()


if __name__ == "__main__":
    cust_name = input("Enter customer's name: ")
    day_date = input("Enter today's date: ")

    print()
    print(f'Customer name: {cust_name}')
    print(f"Today's date: {day_date}")
    print()

    shopping_cart = ShoppingCart(cust_name, day_date)

    print_menu()
    print()

    menu_choice = ' '

    while menu_choice != 'q':
        menu_choice = input('Choose an option:\n')

        while menu_choice not in ['a', 'r', 'c', 'o', 'q']:
            menu_choice = input('Choose an option:\n')

        if menu_choice != 'q':
            execute_menu(menu_choice, shopping_cart)
            print()
            print_menu()
            print()
