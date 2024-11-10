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

### **9. Summary of Changes**

- **Used `python-dotenv`** to load environment variables from a `.env` file.
- **Updated `main.py`** to read configuration from environment variables and pass them to module constructors.
- **Modified Modules** (`LoRa`, `BME280`, `Buzzer`) to accept configuration parameters.
- **Ensured Default Values** are provided if environment variables are missing.
- **Excluded `.env`** from version control using `.gitignore`.
- **Documented Configuration** in `README.md`.

---

### **10. Testing the Changes**

Before running the application, ensure that:

- The `.env` file is correctly set up.
- All environment variables have valid values.
- The hardware is properly connected (if not running in dummy mode).

**Run the application:**

```bash
python src/octasat/main.py