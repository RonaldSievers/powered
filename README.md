# Powered
(Work in progress)

### Description

This app can be run on your raspberry Pi. It will try to detect
your P1 meter (using zeroconf) and then read out the actual power
every second. This data is then used to control a series
of LED lights to indicate the power usage (being negative or positive).

### Interactions

`make run` -- will run the latest version using docker compose (not detached) - use this on your raspberry pi!!

`make push` -- build the image and push it to the repo (targeted at ARM cpus)

`make test` -- run all unit tests

