"""Compile static assets."""
from flask import current_app as app
from flask_assets import Bundle,Environment

def compile_static_assets(assets):
    """Create stylesheet bundles."""
    assets = Environment(assets)
    Environment.auto_build = True
    Environment.debug = False
    assets.auto_build = True
    assets.debug = False
    common_less_bundle = Bundle(
        'src/less/*.less',
        filters='less,cssmin',
        output='dist/css/style.css',
        extra={'rel': 'stylesheet/less'}
    )
    home_less_bundle = Bundle(
        'home_bp/less/home.less',
        filters='less,cssmin',
        output='dist/css/home.css',
        extra={'rel': 'stylesheet/less'}
    )
    profile_less_bundle = Bundle(
        'profile_bp/less/profile.less',
        filters='less,cssmin',
        output='dist/css/profile.css',
        extra={'rel': 'stylesheet/less'}
    )
    product_less_bundle = Bundle(
        'products_bp/less/products.less',
        filters='less,cssmin',
        output='dist/css/products.css',
        extra={'rel': 'stylesheet/less'}
    )
    
    account_less_bundle = Bundle(
        'src/less/account.less',
        filters='less,cssmin',
        output=f'dist/css/account.css',
        extra={'rel': 'stylesheet/less'}
    )
    dashboard_less_bundle = Bundle(
        'src/less/dashboard.less',
        filters='less,cssmin',
        output=f'dist/css/dashboard.css',
        extra={'rel': 'stylesheet/less'}
    )
    
    # JavaScript Bundle
    js_bundle = Bundle(
        'src/js/main.js',
        filters='jsmin',
        output='dist/js/main.min.js'
    )
    
    assets.register('common_less_bundle', common_less_bundle)
    assets.register('home_less_bundle', home_less_bundle)
    assets.register('profile_less_bundle', profile_less_bundle)
    assets.register('account_less_bundle', account_less_bundle)
    assets.register('dashboard_less_bundle', dashboard_less_bundle)
    assets.register('js_all', js_bundle)
    # assets.register('product_less_bundle', product_less_bundle)
    if app.config['FLASK_ENV'] == 'development':
        common_less_bundle.build()
        home_less_bundle.build()
        profile_less_bundle.build()
        account_less_bundle.build()
        dashboard_less_bundle.build()
        js_bundle.build()
        # product_less_bundle.build()
    return assets
