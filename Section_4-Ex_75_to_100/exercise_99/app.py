from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
        
        with open('new.txt', 'w') as file:
            if request.method == 'POST':
                var = request.form.get('content')
                file.write(var)
        return render_template('base.html')
    

if __name__ == "__main__":
    app.run(debug=True)
