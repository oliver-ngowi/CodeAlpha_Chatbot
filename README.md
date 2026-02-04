# POSTA Restaurant Chatbot

A simple conversational chatbot for a restaurant ordering system built with Python and Tkinter.

## Overview

POSTA Restaurant Chatbot is a user-friendly chatbot designed to help customers browse the menu, check prices, place orders, and calculate totals. It features both a command-line interface and a graphical user interface (GUI).

## Features

- **Menu Information**: View available food and drink items
- **Price Lookup**: Check prices for specific menu items
- **Order Management**: Add items to cart and track your order
- **Total Calculation**: Automatic total cost calculation for orders
- **Two Interfaces**: 
  - Command-line interface (text-based)
  - GUI interface with Tkinter (graphical)

## Menu Items

### Food
- Ugali & Chicken - 12,000 TZS
- Rice & Beef - 8,000 TZS
- Chips & Chicken - 15,000 TZS
- Pilau - 10,000 TZS

### Drinks
- Soda - 2,000 TZS
- Water - 1,000 TZS
- Juice - 3,000 TZS
- Tea - 1,500 TZS
- Coffee - 2,000 TZS

## How It Works

### Core Components

**Chatbot.py** - Backend logic:
- `PRICES`: Dictionary storing all menu items and their prices
- `get_price_response()`: Handles price inquiries
- `check_order()`: Processes and tracks customer orders
- `calculate_total()`: Computes order totals
- `display_orders()`: Shows current orders
- `posta_chatbot()`: Main command-line chatbot loop

**chatbot_gui.py** - GUI implementation:
- `ChatbotGUI`: Tkinter-based graphical interface
- Clean, restaurant-themed design with butter yellow color scheme
- Real-time message display and order tracking

### How to Use

#### GUI Version (Recommended)
```bash
python chatbot_gui.py
```
- Type your message in the input field
- Press Enter or click "Send Message" to chat
- View order history and total in the dedicated order panel
- Click "Clear Order" to reset your cart

#### Command-Line Version
```bash
python Chatbot.py
```
- Type messages like:
  - "menu" - See all items
  - "drinks" - See drink options
  - "how much is rice and beef?" - Check a price
  - "I want ugali and chicken" - Add item to order
  - "show my order" - View current order
  - "bye" - Exit the chatbot

## Technical Stack

- **Language**: Python 3.x
- **GUI Framework**: Tkinter (standard Python library)
- **Architecture**: Object-oriented design with modular functions

## Example Interaction

```
You: hello
Bot: Hello! How can I help you today?

You: what's the price of rice and beef?
Bot: Rice & Beef costs 8,000 TZS.

You: I want to order rice and beef
Bot: Great! Added Rice & Beef to your order. Your order total so far: 8,000 TZS.

You: and a soda please
Bot: Great! Added Soda to your order. Your order total so far: 10,000 TZS.
```

## Notes

- Currency used: TZS (Tanzanian Shilling)
- The chatbot recognizes variations like "ugali and chicken" and "ugali & chicken"
- Orders are tracked during the session but not persisted after closing
