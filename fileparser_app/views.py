from django.shortcuts import render

from fileparser_app.models import File
from fileparser_app.forms import FileUploadForm

import pandas as pd
import json

def file_parser(file):
    file_vars = ['purchaser_name', 'item_description', 'item_price', 'purchase_count', 'merchant_address', 'merchant_name']
    file_content = pd.read_csv(file, sep='\t', skiprows = 1, names=file_vars)
    file_content_json = json.loads(file_content.to_json(orient='records'))

    grossreceipts = 0
    for line in file_content_json:
        grossreceipts = grossreceipts + line['item_price']

    return grossreceipts, file_content_json

def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)

        grossreceipts, file_content_json = file_parser(request.FILES['file'])

        if form.is_valid():
            file_register = File(file = request.FILES['file'], content=file_content_json)
            file_register.save()

            return render(request, 'grossreceipts/index.html', {'grossreceipts': grossreceipts, 'form': form})
    else:
        form = FileUploadForm()

    return render(request, 'grossreceipts/index.html', {'grossreceipts': 0, 'form': form})
