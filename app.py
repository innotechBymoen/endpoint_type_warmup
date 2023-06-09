from flask import Flask, request
import json
import dbhelpers

app = Flask(__name__)

def check_endpoint_info(sent_data, expected_data):
    for data  in expected_data:
        if(sent_data.get(data) == None):
            return f"The {data} must be sent!"

@app.post("/api/restaurant")
def create_restaurant():
    error = check_endpoint_info(request.json, ["name", "address", "phone_num", "image_url"])
    if(error != None):
        return error

    results = dbhelpers.run_procedure("call create_restaurant(?,?,?,?)", 
                                      [request.json.get("name"), request.json.get("address"), request.json.get("phone_num"), request.json.get("image_url")])
    return json.dumps(results, default=str)

app.run(debug=True)