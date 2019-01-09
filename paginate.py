from itertools import zip_longest
from render_engine import env
from writer import write_page
import config

def paginate(iterable, items_per_page, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * items_per_page
    return zip_longest(*args, fillvalue=fillvalue) 

def write_paginated_pages(name, pagination, template, **kwargs):
    temp =  env.get_template(template)
    for block in enumerate(pagination):
        render = temp.render(block=block[1], config=config, **kwargs)
        write_page(f'{name}_{block[0]}', render)
