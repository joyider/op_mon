# -*- coding: utf-8 -*-
"""Application assets."""
from flask_assets import Bundle, Environment
from flask import current_app, session
from flask_themes2 import static_file_url

css = Bundle(
	'libs/font-awesome4/css/font-awesome.min.css',
	'libs/simple-line-icons/simple-line-icons.min.css',
    'libs/bootstrap/dist/css/bootstrap.css',
	'libs/uniform/css/uniform.default.css',
	'libs/bootstrap-switch/css/bootstrap-switch.min.css',
	'libs/morris/morris.css',
	'css/components.min.css',
	'css/plugins.min.css',
    filters='cssmin',
    output='public/css/common.css'
)

js = Bundle(
    'libs/jquery.min.js',
	'libs/bootstrap/dist/js/bootstrap.min.js',
	'libs/bootstrap-hover-dropdown/bootstrap-hover-dropdown.min.js',
	'libs/jquery-slimscroll/jquery.slimscroll.min.js',
	'libs/uniform/jquery.uniform.min.js',
	'libs/jquery.blockui.min.js',
	'libs/morris/morris.min.js',
	'libs/morris/raphael-min.js',
	'libs/bootstrap-switch/js/bootstrap-switch.min.js',
	'js/app.min.js',
	'js/dashboard.min.js',
	'js/layout.min.js',
	'js/demo.min.js',
	'js/quick-sidebar.min.js',
    filters='jsmin',
    output='public/js/common.js'
)

assets = Environment()

assets.register('js_all', js)
assets.register('css_all', css)