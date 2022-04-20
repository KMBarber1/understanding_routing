from flask import Flask

app = Flask (__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def say(name):
    return f"Hi {name}"

@app.route('/repeat/<string:word>/<int:num>')
def repeat(word, num):
    return f"{word * num}"
    # return (word*int(num))

#provided solution
@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"

    return output

@app.route('/error')
def error(missing_file):
    return f"Sorry! No response. Try again."













if __name__=='__main__':
        app.run(debug=True)