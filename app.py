
import base64,random,time
from flask import Flask, request
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


app = Flask(__name__)

users={
    "magigo":["123456"]
}


def gen_token(uid):
    token_str =':'.join([str(uid),str(random.random()),str(time.time() + 7200)]).encode("utf-8")
    print(type(token_str))
    token = base64.b64encode(token_str)
    print(type(token))
    # users[uid].append(token)
    # token = Serializer("SECRET_KEY", expires_in=3600)
    users[uid].append(token)
    # 接收用户id转换与编码
    # token = s.dumps({"id": uid}).decode("ascii")
    return token



def verify_token(token):
    _token = base64.b64decode(token).decode()
    print(_token)
    print(users.get(_token.split(':')[0])[-1])
    print(users.get('magigo'))

    if not users.get(_token.split(':')[0])[-1] == '123456':
        return -1
    if float(_token.split(':')[-1]) >= time.time():
        return 1
    else:
        return 0


@app.route('/index', methods=['POST','GET'])
def index():
    print(request.headers)
    return 'hello'


@app.route('/login', methods=['POST','GET'])
def login():
    print(request.headers['Authorization'])
    authorization = str(request.headers['Authorization']).split(' ')[-1]
    uid_pw = base64.b64decode(authorization)
    uid, pw = uid_pw.decode().split(':')

    if users.get(uid)[0] == pw:
        return gen_token(uid)
    else:
        return 'error'


@app.route('/test1', methods=['POST','GET'])
def test():
    token = request.args.get('token')
    if verify_token(token) == 1:
        print('data')
        return 'data'
    else:
        return 'error'


@app.route('/')
def first_flask():
    return "<h1 style='color:red'>hello world</h1>"


if __name__ == '__main__':
    app.run(debug=True)
