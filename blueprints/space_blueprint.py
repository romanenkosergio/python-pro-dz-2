from flask import Blueprint, render_template
import requests

space_blueprint = Blueprint('space_blueprint', __name__, url_prefix='/space')


@space_blueprint.route('/')
def space_view():
    """This view will return the number of astronauts in space."""
    astronauts = requests.get('http://api.open-notify.org/astros.json').json()
    return render_template('space.html', title='Space', astronauts_count=astronauts['number'])
