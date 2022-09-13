#!/bin/bash

python project/server/__init__.py db init
python project/server/__init__.py db migrate -m "Initial migration."
python project/server/__init__.py db upgrade