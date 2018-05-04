from flask import Flask,views

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

class SongleiView(views.MethodView):
    def get(self):
        return 'hello qiangzi'

    app.add_url_rule('qiangzi'view_func=SongleiView)


if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0',port=5000)
