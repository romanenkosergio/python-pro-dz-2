from flask import Blueprint, render_template
import csv

mean_blueprint = Blueprint('mean_blueprint', __name__, url_prefix='/mean')


@mean_blueprint.route('/')
def mean_view():
    """Calculate the mean of the weights and heights in the csv file and return the result to the template."""
    with open('static/hw.csv', 'r') as f:
        weights = []
        heights = []
        csvreader = csv.reader(f)
        next(csvreader, None)
        for row in csvreader:
            if row:
                weights.append(float(row[1]))
                heights.append(float(row[2]))

        mean_weight = round(sum(weights) / len(weights), 1)
        mean_height = round(sum(heights) / len(heights), 1)
    return render_template('mean.html', title='Mean', weight=mean_weight, height=mean_height)
