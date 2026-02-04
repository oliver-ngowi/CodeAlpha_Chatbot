import tkinter as tk
from tkinter import scrolledtext
from Chatbot import check_order, get_price_response, display_orders, calculate_total, PRICES

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("POSTA RESTAURANT CHATBOT")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Color scheme - Butter yellow with elegant complementary colors
        self.butter_yellow = "#F5E6D3"
        self.dark_brown = "#3E2723"
        self.cream_white = "#FFFEF9"
        self.accent_gold = "#D4A574"
        self.accent_maroon = "#5D4037"
        
        # Configure root background
        self.root.configure(bg=self.butter_yellow)
        
        # Orders list
        self.orders = []
        
        # Create UI elements
        self.create_widgets()
    
    def create_widgets(self):
        """Create all GUI widgets."""
        
        # Header Frame
        header_frame = tk.Frame(self.root, bg=self.accent_maroon)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        
        title_label = tk.Label(
            header_frame,
            text="🍽️ POSTA RESTAURANT CHATBOT 🍽️",
            font=("Arial", 18, "bold"),
            fg=self.butter_yellow,
            bg=self.accent_maroon,
            pady=15
        )
        title_label.pack()
        
        # Main content frame
        content_frame = tk.Frame(self.root, bg=self.butter_yellow)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Chat display area (read-only)
        chat_label = tk.Label(
            content_frame,
            text="Chat History:",
            font=("Arial", 11, "bold"),
            fg=self.dark_brown,
            bg=self.butter_yellow
        )
        chat_label.pack(anchor="w", pady=(0, 5))
        
        self.chat_display = scrolledtext.ScrolledText(
            content_frame,
            height=15,
            width=70,
            font=("Arial", 10),
            bg=self.cream_white,
            fg=self.dark_brown,
            state="disabled",
            relief=tk.RIDGE,
            borderwidth=2
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Input area frame
        input_frame = tk.Frame(content_frame, bg=self.butter_yellow)
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        input_label = tk.Label(
            input_frame,
            text="Your Message:",
            font=("Arial", 10, "bold"),
            fg=self.dark_brown,
            bg=self.butter_yellow
        )
        input_label.pack(anchor="w", pady=(0, 5))
        
        self.user_input = tk.Entry(
            input_frame,
            font=("Arial", 11),
            bg=self.cream_white,
            fg=self.dark_brown,
            relief=tk.RIDGE,
            borderwidth=2
        )
        self.user_input.pack(fill=tk.X, ipady=8)
        self.user_input.bind("<Return>", lambda event: self.send_message())
        
        # Buttons frame
        button_frame = tk.Frame(content_frame, bg=self.butter_yellow)
        button_frame.pack(fill=tk.X, pady=(10, 0))
        
        send_button = tk.Button(
            button_frame,
            text="Send Message",
            command=self.send_message,
            font=("Arial", 10, "bold"),
            bg=self.accent_gold,
            fg=self.dark_brown,
            relief=tk.RAISED,
            borderwidth=2,
            padx=15,
            pady=8,
            cursor="hand2"
        )
        send_button.pack(side=tk.LEFT, padx=5)
        
        view_order_button = tk.Button(
            button_frame,
            text="View My Order",
            command=self.view_order,
            font=("Arial", 10, "bold"),
            bg=self.accent_gold,
            fg=self.dark_brown,
            relief=tk.RAISED,
            borderwidth=2,
            padx=15,
            pady=8,
            cursor="hand2"
        )
        view_order_button.pack(side=tk.LEFT, padx=5)
        
        clear_button = tk.Button(
            button_frame,
            text="Clear Order",
            command=self.clear_order,
            font=("Arial", 10, "bold"),
            bg=self.accent_maroon,
            fg=self.butter_yellow,
            relief=tk.RAISED,
            borderwidth=2,
            padx=15,
            pady=8,
            cursor="hand2"
        )
        clear_button.pack(side=tk.LEFT, padx=5)
        
        exit_button = tk.Button(
            button_frame,
            text="Exit",
            command=self.root.quit,
            font=("Arial", 10, "bold"),
            bg="#E74C3C",
            fg="white",
            relief=tk.RAISED,
            borderwidth=2,
            padx=15,
            pady=8,
            cursor="hand2"
        )
        exit_button.pack(side=tk.RIGHT, padx=5)
        
        # Welcome message
        self.display_message("Bot", "Welcome! Type 'bye' to exit. You can ask about menu, drinks, prices, offers, and delivery costs.")
        self.display_message("Bot", "What can I help you with today?")
        
        # Focus on input field
        self.user_input.focus()
    
    def display_message(self, sender, message):
        """Display a message in the chat area."""
        self.chat_display.configure(state="normal")
        
        if sender == "You":
            self.chat_display.insert(tk.END, f"\n{sender}: ", "user_tag")
            self.chat_display.tag_configure("user_tag", foreground=self.accent_maroon, font=("Arial", 10, "bold"))
        else:
            self.chat_display.insert(tk.END, f"\n{sender}: ", "bot_tag")
            self.chat_display.tag_configure("bot_tag", foreground=self.accent_gold, font=("Arial", 10, "bold"))
        
        self.chat_display.insert(tk.END, message)
        self.chat_display.configure(state="disabled")
        self.chat_display.see(tk.END)
    
    def send_message(self):
        """Process user message."""
        user_message = self.user_input.get().strip()
        
        if not user_message:
            return
        
        # Display user message
        self.display_message("You", user_message)
        self.user_input.delete(0, tk.END)
        
        user_input_lower = user_message.lower()
        
        # Process different commands
        if user_input_lower == "bye":
            if self.orders:
                order_display = display_orders(self.orders)
                self.display_message("Bot", order_display)
                self.display_message("Bot", "Thank you for your order! We'll prepare it for you.")
            else:
                self.display_message("Bot", "Thank you for visiting POSTA RESTAURANT!")
        
        elif user_input_lower == "hello":
            self.display_message("Bot", "Hello! How can I help you today?")
        
        elif user_input_lower == "what do you have today":
            self.display_message("Bot", "We have local meals, fast foods, and drinks.")
        
        elif user_input_lower == "menu":
            menu_text = "Our menu includes:\n• Ugali & Chicken - 12,000 TZS\n• Rice & Beef - 8,000 TZS\n• Chips & Chicken - 15,000 TZS\n• Pilau - 10,000 TZS"
            self.display_message("Bot", menu_text)
        
        elif user_input_lower == "drinks":
            drinks_text = "Our drinks:\n• Soda - 2,000 TZS\n• Water - 1,000 TZS\n• Juice - 3,000 TZS\n• Tea - 1,500 TZS\n• Coffee - 2,000 TZS"
            self.display_message("Bot", drinks_text)
        
        elif user_input_lower == "offers available":
            self.display_message("Bot", "Free soda for orders above 20,000 TZS.")
        
        elif user_input_lower == "delivery cost":
            self.display_message("Bot", "Delivery costs 3,000 TZS.")
        
        else:
            # Check if it's an order
            order_response = check_order(user_input_lower, self.orders)
            if order_response:
                self.display_message("Bot", order_response)
            else:
                # Check if it's a price query
                price_response = get_price_response(user_input_lower)
                if price_response:
                    self.display_message("Bot", price_response)
                else:
                    self.display_message("Bot", "Sorry, I didn't understand that. You can: order items, ask about menu, drinks, prices, or say 'my order' to see your order!")
    
    def view_order(self):
        """Display current order."""
        if self.orders:
            order_display = display_orders(self.orders)
            self.display_message("Bot", order_display)
        else:
            self.display_message("Bot", "You haven't ordered anything yet.")
    
    def clear_order(self):
        """Clear current order."""
        self.orders.clear()
        self.display_message("Bot", "Your order has been cleared.")


def run_gui():
    """Run the GUI version of the chatbot."""
    root = tk.Tk()
    gui = ChatbotGUI(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
