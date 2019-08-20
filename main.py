import webapp2
import jinja2
import os

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        result_template = jinja_env.get_template('/Templates/index.html')
        self.response.write(result_template.render())


app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
], debug=True)
