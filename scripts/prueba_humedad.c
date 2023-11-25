#include <stdio.h>
#include <bcm2835.h>
#include <time.h>

void formatTimezoneOffset(char *buffer, struct tm *timeinfo) {
    int hours = timeinfo->tm_gmtoff / 3600;
    int minutes = (timeinfo->tm_gmtoff % 3600) / 60;
    sprintf(buffer + 19, "%+03d:%02d", hours, minutes);
}

int main() {
    // Get the current time
    time_t rawtime;
    struct tm *timeinfo;
    time(&rawtime);
    timeinfo = localtime(&rawtime);

    // Format the time as per the specified format
    char buffer[80];
    strftime(buffer, sizeof(buffer), "%Y-%m-%dT%H:%M:%S%z", timeinfo);

    // Manually format the timezone offset
    formatTimezoneOffset(buffer, timeinfo);

    // Initialize the bcm2835 library
    if (!bcm2835_init()) {
        printf("bcm2835_init failed. Are you running as root?\n");
        return 1;
    }

    // Define the GPIO pin you want to read (e.g., RPI_GPIO_P1_11 for GPIO 17)
    uint8_t gpioPin = RPI_V2_GPIO_P1_37;

    // Set the pin mode to input
    bcm2835_gpio_fsel(gpioPin, BCM2835_GPIO_FSEL_INPT);

    // Read the state of the GPIO pin
    uint8_t state = bcm2835_gpio_lev(gpioPin);

    // Open a file for writing
    FILE *file = fopen("humidity.txt", "a+");

    if (file == NULL) {
        printf("Failed to open the file for writing.\n");
        return 2;
    }

    // Print the result (0 for LOW, 1 for HIGH) to the file
    fprintf(file, "%s,%d\n",buffer, state ? 0 : 1);

    // Close the file
    fclose(file);

    // Deinitialize the bcm2835 library
    bcm2835_close();

    return 0;
}
