import smbus
import time
import datetime as dt
from pytz import timezone  # Ensure you have the pytz library installed

# Obtain the current date and time with the local timezone
current_date = dt.datetime.now(timezone('UTC'))

# Convert the date and time to the Bogotá timezone
target_timezone = timezone('America/Bogota')
current_date = current_date.astimezone(target_timezone)

# Format the date with the timezone offset as "-05:00"
formatted_date = current_date.strftime("%Y-%m-%dT%H:%M:%S%z")

# Insert the colon in the timezone offset
formatted_date_with_colon = formatted_date[:-2] + ":" + formatted_date[-2:]

# LM75 I2C address and bus number (default address is 0x48)
address = 0x48
bus_number = 1

# Initialize the I2C bus
bus = smbus.SMBus(bus_number)

try:
    # Read temperature data from the LM75 sensor
    raw_temperature = bus.read_word_data(address, 0)
    temperature = ((raw_temperature << 8) & 0xFF00) + (raw_temperature >> 8)

    # Convert raw data to temperature in degrees Celsius
    temperature = (temperature >> 7) * 0.5

    # Print the temperature reading
    print(f"TimeStamp: {formatted_date_with_colon} Temperature: {temperature}°C")

    # Save the temperature reading to a text file
    with open("/home/david/proyecto_final/temperature.txt", "a+") as file:
        file.write(f"{formatted_date_with_colon},{temperature}\n")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the I2C bus
    bus.close()
