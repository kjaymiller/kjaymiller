
def add_to_category(content, categories):
    categories = categories

    for category in categories:

        if content.category not in categories.items():
           categories[content.category].append(content) 

        else:
           categories[content.category] = [content]

    return categories
        

def add_to_categories(pages, categories):

    for p in pages:
        categories = add_to_categories(p, categories)
        
    return categories
