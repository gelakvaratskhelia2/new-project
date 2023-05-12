from flask import Flask, render_template, request

app = Flask(__name__)

# მაგალითისთვის რომელიც იყენებს რეგისტრაციის ფორმას
@app.route("/home")
def home():
    return render_template("home.html")
@app.route("/about")
def about():


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # მოთხოვნას შევქმნათ ბაზაში ინფორმაციის ჩაწერისთვის

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
