class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} - Quantity: {self.quantity}, Price: ${self.price}" 

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, name, quantity, price):
        if name in self.products:
            self.products[name].quantity += quantity
        else:
            self.products[name] = Product(name, quantity, price)
        print(f"Product '{name}' added to inventory.")

    def show_inventory(self):
        if not self.products:
            print("The inventory is empty.")
        else:
            for product in self.products.values():
                print(product)

    def update_quantity(self, name, quantity):
        if name in self.products:
            self.products[name].quantity = quantity
            print(f"Quantity of '{name}' updated to {quantity}.")
        else:
            print(f"Product '{name}' not found in the inventory.")

    def delete_product(self, name):
        if name in self.products:
            del self.products[name]
            print(f"Product '{name}' removed from inventory.")
        else:
            print(f"Product '{name}' not found in the inventory.")

def menu():
    inventory = Inventory()

    while True:
        print("\n--- Inventory Menu ---")
        print("1. Add Product")
        print("2. Show Inventory")
        print("3. Update Product Quantity")
        print("4. Delete Product")
        print("5. Exit")

        option = input("Select an option (1-5): ")

        if option == "1":
            name = input("Product name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price per unit: "))
            inventory.add_product(name, quantity, price)
        elif option == "2":
            inventory.show_inventory()
        elif option == "3":
            name = input("Product name: ")
            quantity = int(input("New quantity: "))
            inventory.update_quantity(name, quantity)
        elif option == "4":
            name = input("Product name to delete: ")
            inventory.delete_product(name)
        elif option == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    menu()