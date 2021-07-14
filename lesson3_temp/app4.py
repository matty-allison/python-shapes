from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def first():
    return "<h1>hello</h1>"
@app.route('/<person>/user')
def home(person):
    return  render_template('htmlapp.html', name=True, person=person)
@app.route('/<number>/')
def mulitply(number):
    return render_template('multipe.html', number=number)
@app.route('/<person>/page2/')
def page2(person):
    info = [{'greeting1': 'Hello', 'person': person},{'greeting2': 'Goodbye', 'person': person}]
    return render_template('loops.html', enter=True, info=info)

if __name__ =='__main__':
    app.debug=True
    app.run()
