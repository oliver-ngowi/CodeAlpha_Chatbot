# Price database for foods and drinks
PRICES = {
    # Food items
    "ugali and chicken": 12000,
    "ugali & chicken": 12000,
    "rice and beef": 8000,
    "rice & beef": 8000,
    "chips and chicken": 15000,
    "chips & chicken": 15000,
    "pilau": 10000,
    
    # Drinks
    "soda": 2000,
    "water": 1000,
    "juice": 3000,
    "tea": 1500,
    "coffee": 2000,
}

def get_price_response(user_input):
    """Check if user is asking about prices and return appropriate response."""
    # Check for price-related keywords
    price_keywords = ["price", "cost", "how much", "expensive", "pay", "charge"]
    
    if not any(keyword in user_input for keyword in price_keywords):
        return None
    
    # Check each food/drink item
    for item, price in PRICES.items():
        if item in user_input:
            return f"POSTA RESTAURANT BOT: {item.title()} costs {price:,} TZS."
    
    # Generic price response if asking about prices but no specific item
    if any(keyword in user_input for keyword in price_keywords):
        return "POSTA RESTAURANT BOT: Which item would you like to know the price for? Ask about: Ugali & Chicken, Rice & Beef, Chips & Chicken, Pilau, Soda, Water, Juice, Tea, or Coffee."
    
    return None

def check_order(user_input, orders):
    """Check if user is ordering an item and add it to their order."""
    order_keywords = ["order", "want", "like", "give me", "i'll take", "i want", "i like", "get me", "add"]
    
    # Check if input contains order keywords
    if not any(keyword in user_input for keyword in order_keywords):
        return None
    
    # Check each food/drink item
    for item in PRICES.keys():
        if item in user_input:
            orders.append(item)
            return f"POSTA RESTAURANT BOT: Great! Added {item.title()} to your order. Your order total so far: {calculate_total(orders):,} TZS."
    
    # If user mentions ordering but doesn't specify item
    if any(keyword in user_input for keyword in order_keywords):
        return "POSTA RESTAURANT BOT: What would you like to order? Choose from: Ugali & Chicken, Rice & Beef, Chips & Chicken, Pilau, Soda, Water, Juice, Tea, or Coffee."
    
    return None

def calculate_total(orders):
    """Calculate the total cost of orders."""
    total = 0
    for item in orders:
        total += PRICES.get(item, 0)
    return total

def display_orders(orders):
    """Display the current orders."""
    if not orders:
        return "POSTA RESTAURANT BOT: You haven't ordered anything yet."
    
    order_summary = "POSTA RESTAURANT BOT: Your current order:\n"
    for i, item in enumerate(orders, 1):
        order_summary += f"  {i}. {item.title()} - {PRICES[item]:,} TZS\n"
    order_summary += f"Total: {calculate_total(orders):,} TZS"
    return order_summary

def posta_chatbot():
    print("POSTA RESTAURANT BOT: Welcome! Type 'bye' to exit.")
    print("POSTA RESTAURANT BOT: You can ask about menu, drinks, prices, offers, and delivery costs.\n")
    
    orders = []  # Track customer orders

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("POSTA RESTAURANT BOT: Hello! How can I help you today?")

        elif user_input == "what do you have today":
            print("POSTA RESTAURANT BOT: We have local meals, fast foods, and drinks.")

        elif user_input == "menu":
            print("POSTA RESTAURANT BOT: Our menu includes:")
            print("  • Ugali & Chicken - 12,000 TZS")
            print("  • Rice & Beef - 8,000 TZS")
            print("  • Chips & Chicken - 15,000 TZS")
            print("  • Pilau - 10,000 TZS")

        elif user_input == "drinks":
            print("POSTA RESTAURANT BOT: Our drinks:")
            print("  • Soda - 2,000 TZS")
            print("  • Water - 1,000 TZS")
            print("  • Juice - 3,000 TZS")
            print("  • Tea - 1,500 TZS")
            print("  • Coffee - 2,000 TZS")

        elif user_input == "offers available":
            print("POSTA RESTAURANT BOT: Free soda for orders above 20,000 TZS.")

        elif user_input == "delivery cost":
            print("POSTA RESTAURANT BOT: Delivery costs 3,000 TZS.")
        
        elif user_input == "my order" or user_input == "show order" or user_input == "view order":
            print(display_orders(orders))
        
        elif user_input == "clear order" or user_input == "cancel order":
            orders.clear()
            print("POSTA RESTAURANT BOT: Your order has been cleared.")

        elif user_input == "bye":
            if orders:
                print(display_orders(orders))
                print("POSTA RESTAURANT BOT: Thank you for your order! We'll prepare it for you.")
            else:
                print("POSTA RESTAURANT BOT: Thank you for visiting POSTA RESTAURANT!")
            break

        else:
            # Check if it's an order
            order_response = check_order(user_input, orders)
            if order_response:
                print(order_response)
            else:
                # Check if it's a price query
                price_response = get_price_response(user_input)
                if price_response:
                    print(price_response)
                else:
                    print("POSTA RESTAURANT BOT: Sorry, I didn't understand that. You can: order items, ask about menu, drinks, prices, or say 'my order' to see your order!")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("POSTA RESTAURANT CHATBOT - SELECT MODE")
    print("="*50)
    print("1. Terminal Mode (Text-based)")
    print("2. GUI Mode (Graphical Interface)")
    print("="*50)
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "2":
        try:
            from chatbot_gui import run_gui
            run_gui()
        except ImportError:
            print("GUI module not found. Running in Terminal mode instead...")
            posta_chatbot()
    else:
        posta_chatbot()
