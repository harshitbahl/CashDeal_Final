# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 22:44:44 2014

@author: harshitbahl
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))

MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
COLLECTION_QA = 'cashBackPlatform'

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass