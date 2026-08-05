from flask import Flask
app_1 = Flask(__name__)  ### website create
@app_1.route("/")  ### open home page

def home():
    return"""
    <html>
        <body style="background-color: Blue;">
        <h1>Hello Everyone My Webpage</h1> 
        </body>
    </html>    
        """
if __name__ == "__main__":
           app_1.run(debug=True) ##### Isse server start hota hai http://127.0.0.1:5000
        
