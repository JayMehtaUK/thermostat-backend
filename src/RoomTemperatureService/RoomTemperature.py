import board
import adafruit_dht


class RoomTemperature:
    dhtDevice = adafruit_dht.DHT22(board.D6, use_pulseio=False)
    # Default room temp
    room_temperature = 22
    room_humidity = 0

    def poll_room_temperature(self):

        try:
            self.room_temperature = self.dhtDevice.temperature
            self.room_humidity = self.dhtDevice.humidity
        except RuntimeError:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            pass
        except Exception as error:
            raise error

