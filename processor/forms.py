from django import forms
from django.utils.translation import ugettext_lazy as _

from uploads import MissingHeaderError
from uploads import TransactionProcessor


class CSVHistoryField(forms.FileField):
    REQUIRED_HEADERS = ['DATE', 'AMOUNT', 'DESC']

    def to_python(self, value):
        value = super(CSVHistoryField, self).to_python(value)
        transaction_processor = TransactionProcessor()
        try:
            return transaction_processor.process(value)
        except MissingHeaderError as e:
            raise forms.ValidationError(_(e.message))


class UploadForm(forms.Form):
    history = CSVHistoryField()
