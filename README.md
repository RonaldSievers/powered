# Powered
(Work in progress)

### Description

This app can be run on your raspberry Pi. It will try to detect
your P1 meter (using zeroconf) and then read out the actual power
every second. This data is then used to control a series
of LED lights to indicate the power usage (being negative or positive).

### Interactions

`make run` -- this will build the image first (targeted at ARM cpus) and then run it

`make push` -- build the image and push it to the repo

`make test` -- run all unit tests

