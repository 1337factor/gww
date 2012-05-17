# JSON widget/formfield/modelfield (from http://www.davidcramer.net/code/448/cleaning-up-with-json-and-sql.html)
import json
from django.db import models
from django import forms


class JSONWidget(forms.Textarea):
	def render(self, name, value, attrs=None):
		if not isinstance(value, basestring):
			value = json.dumps(value, indent=2)
		return super(JSONWidget, self).render(name, value, attrs)


class JSONFormField(forms.CharField):
	def __init__(self, *args, **kwargs):
		kwargs['widget'] = JSONWidget
		super(JSONFormField, self).__init__(*args, **kwargs)


	def clean(self, value):
		if not value: return
		try:
			return json.loads(value)
		except Exception, exc:
			raise forms.ValidationError(u'JSON decode error: %s' % (unicode(exc),))


class JSONField(models.TextField):
	__metaclass__ = models.SubfieldBase


	def formfield(self, **kwargs):
		return super(JSONField, self).formfield(form_class=JSONFormField, **kwargs)


	def to_python(self, value):
		try:
			if isinstance(value, basestring):
				value = json.loads(value)
		except ValueError:
			pass
		return value


	def get_db_prep_value(self, value, connection=None, prepared=False):
		if not prepared:
			if value is not None:
				value = json.dumps(value)
		return value


	def value_to_string(self, obj):
		value = self._get_val_from_obj(obj)
		return self.get_db_prep_value(value)