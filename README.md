**David Alfonso and Jesús Moncayo Embedded Systems Final Project - Raspberry Pi Plant Monitoring**

## Overview

This GitHub repository contains the source code for an embedded systems project focused on plant monitoring using a Raspberry Pi. The project involves reading data from various sensors connected to the Raspberry Pi, processing and storing this information, and utilizing daemons for periodic execution.

## Project Components

1. **Sensor Readings:**
    - Code for reading temperature and humidity using LM75 and YL69 sensors.
    - Script for capturing images using the Raspberry Pi camera module.

2. **Communication:**
    - Python script for sending data to Thingspeak for visualization.
    - Bash script for sending captured images to an Azure database.

3. **Daemon and Timer:**
    - Bash script for calling all the necessary functions periodically.
    - Daemon service and timer configuration for scheduled execution.

4. **Timestamp Handling:**
    - Python script for obtaining and formatting timestamps with time zone information.
    - Timestamp incorporation in sensor readings and file naming.

## File Organization

- `scripts/`: Contains individual scripts for sensor readings, communication, image capture, and timestamp handling.
- `daemon/`: Includes the bash script for periodic execution and the daemon service and timer configuration files.
- `README.md`: Project overview, file organization, and usage instructions.

## Usage

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/David-Alfonso/alfonso-moncayo_embedded_systems_final_project.git
    cd alfonso-moncayo_embedded_systems_final_project
    ```

2. **Execute the Project:**
    - Initialize the daemon service for periodic execution.
    - Execute individual scripts for specific functionalities and proofs.

4. **Adjust Configurations:**
    - Modify sensor configurations, API keys, and file paths as needed.

## Conclusion

Explore the source code and adapt it to your requirements. This project showcases a comprehensive approach to plant monitoring using embedded systems and Raspberry Pi.

Feel free to contribute, report issues, or provide feedback!

---

*Note: Please ensure that all necessary dependencies are installed before running the scripts.*
