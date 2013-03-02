import csv

from django import forms
from django.utils.translation import ugettext_lazy as _


class CSVHistoryField(forms.FileField):
    REQUIRED_HEADERS = ['DATE', 'AMOUNT', 'DESC']

    def clean(self, data, initial=None):
        super(CSVHistoryField, self).clean(data, initial)

        reader = csv.reader(data)
        headers = reader.next()
        for required_header in CSVHistoryField.REQUIRED_HEADERS:
            if not required_header in headers:
                raise forms.ValidationError(_("File missing header: {0}".format(required_header)))

        return data


class UploadForm(forms.Form):
    history = CSVHistoryField()
