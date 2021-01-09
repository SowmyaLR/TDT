from flask import Flask, make_response
import logging

from src.service import TDT

__author__ = "SowmyaLR"

app = Flask(__name__)


@app.route('/sync')
def sync_data():
    logging.info("Data sync started")
    obj = TDT()
    obj.load_json()
    logging.info("Data sync completed")
    return make_response("Data sync completed")


app.run(debug=True)
