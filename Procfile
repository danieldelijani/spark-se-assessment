web: gunicorn appserver:gunicorn_app
heroku ps:scale web=1
release: sh initialize_db.sh


