from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginate(objects_list, request, per_page=10):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # Если page не число, показываем первую страницу
        page_obj = paginator.page(1)
    except EmptyPage:
        # Если страница пустая (например, 999), показываем последнюю
        page_obj = paginator.page(paginator.num_pages)
    return page_obj