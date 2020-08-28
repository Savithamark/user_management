"""General page routes."""
from flask import Blueprint, render_template
from flask import current_app as app

home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@home_bp.route('/', methods=['GET'])
def home():
    """Homepage."""
    return render_template(
        'index.jinja2',
        title='My First Blueprint Demo',
        subtitle='Demonstration of Flask blueprints in action.',
        template='home-template',

    )


@home_bp.route('/about', methods=['GET'])
def about():
    """About page."""
    return render_template(
        'index.jinja2',
        title="About",
        subtitle='This is an example about page.',
        template='home-template page'
    )


@home_bp.route('/contact', methods=['GET'])
def contact():
    """Contact page."""
    return render_template(
        'index.jinja2',
        title="Contact",
        subtitle='This is an example contact page.',
        template='home-template page'
    )
