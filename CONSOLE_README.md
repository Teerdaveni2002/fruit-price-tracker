# Console Fruit Price Tracker

A simple, standalone Python script for tracking fruit prices in the console/terminal.

## Features

- Track 5 pre-configured fruits (Apple, Banana, Orange, Mango, Grapes)
- Search fruits to increment prices by ₹2 (up to 5 searches per fruit)
- View search history with timestamps
- Add new fruits with custom prices
- Reset fruit prices and search counts
- Data persistence using JSON file storage
- No dependencies required - uses only Python standard library

## Requirements

- Python 3.6 or higher
- No external packages needed

## Usage

### Quick Start

Simply run the script:

```bash
python console_fruit_tracker.py
```

### Menu Options

1. **Search a fruit (increment price)**
   - Enter a fruit name to search
   - Price increases by ₹2 (up to 5 times)
   - Search is recorded in history

2. **View search history**
   - Shows last 10 searches with prices and timestamps

3. **Add new fruit**
   - Add a custom fruit with your chosen base price

4. **Reset a fruit**
   - Reset search count to 0
   - Restore price to base price

5. **Exit**
   - Save and quit the application

### Example Session

```
============================================================
                    FRUIT PRICE TRACKER                     
============================================================
No.   Fruit           Base Price   Current Price   Searches  
------------------------------------------------------------
1     Apple           ₹100.00      ₹100.00         0/5
2     Banana          ₹50.00       ₹50.00          0/5
3     Orange          ₹80.00       ₹80.00          0/5
4     Mango           ₹120.00      ₹120.00         0/5
5     Grapes          ₹150.00      ₹150.00         0/5
------------------------------------------------------------

OPTIONS:
1. Search a fruit (increment price)
2. View search history
3. Add new fruit
4. Reset a fruit
5. Exit

Enter your choice (1-5): 1

Enter fruit name to search: Apple

✅ Apple searched!
   New price: ₹102.00
   Search count: 1/5
   Price increased by ₹2
```

## Data Storage

- All data is saved in `fruit_data.json` in the same directory
- Data persists between sessions
- You can delete this file to reset all data

## Features Details

### Price Increment Logic
- Each search increases the fruit price by ₹2
- Maximum 5 searches per fruit
- After 5 searches, price remains constant
- Use reset option to start over

### Search History
- Records fruit name, price at search time, and timestamp
- Keeps last 10 searches
- Automatically saved to JSON file

### Adding Fruits
- Any fruit name can be added
- Set custom base price
- Duplicate names are not allowed

### Resetting Fruits
- Resets search count to 0
- Restores current price to base price
- History is preserved

## Comparison with Django Web App

This console version provides:
- ✅ Same core functionality (price tracking, search limit, history)
- ✅ No installation required (pure Python)
- ✅ Runs in any terminal/console
- ✅ Simple JSON storage

The Django web app provides:
- ✅ Modern web interface with animations
- ✅ AJAX real-time updates
- ✅ Admin panel for management
- ✅ Database persistence with SQLite
- ✅ Multi-user support

Choose the console version for quick testing and simple use cases. Choose the Django web app for a full-featured, production-ready application.

## Troubleshooting

### Permission Error
If you get a permission error on Linux/Mac:
```bash
chmod +x console_fruit_tracker.py
./console_fruit_tracker.py
```

### Python Not Found
Make sure Python 3 is installed:
```bash
python3 --version
```

Use `python3` instead of `python` if needed:
```bash
python3 console_fruit_tracker.py
```

## License

This is part of the Fruit Price Tracker project.
