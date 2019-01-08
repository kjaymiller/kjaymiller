import config

def write_page(filename, content):
    with open(f'{config.OUTPUT_PATH}/{filename}.html', 'w') as f:
        f.write(content)
        return f

