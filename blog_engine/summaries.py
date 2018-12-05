def latest_blog(latest_post)
    if 'summary' not in latest_post:
        start_index = 120
        while latest_post['content'][start_index] not in string.punctuation:
            start_index += 1
            latest_post['summary'] = latest_post['content'][:start_index + 1] + '...'
