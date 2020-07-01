title: SubCollections now available in Render Engine
date: 01 Jul 2020 14:43
category: Render Engine
tags: update

**Version Update: 2020.07.02**
I'm happy to announce that subcollections are now supported in render_engine

<iframe
  src="https://carbon.now.sh/embed?bg=rgba(171%2C%20184%2C%20195%2C%201)&t=monokai&wt=none&l=python&ds=true&dsyoff=20px&dsblur=68px&wc=true&wa=true&pv=56px&ph=56px&ln=false&fl=1&fm=Hack&fs=14px&lh=133%25&si=false&es=2x&wm=false&code=%2540mysite.register_collection%250A%250Aclass%2520Blog(Blog)%253A%250A%2520%2520%2520%2520routes%2520%253D%2520%255B''%252C%2520'%252Fblog'%255D%250A%2520%2520%2520%2520template%2520%253D%2520'blog.html'%250A%2520%2520%2520%2520archive_template%2520%253D%2520'archive.html'%250A%2520%2520%2520%2520archive_slug%2520%253D%2520'all_posts.html'%250A%2520%2520%2520%2520content_path%2520%253D%2520'content'%250A%2520%2520%2520%2520subcollections%2520%253D%2520%255B'category'%252C%2520'tags'%255D%250A"
  style="width: 496px; height: 366px; border:0; transform: scale(1); overflow:hidden;"
  sandbox="allow-scripts allow-same-origin">
</iframe>

**SubCollections** create a new collection from pages that has the specified value. SubCollections are of the same type as their parent so if you are using a `Blog` object , you will get access to feeds natively for each SubCollection.

### Other Minor Updates Include

- access to all collections and subcollections throughout the entire site template - e.g. `{% for page in collections['blog'].pages %}` or `{{subcollections['category']}}`
