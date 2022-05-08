from config import app,s3_app
import routes

@app.route('/')
def greet():
    return "Hello Flask app is running!!!"

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0") 