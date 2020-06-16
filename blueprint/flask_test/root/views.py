from . import root

@root.route('/index')
def index():
    return 'this is root index'
