# Fruit Price Tracker

A modern Django web application for tracking fruit prices with real-time updates and search history.

## Features

- **5 Pre-configured Fruits**: Apple, Banana, Orange, Mango, and Grapes with base prices
- **Dynamic Price Updates**: Prices increment by ₹2 per search (up to 5 searches)
- **Search History**: Persistent tracking of all price searches
- **Modern UI**: Responsive Bootstrap 5 interface with CSS animations
- **Real-time Updates**: AJAX-powered search functionality
- **Admin Panel**: Django admin interface for data management

## Technologies Used

- Django 5.x
- Bootstrap 5
- JavaScript (ES6+)
- SQLite database
- CSS3 with animations

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fruit-price-tracker
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Initialize fruits data**
   ```bash
   python manage.py init_fruits
   ```

6. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create your admin account.

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Usage

### Tracking Fruit Prices

1. Open the application in your browser
2. Click on any fruit card or the "Search" button
3. The price will increment by ₹2 (up to 5 searches)
4. Search history is automatically updated
5. View recent searches in the history table below

### Admin Panel

Access the admin panel to:
- View and manage fruits
- View search history
- Add new fruits
- Reset search counts

## Project Structure

```
fruit-price-tracker/
├── fruit_tracker/          # Main project settings
│   ├── __init__.py
│   ├── settings.py        # Project configuration
│   ├── urls.py            # URL routing
│   ├── asgi.py
│   └── wsgi.py
├── tracker/               # Main application
│   ├── management/
│   │   └── commands/
│   │       └── init_fruits.py  # Command to initialize fruits
│   ├── migrations/        # Database migrations
│   ├── templates/
│   │   └── tracker/
│   │       └── index.html # Main template
│   ├── __init__.py
│   ├── admin.py          # Admin configuration
│   ├── apps.py
│   ├── models.py         # Fruit and SearchHistory models
│   ├── urls.py           # App URL routing
│   └── views.py          # View logic
├── static/               # Static files
│   ├── css/
│   │   └── styles.css    # Custom CSS with animations
│   └── js/
│       └── app.js        # AJAX functionality
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Models

### Fruit
- `name`: Unique fruit name
- `base_price`: Original price
- `current_price`: Current price (increments with searches)
- `search_count`: Number of searches (max 5)
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

### SearchHistory
- `fruit`: Foreign key to Fruit
- `price_at_search`: Price when search was performed
- `search_timestamp`: When the search occurred

## API Endpoints

- `GET /`: Main page displaying all fruits
- `POST /search/<fruit_id>/`: Search endpoint (AJAX)
  - Returns JSON with updated price and search count

## Features in Detail

### Price Increment Logic
- Each search increments the fruit's price by ₹2
- Maximum 5 searches per fruit
- After 5 searches, price remains constant
- Search history is recorded with the price at time of search

### UI/UX Features
- Responsive design (mobile-friendly)
- Smooth CSS animations
- Real-time price updates without page reload
- Visual feedback for user actions
- Auto-dismissing success/error messages
- Gradient backgrounds and modern styling

## Development

### Running Tests
```bash
python manage.py test
```

### Making Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files (for production)
```bash
python manage.py collectstatic
```

## Production Deployment

Before deploying to production:

1. Set `DEBUG = False` in `settings.py`
2. Configure `ALLOWED_HOSTS` with your domain
3. Use a production database (PostgreSQL recommended)
4. Set up a secure `SECRET_KEY` (use environment variables)
5. Configure static files serving
6. Use a production WSGI server (Gunicorn, uWSGI)
7. Set up HTTPS

## Troubleshooting

### Static files not loading
- Run `python manage.py collectstatic`
- Check `STATIC_URL` and `STATICFILES_DIRS` in settings.py

### Database errors
- Delete `db.sqlite3` and run migrations again
- Run `python manage.py migrate`

### Port already in use
- Use a different port: `python manage.py runserver 8080`

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues and questions, please open an issue on the GitHub repository.
