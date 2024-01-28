from django.shortcuts import render
from django.http import HttpResponse
import logging
import datetime

logger = logging.getLogger(__name__)


def index(request):
    logger.info(f"Index page accessed {datetime.datetime.now()}")
    return HttpResponse('<h1>Hello world</h1>')


def about(request):
    logger.info(f"About page accessed {datetime.datetime.now()}")
    return HttpResponse('<h1>About me</h1>')



