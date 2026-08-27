products = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Mobile", "price": 20000},
    3: {"name": "Headphones", "price": 2000}
}

cart = {}

while True:
    print("\n--- SHOPPING CART ---")
    print("1. Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        for id, product in products.items():
            print(id, product["name"], "₹", product["price"])

    elif choice == 2:
        product_id = int(input("Enter product ID: "))

        if product_id in products:
            if product_id in cart:
                cart[product_id] += 1
            else:
                cart[product_id] = 1

            print("Product added to cart!")
        else:
            print("Product not found!")

    elif choice == 3:
        total = 0

        print("\n--- YOUR CART ---")

        for product_id, quantity in cart.items():
            product = products[product_id]
            price = product["price"] * quantity

            print(
                product["name"],
                "x", quantity,
                "=", price
            )

            total += price

        print("----------------")
        print("Total = ₹", total)

    elif choice == 4:
        print("Thank you!")
        break

    else :
        print("Invalid choice!")
