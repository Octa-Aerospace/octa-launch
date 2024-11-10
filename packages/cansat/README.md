# CanSat device codebase

## Configuration

The application uses environment variables for configuration. Create a `.env` file in the project root with the following variables:

```ini
# GPIO Pins
BUZZER_PIN=12
BUTTON_GPIO=5

# I2C Address
I2C_ADDRESS=0x68

# LoRa Configuration
RADIO_FREQ_MHZ=915.0
BAUDRATE=1000000

# Timezone
TIMEZONE=America/Santiago
```

---

## TODO 

- [ ] Implement poetry for dependency and env management


## Dev notes so far

### venv steps

1. python -m venv base 
2. source base/bin/activate


### deps

1. python -m pip install RPi.GPIO
2. python -m pip install adafruit-circuitpython-rfm9x
3. install the following with only pip

```
  python-dotenv
  pytz
```

