from flask import Flask, render_template

app = Flask(__name__)

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the crop management page
@app.route('/crop')
def crop():
    return render_template('crop.html')

# Route for the farm management page
@app.route('/farm')
def farm():
    return render_template('farm.html')

# Route for the resource tracking page
@app.route('/resource')
def resource():
    return render_template('resource.html')


if __name__ == '__main__':
    app.run(debug=True)
