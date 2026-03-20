# Aforro Backend — Interview-Ready Demo

**Aforro** is a realistic Django REST API project designed to showcase practical backend engineering skills for interviews and real-world work. It’s easy to run, well-documented, and demonstrates:

- Clean API design
- Async processing (Celery)
- Real-world use of Redis
- Dockerized development
- Automated testing

**Perfect for:** interviews, demos, and as a base for more complex projects.

---

## 📝 Reviewer Quick Summary

- **Everything runs in Docker** (no local setup headaches)
- **Seed data** and a demo HTML UI included
- **All code is idiomatic, clear, and realistic**
- **Automated tests** for all major features
- **API table below for fast review**

---

---

## 🚀 What’s Inside?

- **Django 4.x** with Django REST Framework
- **Celery** for async order processing
- **Redis** for rate limiting and as a Celery broker
- **PostgreSQL** (via Docker) for production, SQLite for dev
- **Docker Compose** for full-stack orchestration
- **Automated tests** for all major features
- **HTML frontend** for easy API demoing

---

## 🛠️ Quick Start

1. **Clone this repo** and open the project folder:
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
5. **Open the demo frontend:**
   Visit [http://localhost:8000/](http://localhost:8000/) in your browser for a simple HTML UI to try all APIs.

---


## 📚 API Overview (Cheat Sheet)

| Method | Endpoint                          | Description                        |
|--------|------------------------------------|------------------------------------|
| POST   | /api/orders/                      | Place a new order                  |
| GET    | /api/stores/<store_id>/orders/    | List orders for a store            |
| GET    | /api/stores/<store_id>/inventory/ | See inventory for a store          |
| GET    | /api/search/products/             | Search products (filters, sort)    |
| GET    | /api/search/suggest/?q=xxx        | Autocomplete product names         |

**Tip:** Try all APIs in the demo HTML UI at [http://localhost:8000/](http://localhost:8000/)

---



## 🖥️ How to Use the Demo HTML UI

Open [http://localhost:8000/](http://localhost:8000/) in your browser after starting the project. The demo page lets you try all APIs visually:

- **Product Autocomplete**: Enter at least 3 letters in the box and click "Autocomplete". See product name suggestions (calls `/api/search/suggest/?q=...`).
- **Order Listing**: Enter a Store ID and click "Show Orders" to see all orders for that store (`/api/stores/<store_id>/orders/`).
- **Stores**: Click "Show Stores" to list all stores (`/api/stores/`).
- **Product List**: Click "Load Products" to see all products (`/api/products/`).
- **Product Detail**: Enter a Product ID and click "Get Detail" to see info for that product (`/api/products/<id>/`).
- **Search Products**: Enter a keyword and click "Search" to search products (`/api/search/products/?q=...`).
- **Order Product**: Enter Store ID, Product ID, and Quantity, then click "Order" to place an order (`POST /api/orders/`).
- **Inventory**: Enter a Store ID and click "Show Inventory" to see all products and quantities for that store (`/api/stores/<store_id>/inventory/`).

Each section shows results or errors directly below the form. You can use these to demo all major features without writing any code!

- **Products, Stores, Orders, Inventory:** All modeled with Django ORM, with clear relationships and constraints.
- **Async Order Confirmation:** Placing an order triggers a background Celery task (simulates real-world async workflows).
- **Redis:** Used for rate limiting (autocomplete endpoint) and as the Celery broker.
- **Docker:** Everything (Django, PostgreSQL, Redis, Celery worker) runs in containers for easy setup.
- **Tests:** Automated tests cover all major APIs and business logic.

---
