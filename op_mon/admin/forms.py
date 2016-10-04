#!/usr/bin/python
# -*- coding: utf-8 -*-
# op_mon (c) 2016 by Andre Karlsson<andre.karlsson@protractus.se>
#
# NorseBot is licensed under a
# Creative Commons Attribution-NonCommercial-NoDerivs 3.0 Unported License.
#
# You should have received a copy of the license along with this
# work.  If not, see <http://creativecommons.org/licenses/by-nc-nd/3.0/>
#
#
# Filename: forms by: andrek
# Timesamp: 2016-10-04 :: 12:10

from flask_wtf import Form
from wtforms import PasswordField, StringField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from op_mon.user.models import Host

class AddHostForm(Form):

	hostname = StringField('Hostname',
							validators=[DataRequired(), Length(min=2, max=25)])
	username = StringField('Username',
							validators=[DataRequired(), Length(min=3, max=25)])
	password = PasswordField('Password',
							validators=[DataRequired(), Length(min=6, max=40)])
	confirm = PasswordField('Verify password',
							[DataRequired(), EqualTo('password', message='Passwords must match')])
	isnix = BooleanField()
	isremote = BooleanField()
	isactive = BooleanField()

	def __init__(self, *args, **kwargs):
		super(AddHostForm, self).__init__(*args, **kwargs)
		self.host = None

	def validate(self):
		"""
		Validate Form Data
		Trust the uniquness of UUID from model?
		:return: True if validation is OK else False
		"""
		initial_validation = super(AddHostForm, self).validate()
		if not initial_validation:
			return False
		self.host = Host.query.filter_by(hostname=self.hostname.data).first()
		if self.host:
			self.username.errors.append('Host already exists')
			return False
		return True