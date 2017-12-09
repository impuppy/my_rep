from jinja import Environment, FileSystemLoader
from webob import Request, Response

assets = [
    'app.js',
    'react.js',
    'leaflet.js',
    'D3.js',
    'moment.js',
    'math.js',
    'main.css',
    'bootstrap.css',
    'normalize.css',
    ]

styles = []
scripts = []

for str in assets
    b = str.split('.')
    if b[1] == "js":
        scripts.append(str)
    else:
        styles.append(str)


class WsgiTopBottomMiddleware(object):
    def _init_(self, app):
        self.app = app
    
     def __call__(self, environ, start_response):
        response = self.app(environ, start_response).decode() 
        if response.find('<body>') > -1:
            header, body = response.split('<body>')
            data, htmlend = body.split('</body>')
            data = '<body>' + data + '</body>'

            yield (header + data + htmlend).encode()  
        else:
            yield (response).encode()  
        def app(environ, start_response):
    
    response_code = '200 OK'
    response_type = ('Content-Type', 'text/HTML')
    start_response(response_code, [response_type])
    return ''''''

app = WsgiTopBottomMiddleware(app)

request = Request.blank('/index.html')

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('index.html')
print(template.render(js=scripts, css=styles))

print(request.get_response(app))
