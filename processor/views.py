import csv

from django.http import HttpResponse

from processor import models


def upload_history(request):
    """
    Accept a user's csv file of bank history and save Transaction objects from
    the rows.
    """
    if request.method == 'POST':
        if 'history' in request.FILES:
            reader = csv.reader(request.FILES['history'])
            try:
                header = reader.next()
            except StopIteration:
                return HttpResponse("File empty. Please upload a CSV file with contents")

            required_headers = ['DATE', 'AMOUNT', 'DESC']
            for required_header in required_headers:
                if not required_header in header:
                    return HttpResponse("File not in the correct format")

            for row in reader:
                processed_row = dict(zip(header, row))
                models.Transaction.objects.create(
                    posted=processed_row['DATE'],
                    amount=processed_row['AMOUNT'],
                    description=processed_row['DESC']
                )
        else:
            return HttpResponse("Please upload a file")
    return HttpResponse("OK")
