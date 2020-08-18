# Exercise 1


# Exercise 2
import flask
print(dir(flask))

#Exercise 3

cv = flask.Flask("CV")

@cv.route("/name")
def name():
    return "my name is"



