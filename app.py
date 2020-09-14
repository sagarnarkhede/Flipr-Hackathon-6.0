from flask import Flask, render_template
app = Flask(__name__)
from fetch_api import *

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/notification")
def notification():
    dish = fetch_data_notifications(notifications_url)
    return render_template('notification.html', a=dish)


@app.route("/deceased_person")
def post():
    a=fetch_data_medical_colleges(medical_colleges_url)
    return render_template('comparison.html',l=a)

@app.route("/hd")
def hd():
    a=fetch_data_hospitals_beds(hospitals_beds_url)
    return render_template('hospital.html',l=a)

@app.route("/cd")
def cd():
    a=fetch_data_medical_colleges(medical_colleges_url)
    return render_template('clg.html',l=a)

# @app.route("/team")
# def team():
#     return render_template('team.html')

@app.route("/contact")
def contact():
    send_dict = fetch_data_contacts(contacts_url)
    return render_template('contact.html', send_dict=send_dict)

if __name__ == '__main__':
    app.run(debug=True)


