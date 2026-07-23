# 💼 Job Application Tracker

A web application built with **Django** that helps job seekers organize, track, and manage their job applications efficiently.

---

## ✨ Features

* **Home Dashboard:** View real-time statistics of total applications, including status breakdowns (Applied, Interview, Offer, Accepted, Rejected).
* **Application Management:** Add, edit, view, and delete job application records with details like company name, position, status, application date, and deadlines.
* **Customized Django Admin Panel:**
  * **Table View:** Displays `Company Name`, `Position`, `Status`, `Application Date`, and `Deadline` for quick insights.
  * **Filtering:** Easily filter records by `Status` and `Application Date`.
  * **Search Bar:** Quickly search applications by `Company Name` or `Position`.

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3, Bootstrap
* **Database:** SQLite
* **Version Control:** Git & GitHub

---

## 🚀 Getting Started Locally

Follow these step-by-step instructions to set up and run the project locally on your machine:

### 1. Clone the Repository
```bash
git clone https://github.com/FahmidaMitu/job_tracker.git
cd job_tracker
```

### 2. Set Up Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py migrate
```

### 5. Create a Superuser (for Admin Access)
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

---

## 🔗 Project URLs

Once the server is running, access the application through these links:
* **Main Dashboard:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## 🎥 UI Demonstration Video
[Click here to watch the project video/screenshots](YOUR_DRIVE_LINK_HERE)