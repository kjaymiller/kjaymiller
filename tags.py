
def add_to_tag(content, tags):
    tags = categories

    for tag in tags:

        if content.tag not in tags.items():
           tags[content.tag].append(content) 

        else:
           tags[content.tag] = [content]

    return tags
        

def add_to_tags(pages, categories):

    for p in pages:
        tags = add_to_categories(p, categories)
        
    return tags
