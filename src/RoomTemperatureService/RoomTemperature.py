import board
import adafruit_dht


class RoomTemperature:
    dhtDevice = adafruit_dht.DHT22(board.D6, use_pulseio=False)
    # Default room temp
    room_temperature = 22

    def poll_room_temperature(self):

        try:
            self.room_temperature = self.dhtDevice.temperature
        except RuntimeError:
            # Errors happen fairly often, DHT's are hard to read, just keep goi$        print(error.args[0])
            pass
        except Exception as error:
            raise error

    def get_room_temperature(self):
        return self.room_temperature
