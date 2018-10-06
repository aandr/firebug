import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("http://fbug-store.herokuapp.com/csv")

SENSOR_1_ID = "200040001047373333353132"
SENSOR_2_ID = "35005c000d51363034323832"
SENSOR_3_ID = "2d0049000d51363034323832"

WINDOW = 40

df.timestamp = pd.to_datetime(df.timestamp)

sensor_1_time = df[df.device == SENSOR_1_ID].timestamp.values
sensor_2_time = df[df.device == SENSOR_2_ID].timestamp.values
sensor_3_time = df[df.device == SENSOR_3_ID].timestamp.values

sensor_1_concentration = df[df.device == SENSOR_1_ID].concentration.rolling(window=WINDOW).mean().values
sensor_2_concentration = df[df.device == SENSOR_2_ID].concentration.rolling(window=WINDOW).mean().values
sensor_3_concentration = df[df.device == SENSOR_3_ID].concentration.rolling(window=WINDOW).mean().values



plt.plot(sensor_1_time, sensor_1_concentration, label="Sensor1")
plt.plot(sensor_2_time, sensor_2_concentration, label="Sensor2")
plt.plot(sensor_3_time, sensor_3_concentration, label="Sensor3")
plt.legend()
plt.show()


'''
‘200040001047373333353132’: ‘Sensor 1’,
‘35005c000d51363034323832’: ‘Sensor 2’,
‘2d0049000d51363034323832’: ‘Sensor 3’
'''
