from flask import render_template
from app.main import bp

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Home')

@bp.route('/MDS', methods=['GET', 'POST'])
def MDS():
    return render_template('MDS.html', title='Model Design Studio')

@bp.route('/TDR', methods=['GET', 'POST'])
def TDR():
    return render_template('TDR.html', title='The Duel: Reloaded')
