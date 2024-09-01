from django.core.cache import cache


def todo_list_cache_key(request):
    cache_key = f"_{request.user.id}"
    return cache_key


def invalid_todo_list_cache(user_id):
    cache_key = f"todo_list_view_{user_id}"
    cache.delete(cache_key)
