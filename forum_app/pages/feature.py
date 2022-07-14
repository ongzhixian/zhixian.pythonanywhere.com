import logging

from flask import render_template, session, request, redirect, url_for
from forum_app import app
from forum_app.modules.feature import Feature
from forum_app.features import __all__ as available_features_count, BaseFeatureInterface
import pdb
from forum_app.modules import log

@app.route('/feature/')
def root_feature_get():
    """Web page at '/feature'"""
    return redirect('/feature/dashboard')

@app.route('/feature/dashboard')
def feature_dashboard_page():
    """Web page at '/feature/dashboard'"""
    # Get list of registered features
    feature = Feature()
    feature_list = feature.get_registered_feature_list()
    log.info("Render 'feature/feature_dashboard.html'")
    return render_template('feature/feature_dashboard.html', feature_list = feature_list)

@app.route('/feature/<feature_name>')
def feature_options_page(feature_name):
    """Web page at '/feature/<feature>'"""
    # Get list of registered features
    # feature = Feature()
    # feature_list = feature.get_registered_feature_list()
    # log.info("Render 'feature/feature_options.html'")
    option_list = []
    return render_template('feature/feature_options.html', option_list=option_list)



def validated_boolean_value(value):
    """Validates if given value is valid"""
    if value not in ('true', 'false'):
        return None
    if value == 'true':
        return True
    return False


def get_validated_toggle_content(form):
    """Validate content; 
    returns None if content is invalid
    returns feature_name, is_enable dictionary value if content is valid"""
    toggle_name = form.get("toggle_name")
    toggle_value = form.get("toggle_value")

    is_enable = validated_boolean_value(toggle_value)

     # If content does not contain 'toggle_name' or 'toggle_value', then its a bad request
    if toggle_name is None or is_enable is None:
        return None

    return {
        "feature_name": toggle_name,
        "is_enable": is_enable
    }

@app.route('/feature/dashboard', methods=['POST'])
def feature_dashboard_post():
    """Handles when user updates a feature toggle
    Originally implemented because pure API call does not update UI.
    After implementation, found that this implementation has its own set of issues:
    1. Stuttering on multiple consecutive updates.
    2. Blink on screen refresh
    Keeping this for future reference on why this is bad.
    Favouring API call
    """

    response_message = "Changes not saved"
    content = get_validated_toggle_content(request.form)
    if not content:
        return redirect(url_for("feature_dashboard_page"))

    base_feature = BaseFeatureInterface()
    change_saved = base_feature.toggle_enable(content['feature_name'], content['is_enable'])
    if change_saved:
        enabled_message = "enabled" if content['is_enable'] else "disabled"
        response_message = f"{content['feature_name']} {enabled_message}"
    logging.info(response_message)
    return redirect(url_for("feature_dashboard_page"))


@app.route('/feature/register')
def feature_register_page():
    """Web page at '/feature/register'"""
    feature = Feature()
    registered_feature_count = feature.get_registered_feature_count()
    return render_template('feature/feature_register.html', 
        registered_feature_count = registered_feature_count, 
        available_features_count = len(available_features_count))
    
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
            registered_feature_count = registered_feature_count,
            available_features_count = len(available_features_count))

    # return render_template('feature/feature_register.html', 
    #     registered_feature_count = registered_feature_count)
    