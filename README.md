<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>سیستم فروش و انبار | Django</title>

    <!-- Bootstrap RTL -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.rtl.min.css" rel="stylesheet">

    <!-- Persian Font -->
    <link href="https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css" rel="stylesheet">

    <style>
        body {
            background-color: #f8f9fa;
            font-family: Vazirmatn, sans-serif;
        }
        .container {
            max-width: 900px;
        }
        h1, h2 {
            font-weight: 700;
        }
        .badge {
            font-size: 0.85rem;
        }
        .box {
            background: #fff;
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 25px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.06);
        }
        ul li {
            margin-bottom: 8px;
        }
        code {
            background: #eef1f4;
            padding: 4px 8px;
            border-radius: 6px;
        }
    </style>
</head>
<body>

<div class="container py-5">

    <!-- Title -->
    <div class="text-center mb-5">
        <h1>🛒 سیستم فروش و انبار</h1>
        <p class="text-muted">
            پیاده‌سازی شده با Django و Bootstrap (RTL)
        </p>
        <span class="badge bg-success">Django</span>
        <span class="badge bg-primary">Bootstrap RTL</span>
        <span class="badge bg-dark">SQLite</span>
    </div>

    <!-- Features -->
    <div class="box">
        <h2>✨ امکانات</h2>
        <ul>
            <li>ثبت فاکتور فروش و کاهش موجودی</li>
            <li>ثبت حواله خرید و افزایش موجودی کالا</li>
            <li>مدیریت موجودی انبار</li>
            <li>ثبت پرداخت و تسویه حساب مشتریان</li>
            <li>گزارش بدهکاران، بستانکاران و فاکتورهای باز</li>
            <li>افزودن مشتری بدون نیاز به پنل ادمین</li>
            <li>رابط کاربری فارسی و راست‌چین</li>
        </ul>
    </div>

    <!-- Technologies -->
    <div class="box">
        <h2>🛠 تکنولوژی‌ها</h2>
        <ul>
            <li>Django</li>
            <li>Python</li>
            <li>Bootstrap 5 (RTL)</li>
            <li>SQLite</li>
            <li>Vazirmatn Font</li>
        </ul>
    </div>

    <!-- Run -->
    <div class="box">
        <h2>▶️ اجرای پروژه</h2>
        <pre><code>
git clone https://github.com/USERNAME/REPOSITORY.git
cd shop
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
        </code></pre>
        <p class="mt-2">
            سپس پروژه در آدرس زیر در دسترس است:
            <br>
            <code>http://127.0.0.1:8000/</code>
        </p>
    </div>

    <!-- Structure -->
    <div class="box">
        <h2>📁 ساختار کلی</h2>
        <pre><code>
core/        مدل‌ها، فرم‌ها و ویوها
templates/   صفحات HTML
static/      فایل‌های استاتیک
        </code></pre>



</body>
</html>
