import concurrent.futures  # 並列処理

import flask
from flask_login import login_user, LoginManager, UserMixin, login_required, logout_user, current_user  # Login関係のライブラリ
from werkzeug.security import generate_password_hash, check_password_hash  # パスワードの暗号化
from flask_sqlalchemy import SQLAlchemy  # ORマッパー
from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)

# DBはSQLiteを使う
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.work_management_system'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
# sessionを使う際にSECRET_KEYを設定
app.config['SECRET_KEY'] = 'secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
# SQLAlchemyを使います宣言
db = SQLAlchemy(app)


# Userというクラス(データベースに格納するデータ)
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(40), unique=True)
    line_token = db.Column(db.String(120), unique=True)
    role = db.Column(db.Integer())


db.create_all()
bootstrap = Bootstrap(app)

# DBが空の状態(最初の1回)はadminを作成する
user = User.query.filter_by(username='admin').first()
if user is None:
    admin = User(username='admin',
                 password=generate_password_hash("admin", method='sha256'),
                 email='invest9me@yahoo.co.jp')
    db.session.add(admin)
    db.session.commit()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized():
    return flask.redirect('/login')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        # Userのインスタンスを作成
        new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    else:
        return render_template('auth/signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        # Userテーブルからusernameに一致するユーザを取得
        auth_user = User.query.filter_by(username=username).first()
        if check_password_hash(auth_user.password, password):
            login_user(auth_user)
            return redirect('/')
    else:
        return render_template('auth/login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


@app.route('/findwork')
@login_required  # ログイン状態のみアクセス可のおまじない
def find_work():  # 同じ名前の関数にするとエラーがでる　関数名は何でもよい
    return render_template('find_work/index.html')


@app.route('/', methods=["GET"])
@login_required
def index():
    auth_user = current_user.username
    print(auth_user)
    return render_template("index.html", auth_user=auth_user)


if __name__ == '__main__':
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    app.run(debug=True)
