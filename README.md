<div align="center">

# DAL - DeepSeek API Linux

**A terminal-based DeepSeek AI assistant with Linux automation capabilities**

---

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40+-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/)
[![License](https://img.shields.io/badge/License-GNU-yellow?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20(WSL)-FCC624?style=for-the-badge&logo=linux&logoColor=white)]()

</div>

---

## Language / زبان / Язык

<details>
<summary><b>Select Language</b></summary>

- [English](#-about) (English)
- [فارسی](#-درباره-پروژه) (Persian)
- [Русский](#-о-проекте) (Russian)

</details>

---

<details open>
<summary><h2>English</h2></summary>

### About

**DAL (DeepSeek API Linux)** is a Python-based tool that provides a terminal interface to interact with DeepSeek's AI model. It uses browser automation via Playwright to communicate with DeepSeek's web interface, giving you a native terminal experience without needing API keys.

### Features

| Feature | Description |
|---------|-------------|
| **Chat Mode** | Interactive terminal chat with DeepSeek AI |
| **Linux Automation** | AI-driven terminal commands for system tasks |
| **Root Elevation** | Automatic sudo privilege handling |
| **Cowsay Output** | Friendly command output visualization |
| **Cross-Platform** | Native Linux + Windows (via WSL) support |

### How It Works

DAL automates a real browser session to `chat.deepseek.com` using Playwright with stealth mode. It:

1. Launches a Chromium/Firefox browser with anti-detection measures
2. Logs into your DeepSeek account automatically
3. Provides a terminal interface to send prompts and receive responses
4. In Linux mode, executes AI-generated commands in real-time

### Modes

#### Normal Chat Mode
Simple conversational interface -- type a prompt, get a response from DeepSeek.

#### Linux Terminal Mode
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
python main.py
```

The application will automatically detect and use Chromium.

### Project Structure

```
dal/
  main.py              # Entry point
  creds.py             # Credentials configuration
  art.py               # ASCII art banner
  requirements.txt     # Python dependencies
  Mods/
    Message.py         # Send/receive messages
    Setup.py           # Browser detection
    Sudo.py            # Root elevation & command execution
  initMods/
    Loginer.py         # DeepSeek login automation
    GetLastResponse.py # Response extraction
    initMessages.py    # System prompts
  useExamples/
    chatWithModel.py   # Chat loop implementation
  docs/                # Documentation
  test/                # Tests
```

### Requirements

- Python 3.10+
- Chromium or Firefox browser
- Linux native or Windows with WSL

### Disclaimer

This tool is for educational purposes. Use responsibly and in accordance with DeepSeek's terms of service.

</details>

---

<details>
<summary><h2>فارسی</h2></summary>

### درباره پروژه

**DAL (DeepSeek API Linux)** يك ابزار پايتوني است كه رابط خط فرمان براي تعامل با مدل هوش مصنوعي DeepSeek فراهم مي‌كند. اين ابزار از اتوماسيون مرورگر از طريق Playwright براي ارتباط با رابط وب DeepSeek استفاده مي‌كند و تجربه خط فرمان بومي را بدون نياز به كليدهاي API در اختيار شما قرار مي‌دهد.

### امكانات

| ويژگي | توضيحات |
|-------|---------|
| **حالت چت** | چت تعاملی خط فرمان با هوش مصنوعی DeepSeek |
| **اتوماسيون لينوكس** | دستورات خط فرمان هوشمند براي وظايف سيستم |
| **ارتقای Root** | مديريت خودکار دسترسی sudo |
| **خروجي Cowsay** | نمايش دوستانه خروجي دستورات |
| **چند پلتفرمي** | پشتيباني از لينوكس بومي + ويندوز (از طريق WSL) |

### نحوه كار

DAL يك جلسه مرورگر واقعي به `chat.deepseek.com` را با استفاده از Playwright با حالت مخفي خودكار مي‌كند:

1. راه‌اندازي مرورگر Chromium/Firefox با اقدامات ضد تشخيص
2. ورود خودكار به حساب DeepSeek شما
3. فراهم كردن رابط خط فرمان براي ارسال پرامپت و دريافت پاسخ
4. در حالت لينوكس، اجراي دستورات توليد شده توسط هوش مصنوعي در زمان واقعي

### حالت‌ها

#### حالت چت عادي
رابط مكالمه‌اي ساده -- پرامپت تايپ كنيد، پاسخ DeepSeek را دريافت كنيد.

#### حالت ترمينال لينوكس
هوش مصنوعي وظيفه شما را تحليل مي‌كند، دستورات لينوكس توليد مي‌كند و آن‌ها را مرحله به مرحله با تاييد خروجي اجرا مي‌كند.

### نصب

```bash
# كلون مخزن
git clone https://github.com/your-username/dal.git
cd dal

# نصب وابستگي‌ها
pip install -r requirements.txt

# نصب مرورگرهاي Playwright
playwright install chromium

# پيكربيدي اطلاعات ورود
# فايل creds.py را با اطلاعات حساب DeepSeek خود ويرايش كنيد
```

### پيكربيدي

فايل `creds.py` را با اطلاعات حساب DeepSeek خود ويرايش كنيد:

```python
email = "your-email@example.com"
password = "your-password"
```

### استفاده

```bash
python main.py
```

برنامه به طور خودکار Chromium را شناسایی و استفاده می‌کند.

### ساختار پروژه

```
dal/
  main.py              # نقطه ورود
  creds.py             # پيكربيدي اطلاعات ورود
  art.py               # بنر ASCII art
  requirements.txt     # وابستگي‌هاي پايتون
  Mods/
    Message.py         # ارسال/دریافت پیام‌ها
    Setup.py           # تشخيص مرورگر
    Sudo.py            # ارتقا به root و اجراي دستورات
  initMods/
    Loginer.py         # اتوماسيون ورود DeepSeek
    GetLastResponse.py # استخراج پاسخ
    initMessages.py    # پرامپت‌هاي سيستم
  useExamples/
    chatWithModel.py   # پياده‌سازي حلقه چت
  docs/                # مستندات
  test/                # تست‌ها
```

### پيش‌نيازها

- پايتون 3.10+
- مرورگر Chromium يا Firefox
- لينوكس بومي يا ويندوز با WSL

### سلب مسئوليت

اين ابزار براي اهداف آموزشي است. مسئولانه و مطابق با شرايط خدمات DeepSeek استفاده كنيد.

</details>

---

<details>
<summary><h2>Русский</h2></summary>

### О проекте

**DAL (DeepSeek API Linux)** -- это инструмент на базе Python, предоставляющий интерфейс командной строки для взаимодействия с AI-моделью DeepSeek. Он использует автоматизацию браузера через Playwright для связи с веб-интерфейсом DeepSeek, обеспечивая нативный опыт работы в командной строке без необходимости ключей API.

### Возможности

| Возможность | Описание |
|-------------|----------|
| **Режим чата** | Интерактивный чат в командной строке с DeepSeek AI |
| **Автоматизация Linux** | AI-управляемые команды для системных задач |
| **Повышение до Root** | Автоматическая обработка прав sudo |
| **Вывод Cowsay** | Дружелюбная визуализация вывода команд |
| **Кроссплатформенность** | Нативная поддержка Linux + Windows (через WSL) |

### Как это работает

DAL автоматизирует реальную сессию браузера к `chat.deepseek.com` с помощью Playwright в режиме стелс:

1. Запускает Chromium/Firefox с мерами по защите от обнаружения
2. Автоматически входит в ваш аккаунт DeepSeek
3. Предоставляет интерфейс командной строки для отправки запросов и получения ответов
4. В режиме Linux выполняет команды, сгенерированные AI, в реальном времени

### Режимы

#### Обычный режим чата
Простой интерфейс для общения -- введите запрос, получите ответ от DeepSeek.

#### Режим терминала Linux
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
python main.py
```

Приложение автоматически обнаружит и использует Chromium.

### Структура проекта

```
dal/
  main.py              # Точка входа
  creds.py             # Конфигурация учётных данных
  art.py               # ASCII art баннер
  requirements.txt     # Зависимости Python
  Mods/
    Message.py         # Отправка/получение сообщений
    Setup.py           # Определение браузера
    Sudo.py            # Повышение до root и выполнение команд
  initMods/
    Loginer.py         # Автоматизация входа в DeepSeek
    GetLastResponse.py # Извлечение ответов
    initMessages.py    # Системные промпты
  useExamples/
    chatWithModel.py   # Реализация цикла чата
  docs/                # Документация
  test/                # Тесты
```

### Требования

- Python 3.10+
- Браузер Chromium или Firefox
- Нативный Linux или Windows с WSL

### Отказ от ответственности

Этот инструмент предназначен для образовательных целей. Используйте его ответственно и в соответствии с условиями использования DeepSeek.

</details>

---

<div align="center">

Made by **Yasin Qusemi**

</div>
