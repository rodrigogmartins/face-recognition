#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from app import app
from flask import redirect, Blueprint
from app.controllers.home_bp import home_bp

app.register_blueprint(home_bp)

@app.route('/')
def index():
    return redirect(home_bp.url_prefix)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run('0.0.0.0', port=port)


