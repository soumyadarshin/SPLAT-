# SPLAT Project

The SPLAT Project is a Python-based tool that works in conjunction with the SPLAT software to generate detailed reports about transmitter and receiver data. It helps calculate and analyze the height of transmitters, receiver distances, and other important parameters related to radio propagation.

## Overview

This project utilizes the SPLAT (Software for Propagation Loss, Antenna, and Terrain) software to calculate the propagation path loss, antenna parameters, and other metrics based on provided data. The SPLAT software is a critical component of the system, and the project generates a detailed report about:

- **Transmitter Height**
- **Receiver Distance**
- **Propagation Loss**
- **Antenna Characteristics**
- **Terrain Analysis**

## Prerequisites

To use the SPLAT Project, you need to have the following installed:

- **SPLAT Software**: SPLAT is the key software required to generate reports based on the provided data. You can download it from the official SPLAT website or repository.  
  [SPLAT Software Documentation](https://www.splat.org/)
- **Python 3.x**: The project is written in Python, so you will need Python installed.
- **Required Python Libraries**: You will also need some Python libraries for data processing, like `pandas` and `psycopg2`.

To install the necessary Python libraries, run:

```bash
pip install -r requirements.txt


Setup
Install SPLAT Software:

Download and install the SPLAT software.

Follow the installation guide available in the SPLAT documentation for your operating system.

Clone the Repository: Clone this repository to your local machine using Git:

git clone https://github.com/yourusername/splat-project.git
cd splat-project


Configure Database Connection: The project may interact with a PostgreSQL database to retrieve data (e.g., transmitter and receiver locations, antenna parameters). Ensure that your database is correctly configured and the connection details (DB_HOST, DB_NAME, DB_USER, DB_PASSWORD) are properly set in the excel.py or configuration file.

Run the Project: After setting up the SPLAT software and the database, you can run the Python script that interacts with SPLAT and generates the report:

Usage
Inputs
The project expects certain inputs for transmitter and receiver parameters to generate the report, including:

Transmitter Location (Latitude, Longitude, Altitude)

Receiver Location (Latitude, Longitude, Altitude)

Transmitter Power

Antenna Heights

Antenna Gain

Frequency Band

Terrain Data (optional, if available)

You can provide this data in your own format or via a database connected to the project.


Outputs
After running the script, the project will output a detailed report that includes:

Transmitter and receiver heights

The distance between the transmitter and receiver

Path loss calculations

Detailed terrain and antenna characteristics

Propagation model outputs (e.g., Hata, Okumura, etc.)

Sample Output:
The output report will provide the following details:
Transmitter Height: 50 meters
Receiver Distance: 15 kilometers
Path Loss: 120 dB
...


Contributing
If you'd like to contribute to the SPLAT Project, feel free to fork the repository, create a feature branch, and submit a pull request. Please make sure your changes are well-documented and adhere to the coding standards used in this project.

Fork the repository.

Create a new branch (git checkout -b feature-name).

Commit your changes (git commit -m 'Add new feature').

Push to the branch (git push origin feature-name).

Open a pull request.

Acknowledgments
Special thanks to the developers of the SPLAT software for providing a comprehensive tool for radio propagation analysis.

This project was inspired by the need to automate the process of generating radio propagation reports based on real-world data.
