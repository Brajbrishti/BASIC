from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  ### file name should be string

@app.route("/submit",methods=["POST"])

def submit():
    name=request.form["student_name"]
    age=request.form["student_age"]
    email = request.form["student_email"]
    city=request.form["city"]
    
    return f""" 
    <h2>Student Detail</h2>
    
    Student Name : {name}
    <br>
    Student Age : {age}
    <br>
    Student Email :{email}
    <br>
    Student City :{city}
            
    """


@app.route("/about")
def about():
    return render_template("about.html")   ### file name should be string

@app.route("/contact")
def contact():
    return render_template("contact.html")   ### file name should be string

if __name__ == "__main__":
    app.run(debug=True)   ### server will start 
    
   