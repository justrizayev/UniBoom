from collections import OrderedDict

from base.sqlpaginator import SqlPaginator
from app_uniboom.models import Product
from uniboom.settings import PER_PAGE


def format_pro(data):
    
    l = [
        ("id", data.id),
        ('rasm', data.img.url),
        ('name', data.name),
        ('description', data.description),
        ('skidka', data.skidka),
        ('price', data.price),
        ('info', data.info),
        ("rasrochka", data.rasrochka),
    ]
    try:
        l.append(("ctg_id", data.ctg.name))
    except:
        pass
    return OrderedDict(l)


def paginated_pro(requests):
    page = int(requests.GET.get('page', 1))
    ctg = Product.objects.all().order_by('-pk')

    limit = PER_PAGE
    offset = (page - 1) * limit

    result = []
    for x in range(offset, offset + limit):
        result.append(format_pro(ctg[x]))

    pag = SqlPaginator(requests, page=page, per_page=PER_PAGE, count=len(ctg))
    meta = pag.get_paginated_response()

    return OrderedDict([
        ('result', result),
        ('meta', meta)
    ])
