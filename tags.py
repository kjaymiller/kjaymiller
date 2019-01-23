def add_to_tag(tags, tag_list):
    for tag in tags:
        if content.tag not in tags.items():
           tag_list[content.tag].append(content) 

        else:
           tags[content.tag] = [content]

    return tags
