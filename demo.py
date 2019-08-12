from flask import Flask,render_template,flash,redirect,url_for
from forms import LoginForm


app = Flask(__name__)
app.secret_key = 'secret string'


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/pics', methods=['get', 'post'])
def pics():
    return render_template('pics.html')


@app.route('/flash')
def doflash():
    flash(u"你好，我是闪电")
    return redirect(url_for('index'))


# @app.route('/form')
# def form():
#     form = LoginForm()
#     return render_template('form.html', form=form)


@app.route('/recvform', methods=['get', 'post'])
def recvform():
    return 'welcome vip '


@app.route('/basic', methods=['GET', 'POST'])
def basic():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        flash('Welcome home, %s!' % username)
        return redirect(url_for('index'))
    return render_template('pics.html', form=form)


@app.route('/fc')
def fc():
    return render_template('fc.html')

@app.route('/st')
def fc():
    return render_template('st.html')

@app.route('/fcqs')
def fcqs():
    return render_template('fcqs.html')


@app.errorhandler(404)
def page404(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)