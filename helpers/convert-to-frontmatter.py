import frontmatter
import pathlib

for path in pathlib.Path('content/microblog').iterdir():
    if not path.suffix == '.md':
        continue

    print(path.name)
    content = path.read_text()
    post = frontmatter.loads(content)

    if not post.metadata:
        sections = content.split('\n\n', 1)
        sections[0] = f'---\n{sections[0]}\n---'
        path.write_text('\n\n'.join(sections))
