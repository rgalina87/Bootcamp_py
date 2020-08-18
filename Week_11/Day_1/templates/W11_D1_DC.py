from flask import Flask, render_template
import markdown
import markdown.extensions.fenced_code

web = Flask("Webpage")

@web.route('/lesson')
def lesson():
    file1 = open("in_this_chapter.md", "r")
    string1 = markdown.markdown(file1.read(), extensions=["fenced_code"])
    return string1

@web.route('/ex')
def ex():
    file2 = open("exercises.md", "r")
    string2 = markdown.markdown(file2.read(), extensions=["fenced_code"])
    return string2

web.run(debug=True)