from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
import csv
import re

file_path = settings.BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(file_path, encoding='utf8', newline='') as csv_file:
        busreader = csv.reader(csv_file)
        rows = []
        for row in busreader:
            col1, col2, col3 = row[1], row[4], row[6]
            col1 = re.sub('\(\d+\)', '', col1)
            rows.append({
                'Name': col1,
                'Street': col2,
                'District': col3,
            })
        rows.pop(0)
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(rows, 10)
    page = paginator.get_page(page_number)
    context = {
        'page': page
    }

    return render(request, 'stations/index.html', context)
