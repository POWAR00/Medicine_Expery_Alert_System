# 💊 MediAlert Pro — Clinical Medicine Expiry & Inventory Management System

**MediAlert Pro** is a modern, full-stack pharmacy inventory, expiry monitoring, and alert web application built with **Python, Flask, and Jinja2**.

---

## 🌟 Key Features & Improvements

### 🎨 Modern Clinical UI & Design ("More Attractive")
- **Premium Design System**: Clean typography with Google Fonts (*Plus Jakarta Sans* & *JetBrains Mono*), frosted-glass elements, and health-tech color accents (Emerald Green, Sky Blue, Amber, Rose).
- **Interactive Visualizations (Chart.js)**:
  - **Health Breakdown Donut Chart**: Live percentage split of Good Stock vs. Expiring Soon vs. Expired vs. Low Stock.
  - **Top Stock Levels Bar Chart**: Visualizes the largest active inventory reserves.
- **Dark Mode & Light Mode**: Smooth 1-click theme switcher with persistent user preference storage.
- **Responsive Mobile Layout**: Mobile-friendly sidebar drawer and responsive table viewports for tablets and smartphones.
- **Real-Time Calendar & Digital Clock**: Live clock badge integrated into the top bar.

### ⚡ Enhanced Web Workflow & Capabilities ("Working Web")
- **Instant Client-Side Filtering**: 1-click filter tabs (`[All]`, `[⚠️ Expiring Soon]`, `[❌ Expired]`, `[📦 Low Stock]`, `[✅ Good Stock]`) without page reloads.
- **Live Search**: Instant table filtering as you type across medicine names, batch numbers, and IDs.
- **Quick Modals (No Page Navigation Required)**:
  - **💊 Quick Dispense Modal**: Dispense units right from the dashboard table with real-time bill calculations and stock-remaining preview.
  - **➕ Quick Restock Modal**: Instantly add incoming stock units and optionally update expiry dates in 1 click.
  - **🏷️ Medicine Details & Pharmacy Label Modal**: Complete product specifications, supplier contact action buttons (Phone, WhatsApp, Email), and a printable pharmacy barcode sticker label.
- **Import & Export via CSV**:
  - **Export**: 1-click download of full medicine inventory with stock valuations and status indicators.
  - **Import**: Upload CSV files with automatic deduplication, batch additions, and quantity merging.
- **1-Click Quick Demo Login**:
  - Instant access pills for **Admin**, **Pharmacist (Bhakti)**, and **Pharmacist (Arpita)** to test the web application with zero friction.
- **Failsafe 2FA / OTP Verification**:
  - Full **Paste (Ctrl+V) Support** across the 6-digit OTP input boxes.
  - In development/offline mode, displays an instant **Autofill OTP Helper** so you are never locked out by email SMTP network delays.
- **Audit & Regulatory Compliance**:
  - Full historical **Dispense & Usage Audit Trail** (`/usage`).
  - Restock modification audit logs (`/report`).
  - Print-ready and PDF-exportable **Audit Report** with signature sign-off block.

---

## 🚀 How to Run the Web Application

### Method 1: One-Click Windows Launcher (Easiest)
Simply double-click **`run.bat`** in the project folder! It will automatically start the server and open your default browser to `http://127.0.0.1:5000`.

### Method 2: Python Command Line
```bash
# In the workspace root folder:
python run_web.py
```
Or directly inside `medicine_alert_system`:
```bash
cd medicine_alert_system
python app.py
```
Open **`http://127.0.0.1:5000`** in your browser.

---

## 🔑 Demo Accounts & Credentials

| Role | Username | Password | Registered Mobile | Email |
| :--- | :--- | :--- | :--- | :--- |
| **Super Admin** | `admin` | `admin123` | `9999999999` | `admin@example.com` |
| **Pharmacist** | `Bhakti` | `Bhakti@1234` | `8446036575` | `bpowar750@gmail.com` |
| **Pharmacist** | `Arpita` | `Arpita@1234` | `7821035808` | `arpitapatil5808@gmail.com` |

*(Tip: You can also use the **1-Click Demo Login** buttons on the login page for instant login without entering passwords!)*

---

## 📁 Project Architecture

```
Python_Project/
├── run.bat                          # 1-Click Windows launcher
├── run_web.py                       # Root launcher (auto-opens browser)
├── README.md                        # Documentation
│
└── medicine_alert_system/
    ├── app.py                       # Flask application engine & schedulers
    ├── main.py                      # CLI console version
    ├── medicine_store.py            # CLI storage logic
    ├── users.csv                    # User accounts & roles
    ├── requirements.txt             # Dependencies
    ├── data/                        # Per-user isolated datasets
    │   ├── bhakti/
    │   └── arpita/
    └── templates/                   # Redesigned UI Templates
        ├── base.html                # Global layout, theme switcher, responsive sidebar
        ├── index.html               # Main dashboard with charts, quick modals, filters
        ├── login.html               # 1-click demo login & authentication
        ├── signup.html              # User registration with password strength meter
        ├── verify_otp.html          # 2FA screen with paste support & demo autofill
        ├── verify_signup_otp.html   # Email verification
        ├── alerts.html              # Categorized alerts & WhatsApp/call reorders
        ├── add.html                 # Add medicine form with live batch worth calculator
        ├── edit.html                # Edit medicine form
        ├── dispense.html            # Patient dispensing form with live bill calculator
        ├── usage.html               # Dispensing audit trail
        ├── report.html              # Printable audit report with signature block
        ├── search.html              # Live catalog search
        ├── admin.html               # Super admin control tower
        └── admin_user.html          # Admin tenant inspection
```
