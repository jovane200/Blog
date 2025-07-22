# ✨ Django Personal Blog - Dark Themed + Tags + Comments + Search + Admin Redesign

A fully functional Django 5 blog application with:

- ✅ Custom admin design (dark mode + animated, modern feel)
- ✅ Posts with image, tag support, and publishing options
- ✅ Comments (moderated)
- ✅ Full-text search bar
- ✅ Tag filtering and tag listing
- ✅ Pagination
- ✅ Responsive layout
- ✅ Deployed on Render.com
- ✅ Cloudinary for image hosting

---

## 🧱 Tech Stack

- Django 5.2
- SQLite (or any other supported DB)
- HTML5 + CSS3 (Dark Mode)
- Custom CSS + Animations
- Cloudinary (media storage)
- Django Taggit (for tags)
- Whitenoise (static file handling for production)
- Render.com (Free Hosting)

---

## 📸 Features Overview

### Public Side
- Beautiful landing page listing blog posts
- Tags system with filtering
- Search bar with result page
- Individual blog post detail with:
  - Image
  - Tags
  - Comment form
  - Share buttons (X, LinkedIn, WhatsApp, Facebook)

### Admin Side
- Completely custom dark-mode admin interface
- Smooth hover and transition effects
- Posts, Comments, and Tags management
- Preview all posts easily
- Paginated and filterable admin list view

---

## 🚀 Getting Started

```bash
# Clone this repository
git clone https://github.com/your-username/django-blog.git
cd django-blog

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput

# Run the server
python manage.py runserver
```

---

## 📁 File Structure

```
Blog/
│
├── Blog/                  # Main Django project folder
│   └── settings.py
│   └── urls.py
│   └── wsgi.py
│
├── myblog/                # Blog app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   ├── admin.py
    ├── templates/
│   	  └── myblog/
│         	   ├── post/
│             	      ├── list.html
│                     ├── detail.html
│                     ├── search_results.html
│               ├── tag_list.html
│     └── base.html
│
├── static/                # Static files
│   └── css/
│       ├── blog.css        # Main frontend styling
│       └── custom_admin.css # Custom admin panel design
│
├── templates/
│   └── admin/
│       ├── base_site.html
│
├── requirements.txt
├── render.yaml
├── Procfile
├── build.sh
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 🌐 Demo (if hosted)
> https://blog-t8gj.onrender.com/

---


---

## 📦 Deployment (Render.com)

- `render.yaml` included
- `build.sh` and `Procfile` ready
- Just connect repo to Render, set environment variables:
  - `SECRET_KEY`
  - `CLOUDINARY_CLOUD_NAME`
  - `CLOUDINARY_API_KEY`
  - `CLOUDINARY_API_SECRET`

---

## 📜 License

This project can be used for personal use.
Attribution appreciated but not required.

---

## 💡 Author

**Jovane Padonou**  
Contact: jovanepadonou@gmail.com