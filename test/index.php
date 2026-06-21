<?phpecho "<!DOCTYPE html><html lang=\"en\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Dark Theme Hello World</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
            font-family: \"Segoe UI\", Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #ffffff;
        }
        .container {
            text-align: center;
            background: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 50px 80px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.1);
            animation: fadeIn 1.5s ease-in;
        }
        h1 {
            font-size: 3em;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            margin-bottom: 20px;
        }
        p {
            font-size: 1.2em;
            color: #cccccc;
            margin-top: 10px;
        }
        .emoji {
            font-size: 4em;
            margin-bottom: 20px;
            animation: bounce 2s infinite;
        }
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        @keyframes bounce {
            0%, 100% {
                transform: translateY(0);
            }
            50% {
                transform: translateY(-10px);
            }
        }
        .time {
            margin-top: 20px;
            font-size: 0.9em;
            color: #888888;
        }
    </style>
</head>
<body>
    <div class=\"container\">
        <div class=\"emoji\">🌙✨</div>
        <h1>Hello World!</h1>
        <p>Welcome to the dark themed page</p>
        <p>PHP is working perfectly 🚀</p>
        <div class=\"time\">
            Server time: \" . date(\"Y-m-d H:i:s\") . \"
        </div>
    </div>
</body>
</html>";
?>
