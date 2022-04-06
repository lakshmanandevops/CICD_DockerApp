from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def hello_geek1():
    return render_template('index.html')
    
@app.route('/health')
def hello_geek2():
    # add your logic to evaluate your application health
     return render_template('health.html')

if __name__ == "__main__":
    app.run(debug=True)