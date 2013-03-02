import csv

from django import forms
from django.utils.translation import ugettext_lazy as _


class CSVHistoryField(forms.FileField):
    REQUIRED_HEADERS = ['DATE', 'AMOUNT', 'DESC']

    def to_python(self, value):
        value = super(CSVHistoryField, self).to_python(value)
        reader = csv.reader(value)
        headers = reader.next()
        for required_header in CSVHistoryField.REQUIRED_HEADERS:
            if not required_header in headers:
                raise forms.ValidationError(_("File missing header: {0}".format(required_header)))

        return [dict(zip(headers, row)) for row in reader]


class UploadForm(forms.Form):
    history = CSVHistoryField()
