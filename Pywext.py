def HTML(content, HTML_File):
    print(f"<!DOCTYPE html>\n<html>\n{content}\n</html>", file=open(HTML_File,'w'))

def Head(content):
    return f"<head>\n{content}\n</head>\n"

def Body(attributes, content):
    return f"<body {attributes}>\n{content}\n</body>\n"
    
def Tag(tag, attributes, content, self_closing):
    if self_closing:
        return f"<{tag} {attributes}>"
    else:
        return f"<{tag} {attributes}>{content}</{tag}>"
