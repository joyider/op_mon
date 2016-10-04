#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# op_mon (c) 2016 by Andre Karlsson<andre.karlsson@protractus.se>
#
# This file is part of op_mon.
#
#    op_mon is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Foobar is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#
# Filename:  by: andrek
# Timesamp: 10/4/16 :: 12:42 AM
from flask import Blueprint, render_template, session, current_app, request, flash
from flask_login import login_required
from flask_themes2 import render_theme_template
from op_mon.utils import admin_required, flash_errors
from op_mon.user.models import Host

from op_mon.admin.forms import AddHostForm

blueprint = Blueprint('admin', __name__, url_prefix='/admin', static_folder='../static')

@blueprint.route('/hosts/', methods=['GET', 'POST'])
#@admin_required
def hosts():
    """List members."""
    hostform=AddHostForm(request.form)
    if request.method == 'POST':
	    if hostform.validate_on_submit():
			Host.create(hostname=hostform.hostname.data, username=hostform.username.data,
						password=hostform.password.data, nix=hostform.isnix.data,
						remote=hostform.isremote.data, active=(hostform.isactive.data))
			flash('Host was successfully added.', 'success')
			return render_theme_template(session.get('theme', current_app.config['DEFAULT_THEME']),
			                             'admin/dashboard.html', hostform=hostform)
	    else:
		    flash_errors(hostform)
    return render_theme_template(session.get('theme', current_app.config['DEFAULT_THEME']),
                                 'admin/dashboard.html', hostform=hostform)
