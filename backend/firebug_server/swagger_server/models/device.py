# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.anomaly_score_series import AnomalyScoreSeries  # noqa: F401,E501
from swagger_server.models.concentration_series import ConcentrationSeries  # noqa: F401,E501
from swagger_server.models.geo_location import GeoLocation  # noqa: F401,E501
from swagger_server.models.time_series import TimeSeries  # noqa: F401,E501
from swagger_server import util


class Device(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, device_number: int=None, geolocation: GeoLocation=None, time_series: TimeSeries=None, concentration_series: ConcentrationSeries=None, anomaly_score_series: AnomalyScoreSeries=None):  # noqa: E501
        """Device - a model defined in Swagger

        :param device_number: The device_number of this Device.  # noqa: E501
        :type device_number: int
        :param geolocation: The geolocation of this Device.  # noqa: E501
        :type geolocation: GeoLocation
        :param time_series: The time_series of this Device.  # noqa: E501
        :type time_series: TimeSeries
        :param concentration_series: The concentration_series of this Device.  # noqa: E501
        :type concentration_series: ConcentrationSeries
        :param anomaly_score_series: The anomaly_score_series of this Device.  # noqa: E501
        :type anomaly_score_series: AnomalyScoreSeries
        """
        self.swagger_types = {
            'device_number': int,
            'geolocation': GeoLocation,
            'time_series': TimeSeries,
            'concentration_series': ConcentrationSeries,
            'anomaly_score_series': AnomalyScoreSeries
        }

        self.attribute_map = {
            'device_number': 'device_number',
            'geolocation': 'geolocation',
            'time_series': 'time_series',
            'concentration_series': 'concentration_series',
            'anomaly_score_series': 'anomaly_score_series'
        }

        self._device_number = device_number
        self._geolocation = geolocation
        self._time_series = time_series
        self._concentration_series = concentration_series
        self._anomaly_score_series = anomaly_score_series

    @classmethod
    def from_dict(cls, dikt) -> 'Device':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Device of this Device.  # noqa: E501
        :rtype: Device
        """
        return util.deserialize_model(dikt, cls)

    @property
    def device_number(self) -> int:
        """Gets the device_number of this Device.

        device number 1, 2, or 3  # noqa: E501

        :return: The device_number of this Device.
        :rtype: int
        """
        return self._device_number

    @device_number.setter
    def device_number(self, device_number: int):
        """Sets the device_number of this Device.

        device number 1, 2, or 3  # noqa: E501

        :param device_number: The device_number of this Device.
        :type device_number: int
        """
        if device_number is None:
            raise ValueError("Invalid value for `device_number`, must not be `None`")  # noqa: E501

        self._device_number = device_number

    @property
    def geolocation(self) -> GeoLocation:
        """Gets the geolocation of this Device.


        :return: The geolocation of this Device.
        :rtype: GeoLocation
        """
        return self._geolocation

    @geolocation.setter
    def geolocation(self, geolocation: GeoLocation):
        """Sets the geolocation of this Device.


        :param geolocation: The geolocation of this Device.
        :type geolocation: GeoLocation
        """
        if geolocation is None:
            raise ValueError("Invalid value for `geolocation`, must not be `None`")  # noqa: E501

        self._geolocation = geolocation

    @property
    def time_series(self) -> TimeSeries:
        """Gets the time_series of this Device.


        :return: The time_series of this Device.
        :rtype: TimeSeries
        """
        return self._time_series

    @time_series.setter
    def time_series(self, time_series: TimeSeries):
        """Sets the time_series of this Device.


        :param time_series: The time_series of this Device.
        :type time_series: TimeSeries
        """
        if time_series is None:
            raise ValueError("Invalid value for `time_series`, must not be `None`")  # noqa: E501

        self._time_series = time_series

    @property
    def concentration_series(self) -> ConcentrationSeries:
        """Gets the concentration_series of this Device.


        :return: The concentration_series of this Device.
        :rtype: ConcentrationSeries
        """
        return self._concentration_series

    @concentration_series.setter
    def concentration_series(self, concentration_series: ConcentrationSeries):
        """Sets the concentration_series of this Device.


        :param concentration_series: The concentration_series of this Device.
        :type concentration_series: ConcentrationSeries
        """
        if concentration_series is None:
            raise ValueError("Invalid value for `concentration_series`, must not be `None`")  # noqa: E501

        self._concentration_series = concentration_series

    @property
    def anomaly_score_series(self) -> AnomalyScoreSeries:
        """Gets the anomaly_score_series of this Device.


        :return: The anomaly_score_series of this Device.
        :rtype: AnomalyScoreSeries
        """
        return self._anomaly_score_series

    @anomaly_score_series.setter
    def anomaly_score_series(self, anomaly_score_series: AnomalyScoreSeries):
        """Sets the anomaly_score_series of this Device.


        :param anomaly_score_series: The anomaly_score_series of this Device.
        :type anomaly_score_series: AnomalyScoreSeries
        """
        if anomaly_score_series is None:
            raise ValueError("Invalid value for `anomaly_score_series`, must not be `None`")  # noqa: E501

        self._anomaly_score_series = anomaly_score_series
