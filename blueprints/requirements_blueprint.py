from flask import Blueprint, render_template

requirements_blueprint = Blueprint('requirements_blueprint', __name__, url_prefix='/requirements')


@requirements_blueprint.route('/')
def requirements_view():
    """Read the requirements.txt file and return the result to the template."""
    with open('requirements.txt', 'r') as f:
        requirements = f.read().split('\n')
        requirements = [requirement.split('==') for requirement in requirements]
    return render_template('requirements.html', title='Requirements', requirements=requirements)