from itertools import zip_longest
from render_enging __init__ import env
from writer import write_page

def paginate(iterable, items_per_page, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * items_per_page
    return zip_longest(*args, fillvalue=fillvalue) 

def write_paginated_pages(pagination, template, output_path, **kwargs)
    env =  env.get_template(template)
    for block in enumerate(pagination):
        render = temp.render(block=block[1], **kwargs)
        write_page(output_path, f'_block[0], render)
