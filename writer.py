def write_page(filename, content):
    with open(f'{filename}.html', 'w') as f:
        f.write(content)
        return f

