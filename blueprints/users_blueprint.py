from flask import Blueprint, request, render_template, url_for, redirect
from faker import Faker

users_blueprint = Blueprint('users', __name__, url_prefix='/users')

fake = Faker()


@users_blueprint.route('/generate')
def generate_view():
    """
    This view will generate a list of users.
    The number of users is determined by the count query parameter.
    If no count is provided, 100 users will be generated.
    """

    count = request.args.get('count', 100)
    users = [{"name": fake.name(), "email": fake.email()} for _ in range(int(count))]
    return render_template('users.html', title="Users", users=users)