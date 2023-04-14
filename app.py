from flask import Flask, render_template

from blueprints.users_blueprint import users_blueprint
from blueprints.errors_blueprint import errors_blueprint
from blueprints.space_blueprint import space_blueprint
from blueprints.mean_blueprint import mean_blueprint
from blueprints.requirements_blueprint import requirements_blueprint

app = Flask(__name__)
app.register_blueprint(users_blueprint)
app.register_blueprint(errors_blueprint)
app.register_blueprint(space_blueprint)
app.register_blueprint(mean_blueprint)
app.register_blueprint(requirements_blueprint)

app.debug = True


@app.route('/')
def home_view():
    return render_template('home.html', title='Home')


if __name__ == '__main__':
    app.run()
