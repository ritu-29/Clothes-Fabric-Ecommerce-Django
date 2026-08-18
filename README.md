# 🧶 Knit Fabric – Clothes-Fabric-Ecommerce-Django

Knit Fabric is a Django-based online fabric e-commerce platform designed for buying and selling knit fabrics and clothing materials.

The website provides separate functionality for **Customers and Sellers**, allowing users to browse products, manage profiles, add products to cart, place orders, make online/offline payments, submit feedback and complaints, while sellers can manage their products and view customer orders.

---

## 📌 Project Overview

**Knit Fabric** is a full-stack e-commerce web application developed using **Python and Django**.

The main purpose of this project is to provide an online marketplace where:

- Customers can browse and purchase fabric products.
- Sellers can register and create their shop profiles.
- Sellers can add and manage products.
- Customers can add products to cart and place orders.
- Online payments are handled using Razorpay.
- Customers can make offline payment requests as well.
- Customers can track their order history.
- Customers can submit feedback and complaints.
- Users can recover forgotten passwords through email.
- Admin can manage users, sellers, products, orders, feedback and complaints.

---

# 🚀 Features

## 👤 Customer Features

### Registration & Authentication
- User registration
- User login/logout
- Email-based password recovery
- Session-based authentication
- User role management

### User Profile
- Create user profile
- Add profile image
- Add address
- Add date of birth
- Add profession
- Add personal bio
- Edit profile information

### Product Browsing
- View all fabric products
- View product details
- Browse products by category
- Search/filter products by category
- View product price and availability
- View product quantity

### Shopping Cart
- Add products to cart
- Increase product quantity
- Decrease product quantity
- Remove products from cart
- Automatic stock quantity management
- Automatic total price calculation
- Prevent purchase when stock is insufficient

### Orders
- Place orders
- View order history
- View individual order details
- Track payment status
- View purchased products

### Payments
- Online payment using Razorpay
- Offline payment option
- Payment status management
- Razorpay payment verification
- Payment confirmation email

### Feedback & Complaints
- Submit product/order feedback
- Give ratings
- Submit complaints related to orders
- Prevent duplicate feedback for the same order

---

# 🏪 Seller Features

## Seller Registration

Sellers can register on the platform by providing:

- Name
- Email
- Password
- Phone number
- ID proof

Seller accounts require approval before they can access seller functionality.

---

## Seller Profile

Sellers can create and manage:

- Shop name
- Shop address
- Seller address
- Profile image
- Years of experience
- Specialization
- Rating
- Availability status

---

## Product Management

Sellers can:

- Add new products
- Select product category
- Add product name
- Add product description
- Set product price
- Set available quantity
- Upload product image
- Edit product information
- Delete products
- View their products

---

## Seller Order Management

Sellers can view orders containing their products.

This allows sellers to monitor customer purchases and manage their product orders.

---

# 👨‍💼 Admin Features

The Django Admin Panel provides management functionality for:

- Users
- Sellers
- User profiles
- Seller profiles
- Product categories
- Products
- Shopping cart items
- Orders
- Feedback
- Complaints
- Contact messages

The admin can also approve seller accounts before they become active.

---

# 💳 Payment System

Knit Fabric supports two payment methods:

### 1. Online Payment

Online payments are integrated using **Razorpay**.

The application:

1. Creates a Razorpay order.
2. Sends payment information to the Razorpay checkout.
3. Receives payment response.
4. Verifies the Razorpay payment signature.
5. Updates the order status.
6. Associates cart items with the completed order.
7. Sends a confirmation email to the customer.

### 2. Offline Payment

Customers can also select offline payment and provide:

- Delivery address
- Payment reference
- Additional remarks

The order is then created with a `Pending` payment status.

---

# 📧 Email Functionality

The application uses Django's email functionality with Gmail SMTP.

Email is used for:

- Forgot password functionality
- New password delivery
- Payment confirmation

SMTP configuration should be stored securely using environment variables instead of directly writing credentials in `settings.py`.

---

# 🛠️ Tech Stack

## Backend

- Python
- Django 5.1.4
- Django ORM
- SQLite

## Frontend

- HTML5
- CSS3
- JavaScript
- Django Templates

## Payment

- Razorpay

## Database

- SQLite

## Email

- Gmail SMTP
- Django Email Backend

## Media

- Pillow
- Django Media Files

---

# 🗂️ Project Structure

```text
Knit-Fabric/
│
├── manage.py
├── requirements.txt
├── README.md
├── db.sqlite3
│
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── myapp/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── templates/
│   ├── 404.html
│   ├── base.html
│   ├── Home1.html
│   ├── Home2.html
│   ├── Home3.html
│   ├── Home4.html
│   ├── Home5.html
│   ├── Home6.html
│   ├── Home7.html
│   ├── Home8.html
│   ├── login_page.html
│   ├── signup.html
│   ├── addproduct.html
│   ├── addsellerprofile.html
│   ├── adduser.html
│   ├── cart_page.html
│   ├── order_history.html
│   ├── vieworder.html
│   ├── sellershowproduct.html
│   ├── sellershoworder.html
│   ├── feedback.html
│   ├── complaint.html
│   ├── success.html
│   └── ...
│
├── static/
│   └── ...
│
└── media/
    └── ...
```

---

# 🗄️ Database Models

The project uses Django ORM for database management.

### Main Models

| Model             | Purpose                                       |
| ----------------- | --------------------------------------------- |
| `Login`           | Stores user/seller login and role information |
| `UserProfile`     | Stores customer profile information           |
| `SellerProfile`   | Stores seller/shop information                |
| `ProductCategory` | Stores fabric product categories              |
| `Product`         | Stores product information                    |
| `productCart`     | Manages shopping cart items                   |
| `Order`           | Stores order and payment information          |
| `Feedback`        | Stores customer ratings and feedback          |
| `Complaint`       | Stores customer complaints                    |
| `Contact_detail`  | Stores contact form submissions               |

---

# 🔗 Application Flow

```text
                 ┌─────────────────┐
                 │   Knit Fabric   │
                 │    Website      │
                 └────────┬────────┘
                          │
              ┌───────────┴───────────┐
              │                       │
          Customer                  Seller
              │                       │
      ┌───────┼────────┐        ┌─────┼──────────┐
      │       │        │        │     │          │
   Signup   Login   Browse    Signup Profile   Products
      │       │    Products      │     │          │
      │       │       │          │     │       Add/Edit
      │       │       ▼          │     │       Products
      │       │     Cart         │     │          │
      │       │       │          │     │          ▼
      │       │       ▼          │     │     View Orders
      │       │    Checkout      │     │
      │       │       │          │     │
      │       │   ┌───┴────┐     │     │
      │       │   │        │     │     │
      │       │ Online   Offline │     │
      │       │ Payment  Payment │     │
      │       │   │        │     │     │
      │       │   └───┬────┘     │     │
      │       │       │          │     │
      │       └───────┼──────────┘     │
      │               │                │
      ▼               ▼                ▼
 Feedback        Order History    Seller Orders
 Complaints      & Tracking
```

---

# 🔐 User Roles

The application supports two main roles:

## Customer

```text
Role = User
```

Customers can:

* Browse products
* Manage profile
* Add products to cart
* Place orders
* Make payments
* View order history
* Submit feedback
* Submit complaints

## Seller

```text
Role = Seller
```

Sellers can:

* Create seller profile
* Add products
* Edit products
* Delete products
* View their products
* View customer orders

Seller registration also includes an approval workflow.

---

# 🛒 Shopping Cart Stock Management

The application implements stock management through the `productCart` model.

When a product is added to the cart:

```text
Available Stock
       ↓
Cart Quantity
       ↓
Stock Reduced
```

When a cart item is deleted:

```text
Cart Item Removed
       ↓
Product Quantity
       ↓
Stock Restored
```

The system also checks whether sufficient stock is available before adding products.

---

# 📊 Order & Payment Status

## Payment Status

```text
Pending
Paid
Failed
```

## Payment Modes

```text
Online
Offline
```

## Product Availability

```text
Available
Not Available
```

## Seller Availability

```text
Available
Not Available
```

---

# 🔑 URL Routes

Some important application routes include:

| URL                 | Function            |
| ------------------- | ------------------- |
| `/`                 | Home page           |
| `/about`            | About page          |
| `/contact`          | Contact page        |
| `/login`            | User login          |
| `/signup`           | User registration   |
| `/logout`           | Logout              |
| `/forgotpassword`   | Password recovery   |
| `/products`         | Product listing     |
| `/shopdetail/<id>`  | Product details     |
| `/add_to_cart`      | Add product to cart |
| `/ecommerce-cart`   | Shopping cart       |
| `/payment`          | Order history       |
| `/vieworder/<id>`   | Order details       |
| `/product_form`     | Add product         |
| `/sellerproduct`    | Seller products     |
| `/showorder`        | Seller orders       |
| `/complaint_submit` | Submit complaint    |
| `/storefeedback`    | Submit feedback     |
| `/admin/`           | Django admin        |

---

# ⚙️ Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Move into the project:

```bash
cd Knit-Fabric
```

---

## 2. Create Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 5. Create Admin Account

```bash
python manage.py createsuperuser
```

Enter:

```text
Username
Email
Password
```

---

## 6. Run Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

Admin panel:

```text
http://127.0.0.1:8000/admin/
```

---

# 🔒 Environment Variables

Sensitive credentials should NOT be committed to GitHub.

Create a `.env` file:

```env
SECRET_KEY=your_django_secret_key

RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_SECRET_KEY=your_razorpay_secret_key

EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_app_password
```

Add `.env` to `.gitignore`:

```gitignore
.env
```
# 🧪 Testing the Application

Recommended testing flow:

### Customer Flow

```text
1. Register as User
2. Login
3. Complete User Profile
4. Browse Products
5. Select Product
6. Add Product to Cart
7. Change Quantity
8. Checkout
9. Select Payment Method
10. Complete Order
11. Check Order History
12. View Order Details
13. Submit Feedback
```

### Seller Flow

```text
1. Register as Seller
2. Upload ID Proof
3. Wait for Admin Approval
4. Login after Approval
5. Complete Seller Profile
6. Add Product
7. Edit Product
8. View Products
9. View Customer Orders
```

---

# 🧑‍💻 Admin Workflow

The administrator can manage the complete platform through Django Admin.

```text
Admin
 │
 ├── Users
 ├── Seller Profiles
 ├── Approve Sellers
 ├── Product Categories
 ├── Products
 ├── Orders
 ├── Cart Items
 ├── Feedback
 ├── Complaints
 └── Contact Messages
```

---

# 📱 Responsive & Template Design

The project contains multiple Django templates for:

* Home pages
* Product pages
* Shop pages
* Blog pages
* Login/signup
* User profile
* Seller profile
* Cart
* Orders
* Feedback
* Complaints
* Contact
* FAQ
* Success/error pages

The templates are organized to provide a complete e-commerce website experience.

---

# 🔮 Future Improvements

The following features can be added in future versions:

* Product search by name
* Advanced product filtering
* Wishlist functionality
* Product reviews on individual products
* Product pagination
* Seller dashboard with analytics
* Sales reports
* Revenue analytics
* Order status tracking
* Delivery tracking
* Product image gallery
* Coupon and discount system
* GST/invoice generation
* Improved authentication using Django's built-in authentication system
* Secure password hashing
* REST API integration
* PostgreSQL/MySQL database
* Deployment using cloud hosting
* Docker support
* Automated testing
* Better mobile responsiveness

---
# 👩‍💻 Developer

**Ritu Poonjani**

### Skills Used

```text
Python
Django
HTML
CSS
JavaScript
SQLite
Django ORM
Razorpay API
SMTP / Email
Git
GitHub
```
---
# ⭐ Project Purpose

This project was developed as a practical **Python Django e-commerce project** to demonstrate backend development, database management, authentication, shopping cart functionality, payment integration, seller management and real-world business workflows.
