# -*- coding: utf-8 -*-
"""Application assets."""
from flask_assets import Bundle, Environment


js = Bundle(
    'libs/jQuery/dist/jquery.js',
    filters='jsmin',
    output='public/js/common.js'
)

assets = Environment()

# ßassets.register('js_all', js)
# assets.register('css_all', css)
