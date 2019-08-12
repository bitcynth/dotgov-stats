from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from dgs import routes, list_mgr

list_mgr.load_list(app.config['FULL_LIST_CSV_URL'])