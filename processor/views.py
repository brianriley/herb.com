from django.http import HttpResponse

from processor import forms
from processor import models


def upload_history(request):
    """
    Accept a user's csv file of bank history and save Transaction objects from
    the rows.
    """
    if request.method == 'POST':
        form = forms.UploadForm(request.POST, request.FILES)
        if form.is_valid():
            for entry in form.cleaned_data['history']:
                models.Transaction.objects.create(
                    posted=entry['DATE'],
                    amount=entry['AMOUNT'],
                    description=entry['DESC']
                )
        else:
            return HttpResponse(form.errors)
    return HttpResponse("OK")
