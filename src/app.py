from flask import Flask, request, render_template, redirect
from apscheduler.schedulers.background import BackgroundScheduler
from TargetTemperatureService.TargetTemperature import TargetTemperature
from RoomTemperatureService.RoomTemperature import RoomTemperature

app = Flask(__name__)
room_temperature_service = RoomTemperature()
target_temperature_service = TargetTemperature(room_temperature_service)


scheduler = BackgroundScheduler(daemon=True)
# Likely need to increase the interval to a minute depending on design
scheduler.add_job(target_temperature_service.reach_target_temperature, 'interval', seconds=300)
scheduler.add_job(room_temperature_service.poll_room_temperature, 'interval', seconds=2)
scheduler.start()

@app.route('/', methods=['GET'])
def index():
    if target_temperature_service.is_heating_on:
        heating_status = "🔥"
    else:
        heating_status = "❄"

    return render_template('index.html',
                           heating_status=heating_status,
                           room_temperature=room_temperature_service.get_room_temperature(),
                           target_temperature=target_temperature_service.target_temperature)

@app.route('/', methods=['POST'])
def target_temperature():
    data = request.form
    print(data.get("target-temperature"))
    target_temperature_service.target_temperature = float(data.get("target-temperature"))
    target_temperature_service.reach_target_temperature()

    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
