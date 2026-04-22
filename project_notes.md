# Freshmart Project Notes

## **1. Project Overview**
**Freshmart** is a premium Grocery Inventory Management System built to handle both weighted products (e.g., Vegetables in kg) and unit-based products (e.g., Snacks in pcs). It features a modern, responsive storefront and a comprehensive administrative dashboard.

---

## **2. Technology Stack**
- **Frontend**: 
  - **HTML5 & Vanilla CSS**: Custom styling for a premium feel.
  - **Bootstrap 5**: Responsive grid and UI components.
  - **JavaScript (ES6)**: Dynamic filtering and real-time order tracking.
- **Backend**: 
  - **Flask (Python)**: Robust routing and business logic.
- **Database**: 
  - **MySQL**: Relational data storage for products, orders, and categories.

---

## **3. APIs & Libraries Used**
### **Twilio API (SMS)**
- **Purpose**: Used for high-priority notifications.
- **Implementation**: 
  - Sends manual SMS alerts to the admin when stock levels fall below the threshold.
  - Integration: `twilio.rest.Client`.
- **Config**: Located at the top of `app.py` (`TWILIO_ACCOUNT_SID`, etc.).

### **Scikit-Learn (Machine Learning)**
- **Purpose**: Powering the Growth/Trend analysis.
- **Implementation**: Uses `LinearRegression` to analyze order frequency and predict future trends based on historical dates.

### **Pandas & NumPy**
- **Purpose**: Data manipulation for reports.
- **Implementation**: Converting database results into DataFrames for analysis and trend calculations.

---

## **4. Core Code Explanation**

### **A. Database Connection (`get_db_connection`)**
We use `mysql-connector-python` to interact with the database. The connection is opened and closed for each request to ensure stability.
```python
def get_db_connection():
    return mysql.connector.connect(
        host="localhost", user="root", password="root", database="homedb"
    )
```

### **B. Category Filtering (Home Page)**
Implemented as a client-side JavaScript function for instant feedback. It uses `data-category` attributes on product cards:
```javascript
function filterByCategory(category, element) {
  const cards = document.querySelectorAll(".product-col");
  cards.forEach((card) => {
    const cardCategory = card.getAttribute("data-category").toLowerCase();
    // Fuzzy matching logic here...
    card.style.display = isMatch ? "" : "none";
  });
}
```

### **C. Real-time Order Tracking**
Orders on the user side use a `setInterval(fetchUpdates, 10000)` polling mechanism. This checks the `/api/order_updates` endpoint every 10 seconds and updates the UI (timeline/badges) without a page reload if the status changes on the admin side.

### **D. Decimal Quantity Support**
The system uses `FLOAT` for product quantities and the `step="0.1"` attribute in HTML inputs to allow fractional purchases (e.g., 1.5 kg).

---

## **5. Key Features Summary**
- **Order Trace Management**: 'Ordered' -> 'Packed' -> 'Shipped' -> 'Delivered'.
- **Reporting**: Dedicated views for Low Stock, Out of Stock, and general inventory health.
- **Admin Suite**: Fully featured CRUD (Create, Read, Update, Delete) for Products and Categories.
