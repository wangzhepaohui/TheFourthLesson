from . import user

@user.route('/index')
def index():
    return 'this is user index'
