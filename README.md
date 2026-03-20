
# Aforro Backend — Real-World Django Demo

Welcome! This project is a practical Django REST API, built to look and feel like something you’d see in a real job or interview. It’s easy to run, easy to demo, and everything is set up for you — no weird surprises.

---

## What’s Included?

- Django 4.x + Django REST Framework for APIs
- Celery for background/async order processing
- Redis for rate limiting and as a Celery broker
- PostgreSQL (Docker) for production, SQLite for dev
- Docker Compose for running everything together
- Automated tests for all the main features
- A simple HTML frontend to demo the APIs visually

---

## Quick Start (No Headaches)

1. **Clone this repo:**
   ```sh
   git clone <your-repo-url>
   cd aforro
   ```
2. **Start everything with Docker Compose:**
   ```sh
   docker-compose up --build
   ```
3. **Apply migrations and seed demo data:**
   ```sh
   docker-compose exec web python manage.py migrate
   docker-compose exec web python manage.py seed_data
   ```
4. **Run the tests (optional):**
   ```sh
   docker-compose exec web python manage.py test
   ```
5. **Open the demo UI:**
   Go to [http://localhost:8000/](http://localhost:8000/) in your browser.

---

## API & Demo UI: What’s Related?

Here’s how each section of the HTML demo maps to the backend APIs:

| Demo UI Section         | Related API Endpoint(s)                  | What It Does                                  |
|------------------------|------------------------------------------|-----------------------------------------------|
| Product Autocomplete   | GET /api/search/suggest/?q=...           | Suggests product names as you type            |
| Order Listing          | GET /api/stores/<store_id>/orders/       | Lists all orders for a store                  |
| Stores                 | GET /api/stores/                         | Shows all stores                              |
| Product List           | GET /api/products/                       | Lists all products                            |
| Product Detail         | GET /api/products/<id>/                  | Shows details for a single product            |
| Search Products        | GET /api/search/products/?q=...          | Searches products by keyword                  |
| Order Product          | POST /api/orders/                        | Places a new order                            |
| Inventory              | GET /api/stores/<store_id>/inventory/    | Shows inventory for a store                   |


---

## How to Use the Demo UI (Step-by-Step)

1. **Start the project** (see Quick Start above) and open [http://localhost:8000/](http://localhost:8000/) in your browser.
2. **Try each section:**
   - **Product Autocomplete:** Type at least 3 letters and click Autocomplete to see product suggestions.
   - **Product List:** Click Load Products to see all products. Use the Product ID for other actions.
   - **Product Detail:** Enter a Product ID and click Get Detail to see details.
   - **Search Products:** Enter a keyword and click Search to filter products.
   - **Stores:** Click Show Stores to list all stores.
   - **Order Listing:** Enter a Store ID and click Show Orders to see orders for that store.
   - **Order Product:** Enter Store ID, Product ID, and Quantity, then click Order to place an order.
   - **Inventory:** Enter a Store ID and click Show Inventory to see all products and quantities for that store.
3. **See results instantly** below each form. Errors and API responses are shown right on the page.

You can mix and match: for example, find a product in Product List, then use its ID to place an order or check inventory. The UI is built so you can demo everything visually, no code needed!

---

## How It Works (Plain English)

- **Products, Stores, Orders, Inventory:** All modeled with Django ORM, with clear relationships.
- **Async Order Confirmation:** Placing an order triggers a background Celery task (just like in real apps).
- **Redis:** Used for rate limiting (autocomplete) and as the Celery broker.
- **Docker:** Everything runs in containers for easy setup.
- **Tests:** Automated tests cover all the main APIs and business logic.

---

## Need Help?

Check the code comments, try the demo UI, or run the tests. Everything is set up to be as clear and realistic as possible. Good luck with your review or interview!

---
