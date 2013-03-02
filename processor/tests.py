from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.urlresolvers import reverse
from django.test import TestCase

from processor.models import Transaction


class ProcessorTestCase(TestCase):

    def test_that_a_new_transaction_is_created_for_each_history_entry(self):
        self.assertEquals(0, Transaction.objects.count())

        f = SimpleUploadedFile('history.csv', 'ID,DATE,AMOUNT,DESC\n1,2012-12-12,-19.95,"Amazon"\n2,2012-12-13,-7.50,"Papa Ginos"\n3,2012-12-15,100,"Paychex"')
        response = self.client.post(reverse('processor'), {'history': f})

        self.assertEquals(200, response.status_code)
        transactions = Transaction.objects.all()
        self.assertEquals("Amazon", transactions[0].description)
        self.assertEquals("Papa Ginos", transactions[1].description)
        self.assertEquals("Paychex", transactions[2].description)

    def test_that_uploading_a_blank_file_gets_ignored(self):
        f = SimpleUploadedFile('history.csv', '')

        response = self.client.post(reverse('processor'), {'history': f})
        self.assertEquals(200, response.status_code)
        self.assertEquals(0, Transaction.objects.count())

        f.close()

    def test_that_files_with_a_bad_format_are_rejected(self):
        f = SimpleUploadedFile('history.csv', 'ID,DATE\n1,2012-12-12\n2,2012-12-13')

        response = self.client.post(reverse('processor'), {'history': f})
        self.assertEquals(200, response.status_code)
        self.assertEquals(0, Transaction.objects.count())

    def test_that_no_file_uploaded_does_nothing(self):
        response = self.client.post(reverse('processor'))
        self.assertEquals(200, response.status_code)
        self.assertEquals(0, Transaction.objects.count())
