from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Ye function CSS file ko browser tak pahunchayega
@app.route('/')
def home():
    return render_template('index.html')

# Baki verify wala code niche same rahega...

@app.route('/verify', methods=['POST'])
def verify():
    # HTML ke 'name' attribute se data uthana
    user_name = request.form.get('u_name')
    try:
        user_age = int(request.form.get('u_age'))
        if user_age > 17:
            result = "AAWA CHALA KOTHA PE"
        else:
            result = "TU MARDWA CHHOT HWA"
    except:
        result = f"{user_name} tu latkhor hwa"
    
    return f"<body style='background:#1a1a2e; color:white; text-align:center; padding-top:100px; font-family:sans-serif;'><h1>{result}</h1><br><a href='/' style='color:cyan;'>Wapas Jao</a></body>"

if __name__ == '__main__':
    if __name__ == "__main__":
    app.run(debug=True)

