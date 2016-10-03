# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
from flask import flash
from flask_login import current_user
from functools import wraps
from flask import g, request, redirect, url_for

from op_mon.user.models import User


def flash_errors(form, category='warning'):
	"""Flash all errors for a form."""
	for field, errors in form.errors.items():
		for error in errors:
			flash('{0} - {1}'.format(getattr(form, field).label.text, error), category)


def admin_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if current_user is None:
			return redirect(url_for('login', next=request.url))
		if not User.is_admin:
			flash('Not auhorized to edit', 'warning')
			return redirect(url_for(request.url))
		return f(*args, **kwargs)
	return decorated_function
