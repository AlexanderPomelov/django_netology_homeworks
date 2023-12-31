from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from django_second_task.pagination.pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    with open(settings.BUS_STATION_CSV, encoding='utf-8', newline='') as file:
        result = csv.DictReader(file)

        result_list = []
        for row in result:
           result_list.append(row)

        paginator = Paginator(result_list, 10)
        page_number = int(request.GET.get('page', 1))
        page = paginator.get_page(page_number)

        context = {
            'bus_stations': page.object_list,
            'page': page,
        }
    return render(request, 'stations/index.html', context)
