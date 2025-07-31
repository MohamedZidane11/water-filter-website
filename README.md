# 🚀 Company Landing Page

A modern, responsive company landing page built with Django and styled with custom CSS. This web application showcases your business with a clean, professional design optimized for conversions and user engagement.

## ✨ Features

- 🎨 **Modern Design** - Clean, professional layout with responsive design
- 📱 **Mobile Responsive** - Optimized for all device sizes
- ⚡ **Fast Performance** - Lightweight and optimized for speed
- 🔧 **Easy Customization** - Simple to modify content and styling
- 🛡️ **Secure** - Built with Django's security best practices

## 🚀 Demo

<img src="https://github.com/MohamedZidane11/water-filter-website/blob/main/Capture12.PNG" width=850>

## 📋 Prerequisites

Before running this project, make sure you have:

- 🐍 Python 3.8 or higher
- 📦 pip (Python package manager)
- 🔧 Git

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/MohamedZidane11/water-filter-website.git
   cd water-filter-website
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start development server**
   ```bash
   python manage.py runserver
   ```

6. **Open your browser** 🌐
   Navigate to `http://127.0.0.1:8000/`

## 📁 Project Structure

```
water-filter-website/
├── 📂 static/
│   ├── 🎨 css/
│   ├── 🖼️ images/
│   └── ⚡ js/
├── 📂 templates/
│   ├── 📂 pages/
│   ├── 📂 partials/
│   └── 🏠 base.html
├── 📂 company/
│   ├── ⚙️ settings.py
│   ├── 🔗 urls.py
│   └── 📋 views.py
└── 🐍 manage.py
```

## 🎨 Customization

### Updating Content
- Edit templates in the `templates/` directory
- Modify styles in `static/css/`
- Add images to `static/images/`

### Configuration
- Update `settings.py` for Django configuration
- Modify `urls.py` for routing
- Customize views in `views.py`

## 🌐 Deployment

### Production Setup
1. Set `DEBUG = False` in settings
2. Configure allowed hosts
3. Set up static files serving
4. Use PostgreSQL for production database

### Deployment Options
- 🚀 **Heroku** - Easy deployment with git
- 🔵 **DigitalOcean** - Droplets or App Platform
- ☁️ **AWS** - EC2 or Elastic Beanstalk
- 🔮 **Vercel** - Serverless deployment

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. 🍴 Fork the repository
2. 🌿 Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push to the branch (`git push origin feature/AmazingFeature`)
5. 🔄 Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with ❤️ using Django
- Inspiration from modern web design trends

---

⭐ **Star this repo if you find it helpful!** ⭐
