class GroceryListManager:
    def __init__(self):
        self.grocery_list = []

    def display_menu(self):
        print("\nGrocery List Manager")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View List")
        print("4. Sort List")
        print("5. Reverse List")
        print("6. Exit")

    def add_item(self):
        item = input("Enter item to add: ")
        self.grocery_list.append(item)
        print(f"{item} added to the list.")

    def remove_item(self):
        item = input("Enter item to remove: ")
        if item in self.grocery_list:
            self.grocery_list.remove(item)
            print(f"{item} removed from the list.")
        else:
            print(f"{item} not found in the list.")

    def view_list(self):
        print("Grocery List:")
        for item in self.grocery_list:
            print(f"- {item}")

    def sort_list(self):
        self.grocery_list.sort()
        print("List sorted alphabetically.")

    def reverse_list(self):
        self.grocery_list.reverse()
        print("List order reversed.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.remove_item()
            elif choice == "3":
                self.view_list()
            elif choice == "4":
                self.sort_list()
            elif choice == "5":
                self.reverse_list()
            elif choice == "6":
                print("Exiting the Grocery List Manager.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = GroceryListManager()
    manager.run()
