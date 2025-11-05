# ⚙️ Dynamic Pricing Rules Engine

A lightweight, flexible Django-based engine to **define and apply complex commercial pricing rules** (discounts, thresholds, bulk rules, etc.) entirely from the database — **no code changes required to add new rules**.

---

## 🎯 Goals
- Store pricing rules (`PricingRule`) in the DB (rule type, condition, discount).  
- Provide an API that accepts a cart (list of `{product_id, quantity}`) and returns the final price after applying all active rules.  
- Make rules pluggable: new rules = new DB row, no code change.

---

## ✨ Features
- `Product`, `Cart`, and `CartItem` models.  
- `PricingRule` model to define flexible discount logic.  
- `CartService` to apply rules dynamically and compute totals.  
- DRF endpoint to submit cart items and get calculated prices.  
- **Fixtures included** to load sample data:  
  - `product.json` (sample products)  
  - `pricing-rule.json` (sample rules for testing)

---

## 🧰 Tech Stack
- Python 3.12  
- Django (latest)  
- Django REST Framework  
- PostgreSQL  
- Docker & docker-compose  

---
