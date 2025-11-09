#!/usr/bin/env python3
"""
Simple console-based Fruit Price Tracker
A standalone Python script that tracks fruit prices with search increments.
"""

import json
import os
from datetime import datetime


class FruitTracker:
    """Console-based fruit price tracker"""
    
    def __init__(self, data_file='fruit_data.json'):
        self.data_file = data_file
        self.fruits = {}
        self.search_history = []
        self.load_data()
    
    def load_data(self):
        """Load fruit data from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.fruits = data.get('fruits', {})
                    self.search_history = data.get('history', [])
            except Exception as e:
                print(f"Error loading data: {e}")
        else:
            # Initialize with default fruits
            self.fruits = {
                'Apple': {'base_price': 100.0, 'current_price': 100.0, 'search_count': 0},
                'Banana': {'base_price': 50.0, 'current_price': 50.0, 'search_count': 0},
                'Orange': {'base_price': 80.0, 'current_price': 80.0, 'search_count': 0},
                'Mango': {'base_price': 120.0, 'current_price': 120.0, 'search_count': 0},
                'Grapes': {'base_price': 150.0, 'current_price': 150.0, 'search_count': 0},
            }
            self.save_data()
    
    def save_data(self):
        """Save fruit data to JSON file"""
        try:
            data = {
                'fruits': self.fruits,
                'history': self.search_history
            }
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def display_fruits(self):
        """Display all fruits with current prices"""
        print("\n" + "="*60)
        print("FRUIT PRICE TRACKER".center(60))
        print("="*60)
        print(f"{'No.':<5} {'Fruit':<15} {'Base Price':<12} {'Current Price':<15} {'Searches':<10}")
        print("-"*60)
        
        for idx, (name, data) in enumerate(self.fruits.items(), 1):
            print(f"{idx:<5} {name:<15} ₹{data['base_price']:<11.2f} "
                  f"₹{data['current_price']:<14.2f} {data['search_count']}/5")
        print("-"*60)
    
    def search_fruit(self, fruit_name):
        """Search for a fruit and increment its price"""
        if fruit_name not in self.fruits:
            print(f"\n❌ Fruit '{fruit_name}' not found!")
            return
        
        fruit = self.fruits[fruit_name]
        
        # Record search history
        self.search_history.insert(0, {
            'fruit': fruit_name,
            'price': fruit['current_price'],
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
        # Keep only last 10 searches
        self.search_history = self.search_history[:10]
        
        # Increment price if search count < 5
        if fruit['search_count'] < 5:
            fruit['current_price'] += 2
            fruit['search_count'] += 1
            self.save_data()
            print(f"\n✅ {fruit_name} searched!")
            print(f"   New price: ₹{fruit['current_price']:.2f}")
            print(f"   Search count: {fruit['search_count']}/5")
            print(f"   Price increased by ₹2")
        else:
            self.save_data()
            print(f"\n⚠️  {fruit_name} has reached maximum searches (5/5)")
            print(f"   Price remains at: ₹{fruit['current_price']:.2f}")
            print(f"   Use option 5 to reset if needed")
    
    def view_history(self):
        """Display search history"""
        print("\n" + "="*70)
        print("RECENT SEARCH HISTORY".center(70))
        print("="*70)
        
        if not self.search_history:
            print("No search history yet.")
        else:
            print(f"{'No.':<5} {'Fruit':<15} {'Price at Search':<18} {'Timestamp':<20}")
            print("-"*70)
            for idx, entry in enumerate(self.search_history, 1):
                print(f"{idx:<5} {entry['fruit']:<15} ₹{entry['price']:<17.2f} {entry['timestamp']}")
        print("-"*70)
    
    def add_fruit(self):
        """Add a new fruit"""
        print("\n" + "="*50)
        print("ADD NEW FRUIT")
        print("="*50)
        
        name = input("Enter fruit name: ").strip()
        if not name:
            print("❌ Fruit name cannot be empty!")
            return
        
        if name in self.fruits:
            print(f"❌ Fruit '{name}' already exists!")
            return
        
        try:
            base_price = float(input("Enter base price (₹): "))
            if base_price <= 0:
                print("❌ Price must be greater than 0!")
                return
            
            self.fruits[name] = {
                'base_price': base_price,
                'current_price': base_price,
                'search_count': 0
            }
            self.save_data()
            print(f"\n✅ Fruit '{name}' added successfully at ₹{base_price:.2f}")
        except ValueError:
            print("❌ Invalid price! Please enter a number.")
    
    def reset_fruit(self):
        """Reset a fruit's price and search count"""
        self.display_fruits()
        fruit_name = input("\nEnter fruit name to reset: ").strip()
        
        if fruit_name not in self.fruits:
            print(f"❌ Fruit '{fruit_name}' not found!")
            return
        
        fruit = self.fruits[fruit_name]
        fruit['current_price'] = fruit['base_price']
        fruit['search_count'] = 0
        self.save_data()
        
        print(f"\n✅ {fruit_name} has been reset!")
        print(f"   Price: ₹{fruit['current_price']:.2f}")
        print(f"   Search count: 0/5")
    
    def run(self):
        """Main program loop"""
        while True:
            self.display_fruits()
            print("\nOPTIONS:")
            print("1. Search a fruit (increment price)")
            print("2. View search history")
            print("3. Add new fruit")
            print("4. Reset a fruit")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                fruit_name = input("\nEnter fruit name to search: ").strip()
                self.search_fruit(fruit_name)
                input("\nPress Enter to continue...")
            
            elif choice == '2':
                self.view_history()
                input("\nPress Enter to continue...")
            
            elif choice == '3':
                self.add_fruit()
                input("\nPress Enter to continue...")
            
            elif choice == '4':
                self.reset_fruit()
                input("\nPress Enter to continue...")
            
            elif choice == '5':
                print("\n" + "="*50)
                print("Thank you for using Fruit Price Tracker!")
                print("="*50)
                break
            
            else:
                print("\n❌ Invalid choice! Please enter 1-5.")
                input("Press Enter to continue...")


def main():
    """Entry point for the console application"""
    tracker = FruitTracker()
    tracker.run()


if __name__ == '__main__':
    main()
