import csv


class MissingHeaderError(Exception):
    pass


class TransactionProcessor(object):
    REQUIRED_HEADERS = ['DATE', 'AMOUNT', 'DESC']

    def process(self, csvfile):
        reader = csv.reader(csvfile)
        headers = reader.next()
        for required_header in TransactionProcessor.REQUIRED_HEADERS:
            if not required_header in headers:
                raise MissingHeaderError("File missing header: {0}".format(required_header))

        return [dict(zip(headers, row)) for row in reader]
