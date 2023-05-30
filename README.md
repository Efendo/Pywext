![Pywext](9AAB9E90-14FC-4C16-A26B-2E2A690C6996.jpeg)

# What is Pywext?
pywext is a python library that can compile to html.

# Functions

## HTML(content, HTML_File)
HTML is the function where youll be writing you code.
it takes in 2 arguments: Content, HTML_File

## Head(Content)
this creates the head element with the entered content inside

## Body(Attributes, Content)
this generates the body element, its like the head but you also need to specify attributes

## Tag(tag, attributes, content, self_closing)
this creates a Tag. !!! Please set self_closing to True only on self closing tags !!!
