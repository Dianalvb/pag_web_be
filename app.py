from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Sobre')
def sobre():
    return render_template('sobremi.html')

    if __name__ =='__main__':
        app.run()