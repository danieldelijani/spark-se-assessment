from project.server import app

if __name__ == '__main__':
    create_app = app
    create_app.run()
else:
    gunicorn_app = app
