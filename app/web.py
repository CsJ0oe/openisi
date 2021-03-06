from bottle import Bottle, static_file, redirect
from .config import repo_dir

web_app = Bottle()
	
@web_app.route('/', method='GET')
def redirect_web():
	return redirect('/web/')

@web_app.route('/web/', method='GET')
@web_app.route('/web/<filepath:path>', method='GET')
def site_web(filepath = 'index.html'):
    return static_file(filepath, root=repo_dir+'/web')
