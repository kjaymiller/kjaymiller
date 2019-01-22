def writer(route):
    def wrapper(*args, **kwargs):
        page = func(*args, **kwargs)
    return write_page(route, page)
