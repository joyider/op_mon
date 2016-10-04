# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, current_app, session, g, app
from flask_login import login_required, login_user, logout_user, current_user
from flask_themes2 import render_theme_template, get_theme, get_themes_list, url_for

from op_mon.extensions import login_manager
from op_mon.public.forms import LoginForm
from op_mon.user.forms import RegisterForm
from op_mon.user.models import User
from op_mon.utils import flash_errors

blueprint = Blueprint('public', __name__, static_folder='../static')

@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route('/')
def home():
    """Home page."""
    # Handle logging in
    if current_user.is_authenticated:
        return render_theme_template(session.get('theme', current_app.config['DEFAULT_THEME']), 'users/dashboard.html')
    else:
        return redirect(url_for('public.login'), code=302)


@blueprint.route('/logout/')
@login_required
def logout():
    """Logout."""
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


@blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    """Register new user."""
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate_on_submit():
        User.create(username=form.username.data, email=form.email.data,
                    password=form.password.data, active=True)
        flash('Thank you for registering. You can now log in.', 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return render_template('public/register.html', form=form)


@blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    """Login Page."""
    form = LoginForm(request.form)
    # Handle logging in
    if request.method == 'POST':
        if form.validate_on_submit():
            login_user(form.user)
            flash('You are logged in.', 'success')
            redirect_url = request.args.get('next') or url_for('user.dashboard')
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_theme_template(session.get('theme', current_app.config['DEFAULT_THEME']), 'public/login.html', form=form)


# Below here is only code for development and theme testing
@blueprint.route('/themes/')
def themes():
    """Theme Page."""
    themes = get_themes_list()
    return render_theme_template(current_app.name, 'public/themes.html', themes=themes)

@blueprint.route('/themes/<ident>')
def settheme(ident):
    if ident not in current_app.theme_manager.themes:
        abort(404)
    session['theme'] = ident
    return redirect(url_for('public.themes'))
