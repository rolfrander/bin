import os, html

def make_index(path):
    files = sorted(os.listdir(path))
    items = []
    for f in files:
        full = os.path.join(path, f)
        display = html.escape(f)
        if os.path.isdir(full):
            items.append(f'<li><a href="{f}/">{display}/</a></li>')
            make_index(full)  # recurse
        else:
            items.append(f'<li><a href="{f}">{display}</a></li>')

    html_content = f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>Index of {html.escape(path)}</title></head>
<body><h1>Index of {html.escape(path)}</h1><ul>{''.join(items)}</ul></body></html>"""
    with open(os.path.join(path, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_content)

make_index(".")
