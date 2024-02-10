import random

def welcome_message():
    return "Welcome to the Electrical Gadgets Shopping Assistant! How can I help you today?"

def ai_response(user_input):
    responses = ["I'm sorry, I didn't understand that.", "Please provide more details.", "How about checking our latest arrivals?"]
    return random.choice(responses)

def recommend_gadget(category):
    gadgets = {"smartphone": "Latest smartphone model", "laptop": "Powerful laptop for your needs", "smartwatch": "Fitness tracking smartwatch"}
    return gadgets.get(category, "Sorry, we don't have recommendations for that category.")

def show_categories():
    return "We offer a variety of electrical gadgets. Some popular categories include smartphones, laptops, and smartwatches."

def get_product_details(product_name):
    details = {"Latest smartphone model": "Features: XYZ, Price: $999", "Powerful laptop for your needs": "Specifications: ABC, Price: $1499", "Fitness tracking smartwatch": "Features: DEF, Price: $199"}
    return details.get(product_name, "Sorry, details not available for this product.")

def add_to_cart(product_name, cart):
    cart.append(product_name)
    return f"Added {product_name} to your shopping cart."

def view_cart(cart):
    if not cart:
        return "Your shopping cart is empty."
    else:
        cart_contents = ", ".join(cart)
        return f"Your shopping cart contains: {cart_contents}"

def checkout(cart):
    total_price = 0  # Replace this with actual logic to calculate the total price
    return f"Thank you for shopping with us! Your total is ${total_price}. Your order will be processed soon."

def main():
    print(welcome_message())

    shopping_cart = []

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye! Have a great day.")
            break
        
        ai_output = ai_response(user_input)
        print(f"AI: {ai_output}")

        if "recommend" in user_input.lower():
            words = user_input.lower().split()
            category_index = words.index("recommend") + 1
            category = words[category_index] if category_index < len(words) else ""
            recommendation = recommend_gadget(category)
            print(f"AI: {recommendation}")

        elif "categories" in user_input.lower():
            print(f"AI: {show_categories()}")

        elif "details" in user_input.lower():
            words = user_input.lower().split()
            product_index = words.index("details") + 1
            product_name = " ".join(words[product_index:]) if product_index < len(words) else ""
            product_details = get_product_details(product_name)
            print(f"AI: {product_details}")

        elif "add to cart" in user_input.lower():
            words = user_input.lower().split()
            product_index = words.index("cart") + 1
            product_name = " ".join(words[product_index:]) if product_index < len(words) else ""
            cart_message = add_to_cart(product_name, shopping_cart)
            print(f"AI: {cart_message}")

        elif "view cart" in user_input.lower():
            print(f"AI: {view_cart(shopping_cart)}")

        elif "checkout" in user_input.lower():
            checkout_message = checkout(shopping_cart)
            print(f"AI: {checkout_message}")

# Run the main function if the script is executed
if _name_ == "_main_":
    main()
