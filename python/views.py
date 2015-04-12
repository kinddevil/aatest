from flask import Flask, request, render_template, url_for

app = Flask(__name__)
app.debug = True

@app.route('/main')
def hello_world():
    #return 'Hello World!'
    return render_template("main.html", title="title",content="content")

@app.route('/table')
def table():
    #return 'Hello World!'
    return render_template("table.html", title="title",content="content")

@app.route('/dpimain')
def dpimain():
    #return 'Hello World!'
    return render_template("dpi_app_device.html")

if __name__ == '__main__':
    app.run()
