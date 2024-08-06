from django.shortcuts import render


def main_page_view(request):
    return render(request, 'todo_list_app/main_page.html')
