import csv

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
            reader = csv.reader(form.cleaned_data['history'])
            header = reader.next()

            for row in reader:
                processed_row = dict(zip(header, row))
                models.Transaction.objects.create(
                    posted=processed_row['DATE'],
                    amount=processed_row['AMOUNT'],
                    description=processed_row['DESC']
                )
        else:
            return HttpResponse(form.errors)
    return HttpResponse("OK")
