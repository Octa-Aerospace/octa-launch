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

- [ ] Implement poetry for dependency and env management (maybe just a setup.py file is better and enough)
- [ ] Automate the startup setup process in a script

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

### Running on startups setup

1. giving permission

  ```bash
  cp -R /path-to-repo/packages/cansat/_startup.sh startup.sh
  chmod +x /path-to-repo/packages/cansat/startup.sh
  ```

2. test the script manually

  ```bash
  /home/pi/octasat/src/octasat/main.py
  ```

3. create a service file

  ```bash
  sudo nano /etc/systemd/system/octasat.service
  ```

4. add the content of the _template.service to that file and save.
5. reload systemd to Recognize the New Service
  
  ```bash
  sudo systemctl daemon-reload
  ```

6. Enable the Service to Start at Boot

  ```bash
  sudo systemctl enable octasat.service
  ```

7. check the status of the service

  ```bash
  sudo systemctl status octasat.service
  ```
