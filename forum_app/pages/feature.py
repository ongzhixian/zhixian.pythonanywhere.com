from flask import render_template, session, request, redirect, url_for
from forum_app import app
from forum_app.modules.feature import Feature

@app.route('/feature/')
def root_feature_get():
    """Web page at '/feature'"""
    return redirect('/feature/dashboard')

@app.route('/feature/dashboard')
def feature_dashboard_page():
    """Web page at '/feature/dashboard'"""
    return render_template('feature/feature_dashboard.html')

@app.route('/feature/register')
def feature_register_page():
    """Web page at '/feature/register'"""
    feature = Feature()
    registered_feature_count = feature.get_registered_feature_count()
    return render_template('feature/feature_register.html', 
        registered_feature_count = registered_feature_count)
    
@app.route('/feature/register', methods=['POST'])
def feature_register_post():
    """Web page at '/feature/register'"""
    feature = Feature()

    feature_module_actions = {
        'register-built-in': feature.register_built_in_features,
        'diagnose': feature.diagnose,
    }

    action = request.form.get("action")

    if action in feature_module_actions:
        feature_module_actions[action]()

    registered_feature_count = feature.get_registered_feature_count()

    return render_template('feature/feature_register.html', 
            registered_feature_count = registered_feature_count)

    # return render_template('feature/feature_register.html', 
    #     registered_feature_count = registered_feature_count)
    