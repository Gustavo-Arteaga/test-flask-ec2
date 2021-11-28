from flask import Blueprint, render_template, request, flash, redirect, url_for, Flask,jsonify,redirect, make_response
import os
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

@app.route("/urlunprocessed",  methods = ['POST'])

def dateJS():
    if request.get_json():

        req = request.get_json()

        print("****"*10)

        img_n = req["url_img_unprocessed"]
        print("url_img_unprocessed:")
        print(img_n)

        
        response = [
          {
          "url_img_processed": "https://bucket-power-dragon-test.s3.us-east-2.amazonaws.com/processed/ATT46_Photo9.jpg"
          },
          {
            "HP": "5",
            "HZ": "60",
            "Voltage": "208-230/460",
            "amperage": "BEARINGS",
            "efficiency": "89.5",
            "phases": "3",
            "powerfactor": "78",
            "rpm": "1750",
            "servicefactor": "none"
          },
          {
            "CAT": "none",
            "DATE": "none",
            "Weight": "none",
            "duty": "none",
            "enclousure": "TEFC",
            "frame": "none",
            "insulationclass": "NEMA",
            "manufacturer": "ELECTRIC",
            "modelnumber": "none",
            "serialnumber": "F1408011375",
            "temperature": "40C"
          }
        ]


        res = make_response(jsonify(response), 200)
        
        return res

    else:
        return "No JSON received", 400


@app.route("/foo")
def index():
    return 'test json send'

if __name__ == '__main__':

  # app.run()
  app.run("0.0.0.0", debug=False)