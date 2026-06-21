<div align="center">

# DAL — DeepSeek API Linux

**A terminal-based DeepSeek AI assistant with Linux automation capabilities**

---

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40+-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20(WSL)-FCC624?style=for-the-badge&logo=linux&logoColor=white)]()

</div>

---

## 🌐 Language / زبان / Язык

<details>
<summary><b>🔽 Select Language</b></summary>

- 🇬🇧 [English](#-about) (English)
- 🇮🇷 [فارسی](#-درباره-پروژه) (Persian)
- 🇷🇺 [Русский](#-о-проекте) (Russian)

</details>

---

<div id="about">

## 🇬🇧 English

### About

**DAL (DeepSeek API Linux)** is a Python-based tool that provides a terminal interface to interact with DeepSeek's AI model. It uses browser automation via Playwright to communicate with DeepSeek's web interface, giving you a native terminal experience without needing API keys.

### Features

| Feature | Description |
|---------|-------------|
| 💬 **Chat Mode** | Interactive terminal chat with DeepSeek AI |
| 🖥️ **Linux Automation** | AI-driven terminal commands for system tasks |
| 🔧 **Root Elevation** | Automatic sudo privilege handling |
| 🐄 **Cowsay Output** | Friendly command output visualization |
| 🌍 **Cross-Platform** | Native Linux + Windows (via WSL) support |

### How It Works

DAL automates a real browser session to `chat.deepseek.com` using Playwright with stealth mode. It:

1. Launches a Chromium/Firefox browser with anti-detection measures
2. Logs into your DeepSeek account automatically
3. Provides a terminal interface to send prompts and receive responses
4. In Linux mode, executes AI-generated commands in real-time

### Modes

#### 💬 Normal Chat Mode
Simple conversational interface — type a prompt, get a response from DeepSeek.

#### 🖥️ Linux Terminal Mode
The AI analyzes your task, generates Linux commands, and executes them step by step with output verification.

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/dal.git
cd dal

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Configure your credentials
# Edit creds.py with your DeepSeek account credentials
```

### Configuration

Edit `creds.py` with your DeepSeek account credentials:

```python
email = "your-email@example.com"
password = "your-password"
```

### Usage

```bash
# Normal chat mode
python main.py firefox

# Linux automation mode
python main.py chrome
```

**Arguments:**
- First argument: Browser type (`firefox` or `chrome`)

### Project Structure

```
dal/
├── main.py              # Entry point
├── creds.py             # Credentials configuration
├── art.py               # ASCII art banner
├── requirements.txt     # Python dependencies
├── Mods/
│   ├── Message.py       # Send/receive messages
│   └── Setup.py         # Browser detection
├── initMods/
│   ├── Loginer.py       # DeepSeek login automation
│   ├── GetLastResponse.py  # Response extraction
│   └── initMessages.py  # System prompts
├── useExamples/
│   └── chatWithModel.py # Chat loop implementation
├── docs/                # Documentation
└── test/                # Tests
```

### Requirements

- Python 3.10+
- Chromium or Firefox browser
- Linux native or Windows with WSL

### Disclaimer

This tool is for educational purposes. Use responsibly and in accordance with DeepSeek's terms of service.

</div>

---

<div id="درباره-پروژه">

## 🇮🇷 فارسی

### درباره پروژه

**DAL (DeepSeek API Linux)** یک ابزار پایتونی است که رابط خط فرمانی برای تعامل با مدل هوش مصنوعی DeepSeek فراهم می‌کند. این ابزار از اتوماسیون مرورگر از طریق Playwright برای ارتباط با رابط وب DeepSeek استفاده می‌کند و تجربه خط فرمان بومی را بدون نیاز به کلیدهای API در اختیار شما قرار می‌دهد.

### امکانات

| ویژگی | توضیحات |
|-------|---------|
| 💬 **حالت چت** | چت تعاملی خط فرمان با هوش مصنوعی DeepSeek |
| 🖥️ **اتوماسیون لینوکس** | دستورات خط فرمان هوشمند برای وظایف سیستم |
| 🔧 **ارتقای Root** | مدیریت خودکار دسترسی sudo |
| 🐄 **خروجی Cowsay** | نمایش دوستانه خروجی دستورات |
| 🌍 **چند پلتفرمی** | پشتیبانی از لینوکس بومی + ویندوز (از طریق WSL) |

### نحوه کار

DAL یک جلسه مرورگر واقعی به `chat.deepseek.com` را با استفاده از Playwright با حالت مخفی خودکار می‌کند:

1. راه‌اندازی مرورگر Chromium/Firefox با اقدامات ضد تشخیص
2. ورود خودکار به حساب DeepSeek شما
3. فراهم کردن رابط خط فرمان برای ارسال پرامپت و دریافت پاسخ
4. در حالت لینوکس، اجرای دستورات تولید شده توسط هوش مصنوعی در زمان واقعی

### حالت‌ها

#### 💬 حالت چت عادی
رابط مکالمه‌ای ساده — پرامپت تایپ کنید، پاسخ DeepSeek را دریافت کنید.

#### 🖥️ حالت ترمینال لینوکس
هوش مصنوعی وظیفه شما را تحلیل می‌کند، دستورات لینوکس تولید می‌کند و آن‌ها را مرحله به مرحله با تأیید خروجی اجرا می‌کند.

### نصب

```bash
# کلون مخزن
git clone https://github.com/your-username/dal.git
cd dal

# نصب وابستگی‌ها
pip install -r requirements.txt

# نصب مرورگرهای Playwright
playwright install chromium

# پیکربندی اطلاعات ورود
# فایل creds.py را با اطلاعات حساب DeepSeek خود ویرایش کنید
```

### پیکربندی

فایل `creds.py` را با اطلاعات حساب DeepSeek خود ویرایش کنید:

```python
email = "your-email@example.com"
password = "your-password"
```

### استفاده

```bash
# حالت چت عادی
python main.py firefox

# حالت اتوماسیون لینوکس
python main.py chrome
```

**آرگومان‌ها:**
- آرگومان اول: نوع مرورگر (`firefox` یا `chrome`)

### ساختار پروژه

```
dal/
├── main.py              # نقطه ورود
├── creds.py             # پیکربندی اطلاعات ورود
├── art.py               # بنر ASCII art
├── requirements.txt     # وابستگی‌های پایتون
├── Mods/
│   ├── Message.py       # ارسال/دریافت پیام‌ها
│   └── Setup.py         # تشخیص مرورگر
├── initMods/
│   ├── Loginer.py       # اتوماسیون ورود DeepSeek
│   ├── GetLastResponse.py  # استخراج پاسخ
│   └── initMessages.py  # پرامپت‌های سیستم
├── useExamples/
│   └── chatWithModel.py # پیاده‌سازی حلقه چت
├── docs/                # مستندات
└── test/                # تست‌ها
```

### پیش‌نیازها

- پایتون 3.10+
- مرورگر Chromium یا Firefox
- لینوکس بومی یا ویندوز با WSL

### سلب مسئولیت

این ابزار برای اهداف آموزشی است. مسئولانه و مطابق با شرایط خدمات DeepSeek استفاده کنید.

</div>

---

<div id="о-проекте">

## 🇷🇺 Русский

### О проекте

**DAL (DeepSeek API Linux)** — это инструмент на базе Python, предоставляющий интерфейс командной строки для взаимодействия с AI-моделью DeepSeek. Он использует автоматизацию браузера через Playwright для связи с веб-интерфейсом DeepSeek, обеспечивая нативный опыт работы в командной строке без необходимости ключей API.

### Возможности

| Возможность | Описание |
|-------------|----------|
| 💬 **Режим чата** | Интерактивный чат в командной строке с DeepSeek AI |
| 🖥️ **Автоматизация Linux** | AI-управляемые команды для системных задач |
| 🔧 **Повышение до Root** | Автоматическая обработка прав sudo |
| 🐄 **Вывод Cowsay** | Дружелюбная визуализация вывода команд |
| 🌍 **Кроссплатформенность** | Нативная поддержка Linux + Windows (через WSL) |

### Как это работает

DAL автоматизирует реальную сессию браузера к `chat.deepseek.com` с помощью Playwright в режиме стелс:

1. Запускает Chromium/Firefox с мерами по защите от обнаружения
2. Автоматически входит в ваш аккаунт DeepSeek
3. Предоставляет интерфейс командной строки для отправки запросов и получения ответов
4. В режиме Linux выполняет команды, сгенерированные AI, в реальном времени

### Режимы

#### 💬 Обычный режим чата
Простой интерфейс для общения — введите запрос, получите ответ от DeepSeek.

#### 🖥️ Режим терминала Linux
AI анализирует вашу задачу, генерирует команды Linux и выполняет их пошагово с проверкой вывода.

### Установка

```bash
# Клонирование репозитория
git clone https://github.com/your-username/dal.git
cd dal

# Установка зависимостей
pip install -r requirements.txt

# Установка браузеров Playwright
playwright install chromium

# Настройка учётных данных
# Отредактируйте creds.py с вашими учётными данными DeepSeek
```

### Настройка

Отредактируйте `creds.py` с вашими учётными данными DeepSeek:

```python
email = "your-email@example.com"
password = "your-password"
```

### Использование

```bash
# Обычный режим чата
python main.py firefox

# Режим автоматизации Linux
python main.py chrome
```

**Аргументы:**
- Первый аргумент: тип браузера (`firefox` или `chrome`)

### Структура проекта

```
dal/
├── main.py              # Точка входа
├── creds.py             # Конфигурация учётных данных
├── art.py               # ASCII art баннер
├── requirements.txt     # Зависимости Python
├── Mods/
│   ├── Message.py       # Отправка/получение сообщений
│   └── Setup.py         # Определение браузера
├── initMods/
│   ├── Loginer.py       # Автоматизация входа в DeepSeek
│   ├── GetLastResponse.py  # Извлечение ответов
│   └── initMessages.py  # Системные промпты
├── useExamples/
│   └── chatWithModel.py # Реализация цикла чата
├── docs/                # Документация
└── test/                # Тесты
```

### Требования

- Python 3.10+
- Браузер Chromium или Firefox
- Нативный Linux или Windows с WSL

### Отказ от ответственности

Этот инструмент предназначен для образовательных целей. Используйте его ответственно и в соответствии с условиями использования DeepSeek.

</div>

---

<div align="center">

Made with ❤️ by **Yasin Qusemi**

</div>
