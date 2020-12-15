# WMR200

This is a driver for the Oregon Scientific WMR200 weather station for the WeeWX weather system. It was originally part
of the main WeeWX distribution, but was split off in December 2020 because of continuing support problems. In
particular, it is known to get occasional "Resource busy" errors. See WeeWX
issue [#578](https://github.com/weewx/weewx/issues/578).

**The driver is unsupported**

WeeWX V4 and Python 3.x compatible.

## Options

This section is for options relating to the Oregon Scientific WMR200 series of weather stations with USB connectors.

### [WMR200]

**model**

Set to the station model. For example, `WMR200` or `WMR200A`.

**use_pc_time**

If `True`, use the computer time, otherwise use the station time. Default is `True`.

**archive_interval**

Set the wmr200 archive interval in seconds. Default is 60 seconds.

The wmr200 hardware records archive data at an immutable rate of 60 seconds. This field may be set to a higher value
enabling the WeeWX engine to coalesce live data packets. However, when the wmr200 is not connected to a system via USB
or if the WeeWX software is not running, the wmr200 console will continue to store weather data in onboard console
memory at a fixed rate of 60 seconds.

**erase_archive**

If `True`, erase onboard console memory archive when starting up. Default is `False`.

**archive_startup**

When retrieving archive data packets from the wmr200 onboard console memory, there is no explicit indication that all
the data has been drained. This field specifies when to transition from archive mode to live mode. This transition
occurs when no archive packets are detected within this time interval. Default is 120 seconds.

**archive_threshold**

Occasionally when retrieving archive packets from the wmr200 onboard memory a stale data packet will be detected. The
archive packets are presented in sequential order typically timestamped 60 seconds apart. However, there is no guarantee
the archive packets are exactly 60 seconds apart. Should an incoming archive data packet timestamp exceed the previous
archive data packet one by the amount in this field it will be dropped. Default is 1512000 seconds (1 week).

**sensor_status**

If `True`, emit sensor faults and failures to log. Default is `True`.

**[[sensor_map]]**

This section defines the mapping between observations from remote sensors and the fields in the database.

For example, this would associate extraTemp1 with the remote T/H sensor on channel 5:

```ini
[[sensor_map]]
extraTemp1 = temperature_5
```

See below for a complete listing of sensor names, and the default database fields for each sensor.

## WMR200 station data

The following table shows which data are provided by the station hardware and which are calculated by WeeWX.

| Database Field       | Observation         | Loop | Archive |
|----------------------|---------------------|------|---------|
| barometer            |                     | S    | S       |
| pressure             | pressure            | H    | H       |
| altimeter            | altimeter           | H    | H       |
| inTemp               | temperature_0       | H    | H       |
| outTemp              | temperature_1       | H    | H       |
| inHumidity           | humidity_0          | H    | H       |
| outHumidity          | humidity_1          | H    | H       |
| windSpeed            | wind_speed          | H    | H       |
| windDir              | wind_dir            | H    | H       |
| windGust             | wind_gust           | H    | H       |
| rain                 | rain                | D    | D       |
| rain_total           | H                   | H    |         |
| rainRate             | rain_rate           | H    | H       |
| dewpoint             | S                   | S    |         |
| windchill            | windchill           | H    | H       |
| heatindex            | heatindex           | H    | H       |
| UV                   | uv                  | H    | H       |
| extraTemp1           | temperature_2       | H    | H       |
| extraTemp2           | temperature_3       | H    | H       |
| extraTemp3           | temperature_4       | H    | H       |
| extraTemp4           | temperature_5       | H    | H       |
| extraTemp5           | temperature_6       | H    | H       |
| extraTemp6           | temperature_7       | H    | H       |
| extraTemp7           | temperature_8       | H    | H       |
| extraHumid1          | humidity_2          | H    | H       |
| extraHumid2          | humidity_3          | H    | H       |
| extraHumid3          | humidity_4          | H    | H       |
| extraHumid4          | humidity_5          | H    | H       |
| extraHumid5          | humidity_6          | H    | H       |
| extraHumid6          | humidity_7          | H    | H       |
| extraHumid7          | humidity_8          | H    | H       |
| outTempBatteryStatus | battery_status_out  | H    |         |
| rainBatteryStatus    | rain_battery_status | H    |         |
| windBatteryStatus    | wind_battery_status | H    |         |
| uvBatteryStatus      | uv_battery_status   | H    |         |

Each packet contains a subset of all possible readings. For example, a temperature packet contains `temperature_N`
and `battery_status_N`, a rain packet contains `rain_total` and `rain_rate`.

- H indicates data provided by Hardware
- D indicates data calculated by the Driver
- S indicates data calculated by the StdWXCalculate Service

Copyright (c) 2013 Chris Manton <cmanton@gmail.com>  www.onesockoff.org
