from flask import Flask
from flask import render_template

icon = "html_5.ico"

logos = {
    'cpp':"cpp_logo.png",
    'java':"java_logo.png", 
    'html':"html_logo.png",
    'python':"py_logo.png"
}

certificates = {
    'time':"EffectiveTimeManagement.png",
    'healthy':"HealthyHabitsForHealthyLife.png"
}

web = Flask(__name__)

@web.route("/")
@web.route("/home")
def home_page():
    return render_template("index.html",icon=icon)

@web.route("/projects")
def project_page():
    return render_template("project.html", logo_lst = logos)

@web.route("/certificates")
def certificate_page():
    return render_template("certificate.html",cert_lst = certificates)

if __name__ == "__main__":
    web.run(debug=True)