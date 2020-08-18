####Table of contents
#Templates
Templates are a way to generate dynamic html code.

This means adding variables, for loops and if statements inside the HTML code.
The template is written in a template language that combines python and HTML.
There are a lot of python modules that can convert template to html code (they’re called template engines), flask use jinja2.

Templates can be written in any extension.

#What is in the template ?
###Delimiters
There are three types of enclosures in jinja2:

Variables: `{{ ... }}` is used to define expressions, it will just be replaced by their python value.

Statements: `{% ... %}` is used to define statements (it means if or loops).

Comments: `{# #}` is used for comments (means it won’t be included in the template output).
###Variables
Variables (enclosed in `{{ ... }}` sections) are placeholders for dynamic content.

These placeholders represent the parts of the page that are variable and will only be known at runtime.

They will be replaced by their value when the template will be rendered by jinja2.