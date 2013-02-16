import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

ADMINS = frozenset(['vunhatminh@icloud.com'])
SECRET_KEY = 'SecretKeyForSessionSigning'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED=True
CSRF_SESSION_KEY="somethingimpossibletoguess"

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LfpFt0SAAAAAC__c_N8i4q-KWCTNFLSNn51aVif'

RECAPTCHA_PRIVATE_KEY = '6LfpFt0SAAAAAKk6kfFBprfcGmOBDt5rWke2bGNy'
RECAPTCHA_OPTIONS = {'theme': 'white'}

