from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SelectField, SubmitField, HiddenField
from wtforms.validators import DataRequired

def createDictForSelect(models):
	ret_list = []
	for model in models:
		ret_list.append((model.name, model.name))

	return ret_list


