import time
import argparse
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC

PUSH_BUTTON_CHANNEL="P9_41"
ADC_READ_CHANNEL="P9_40"

parser = argparse.ArgumentParser(description='ADC readout')
parser.add_argument('-t', dest='timeout', default=5, type=int,
    help='duration of ADC readout (in seconds)')
args = parser.parse_args()

TIME_OUT = args.timeout

ADC.setup()
GPIO.setup(PUSH_BUTTON_CHANNEL, GPIO.IN)

GPIO.wait_for_edge(PUSH_BUTTON_CHANNEL, GPIO.RISING)
start_time = time.time()
while True:
    current_time = time.time()
    print(current_time - start_time, end="", flush=False)
    print('\t', end="", flush=False)
    print(ADC.read(ADC_READ_CHANNEL), flush=False)
    if current_time - start_time > TIME_OUT:
        break

GPIO.cleanup()

