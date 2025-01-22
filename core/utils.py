ICON_CHOICES = [
        ('fa-facebook', 'Facebook'),
        ('fa-twitter', 'Twitter'),
        ('fa-instagram', 'Instagram'),
        ('fa-linkedin', 'LinkedIn'),
        ('fa-github', 'GitHub'),
    ]  

RATES = [
        (5, '5 - Excelent'),
        (4, '4 - Good as excepted'),
        (3, '3 - Ok'),
        (2, '2 - Could be better'),
        (1, '1 - Below expectations '),
]

CATEGORIES = [
    ('sport', 'Sport'),
    ('business', 'Business'),
    ('technology', 'Technology'),
    ('health', 'Health'),
    ('entertainment', 'Entertainment'),
]

VIEWS = [
    ('about', 'about'),
    ('services', 'services'),
    ('works', 'works')
]


from django.core.paginator import Paginator


def get_paginator_data(request, query_set, obj_per_page, max_page_links=3):
    
    # Create pagination - pass query set and obj per page
    paginator = Paginator(query_set, obj_per_page)

    # Get page num from GET param. and set 1 as a default
    page_number = int(request.GET.get('page', 1))

    # page_obj is class Page's object returned by method get_page(), contains objects assigned to the page
    page_obj = paginator.get_page(page_number)
    
    # Declare range of start & end displayed nums
    # Max_page_links means amount of buttons to navigate [2][3][4] | [98][99][100]
    start_page = max(page_number - max_page_links // 2, 1)
    end_page = min(start_page + max_page_links - 1, paginator.num_pages)

    paginator_data = {
        'page_obj': page_obj,
        'page_range': range(start_page, end_page + 1),
        'has_prev':  page_obj.has_previous,
        'has_next': page_obj.has_next,
        'prev': page_obj.previous_page_number,
        'next': page_obj.next_page_number,
        'first': 1,
        'last': page_obj.paginator.num_pages,
    }
    
    return paginator_data