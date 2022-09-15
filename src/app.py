from flask import Flask, request, jsonify
from thermostat_controller import ThermostatController


app = Flask(__name__)
thermostat_controller = ThermostatController()


@app.route('/target-temperature', methods=['POST'])
def target_temperature():
    data = request.form
    print(data.get("target-temperature"))
    thermostat_controller.set_target_temperature(int(data.get("target-temperature")))
    return jsonify(success=True)






if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
