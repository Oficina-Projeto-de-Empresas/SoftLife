def init_app(app):
    app.config['SECRET_KEY'] = 'super_secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SoftLife.db'

    if app.debug:
        app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
        app.config['DEBUG_TB_PROFILER_ENABLED'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
