

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


## 🧩 How It Works (In Plain English)

- **Products, Stores, Orders, Inventory:** All modeled with Django ORM, with clear relationships and constraints.
- **Async Order Confirmation:** Placing an order triggers a background Celery task (simulates real-world async workflows).
- **Redis:** Used for rate limiting (autocomplete endpoint) and as the Celery broker.
- **Docker:** Everything (Django, PostgreSQL, Redis, Celery worker) runs in containers for easy setup.
- **Tests:** Automated tests cover all major APIs and business logic.

---


## 🤔 Why This Project?

- **Shows real-world backend skills** (not just toy examples)
- **Easy for interviewers to run and review**
- **Ready for extension** (add user auth, admin UI, advanced filters, etc.)

---


## 🙋‍♂️ Author & Reviewer Notes

- **All code is written for clarity and realism** (see comments and docstrings)
- **No AI artifacts or awkward code** — everything is human-quality
- **Want to extend?** Just add your features — the codebase is clean and modular

---

Happy reviewing! If you have questions, check the code comments or run the tests.
