from flask import Flask
from flask import render_template
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader(__name__, 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)
app = Flask(__name__)

@app.route('/')
def main():
	template = env.get_template('app.html')
	return template.render()

if __name__ == '__main__':
	app.run(host='0.0.0.0')
