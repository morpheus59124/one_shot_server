#!/bin/sh
gunicorn --bind 127.0.0.1:5000 app:app