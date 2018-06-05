# bbb-adc-measure

This is a simple script to use ADC input on Beaglebone black to measure camera shutter speed.

### Schematic

![Schematic](https://1.bp.blogspot.com/-3vlNi54jXmc/WxYY6b4fxzI/AAAAAAAANcY/x0ve8wLg8XkhJym77QLIJNzLTCJONOrUACLcBGAs/s320/schematic.png)

A photoresistor is used to detect the light when shutter open, and hence changing the values read by ADC pin P9_40.  The push button is used to trigger the Python script to start reading the ADC input.

![breadboard](https://2.bp.blogspot.com/-Z-kL8s7ylyk/WxYbBF8Rj4I/AAAAAAAANc8/q6ammQacZ7oci9RTwChF2lK8qEb1JvQbACLcBGAs/s320/IMG_20180603_164944.jpg)

![result](https://4.bp.blogspot.com/-TiTPcBT4kNo/WxYbBA9pPTI/AAAAAAAANdA/S0WUAq-fsh0e6uqQVXJam5oWxNub9wIiACLcBGAs/s320/IMG_20180604_212937.jpg)

### Quick start
```
git clone https://github.com/kitsook/bbb-adc-measure
cd bbb-adc-measure
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python adc-measure.py -t 10 > result.csv
```

Output can be plotted with `gnuplot`, e.g.
```
gnuplot
set mxtics 10
set grid
plot 'result.csv' with lines
```

![plot](https://1.bp.blogspot.com/-nH5xWa5DVi8/WxYZZhu4wpI/AAAAAAAANcg/wl2kxCR-Mu8MpaN1Zn32DyMKF5fAeMtaQCLcBGAs/s320/pentax_mx_15_8.png)

Note that this is by no mean an accurate measure of absolute shutter speed.  The response time of photoresistor will affect the result.  Nevertheless, it is useful to compare different shutter speeds.
