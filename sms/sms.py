from flask import Flask
app = Flask(__name__)


@app.route('/getURI', methods=['GET', 'POST'])
def getUri(): 
    print (request.args)
    return request.args

if __name__ == '__main__':
    app.run()