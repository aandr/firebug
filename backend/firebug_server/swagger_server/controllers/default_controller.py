import connexion
import six
import pandas as pd

from swagger_server.models.device import Device  # noqa: E501
from swagger_server.models.concentration_series import ConcentrationSeries  # noqa: F401,E501
from swagger_server.models.geo_location import GeoLocation  # noqa: F401,E501
from swagger_server.models.time_series import TimeSeries  # noqa: F401,E501
from swagger_server import util

SENSOR_1_ID = "200040001047373333353132"
SENSOR_2_ID = "35005c000d51363034323832"
SENSOR_3_ID = "2d0049000d51363034323832"

sensor_id = {'1': SENSOR_1_ID, '2': SENSOR_2_ID, '3': SENSOR_3_ID}

def get_data(device_number):  # noqa: E501
    """Get an object of sensor data

    Returns a Device object # noqa: E501

    :param device_number: the device_number of the device you want to get data for
    :type device_number: str

    :rtype: Device
    """

    # extract data
    df = pd.read_csv("http://fbug-store.herokuapp.com/csv")
    time = df[df.device == sensor_id[device_number]].timestamp.values.tolist()
    concentrations = df[df.device == sensor_id[device_number]].concentration.values.tolist()

    # build response objects
    geolocation = GeoLocation(37.3863, 'N', 122.0669, 'W')
    time_series = TimeSeries(time)
    concentration_series = ConcentrationSeries(concentrations)

    return Device(device_number, geolocation, time_series, concentration_series)
