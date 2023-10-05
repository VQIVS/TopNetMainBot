from django.shortcuts import render
from .models import Link
from .models import Link


def link_input(request):
    return render(request, 'index.html')


def links_template_view(request):
    # Initialize dictionaries to store links for each link_id
    links_by_link_id = {str(i): [] for i in range(1, 7)}

    # Retrieve links with status=True and organize them by link_id
    links = Link.objects.filter(status=True, link_id__range=(1, 6))
    for link in links:
        link_id_str = str(link.link_id)
        links_by_link_id[link_id_str].append(link)

    context = {
        'links_by_link_id_1': links_by_link_id['1'],
        'links_by_link_id_2': links_by_link_id['2'],
        'links_by_link_id_3': links_by_link_id['3'],
        'links_by_link_id_4': links_by_link_id['4'],
        'links_by_link_id_5': links_by_link_id['5'],
        'links_by_link_id_6': links_by_link_id['6'],
    }

    return render(request, 'links_template.html', context)
