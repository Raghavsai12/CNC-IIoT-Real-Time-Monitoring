# CNC IIoT Real-Time Monitoring Project

## Project Overview
This project demonstrates a real-time CNC (Computer Numerical Control) machine monitoring system using **Azure IoT, SQL Database, and Power BI**. The system collects telemetry from CNC machines, stores it in a database, and visualizes it on a dashboard for analysis.

## Architecture
CNC Machine -> Simulator (Python) -> Azure IoT Hub -> Stream Analytics -> Azure SQL Database -> Power BI Dashboard

## Components
- **Simulator**: Python script simulates CNC telemetry (temperature, motor current, cutting speed).  
- **Azure IoT Hub**: Receives telemetry data from devices.  
- **Azure Stream Analytics**: Processes and forwards telemetry data to SQL Database.  
- **Azure SQL Database**: Stores CNC telemetry for historical analysis.  
- **Power BI**: Visualizes telemetry data in real-time dashboards.  

## Project Structure
CNC-Project/
│
├─ simulator/ # Python simulator for CNC telemetry
│ └─ simulator.py
│
├─ CNCtelemetryDB (Azure files) # Database HTML export
│ └─ CNCtelemetryDB.html
│
├─ DashBoard.pbix # Power BI dashboard file
├─ .gitignore # Ignored files like .env and pycache
├─ requirements.txt # Python dependencies
└─ README.md # Project documentation

## Getting Started

### Prerequisites
1. Python 3.x  
2. Azure Subscription  
3. Azure IoT Hub  
4. Azure SQL Database  
5. Power BI Desktop  

### Setup
1. Install dependencies:
pip install -r requirements.txt
Create .env file in simulator/ folder:
IOTHUB_CONN_STR="Your Azure IoT Hub device connection string here"
Run the simulator:

cd simulator
python simulator.py
This will start sending CNC telemetry data to Azure IoT Hub every 3 seconds.

Database Schema
Table: CNC_Telemetry
Stores real-time CNC machine data.

##Example Stream Analytics Query
This query is used in **Azure Stream Analytics** to process telemetry from IoT Hub and store it in the SQL Database:
sql
SELECT
    temperature,
    motor_current,
    cutting_speed,
    fault_status,
    System.Timestamp AS time
INTO
    SQLTable
FROM
    IoTHubInput
    
##Power BI Dashboard
Connects to Azure SQL Database.
Visualizes real-time CNC machine telemetry: temperature, motor current, and cutting speed.
Allows trend analysis and alerts for abnormal conditions.

##Security Notes
Do not push your .env file to GitHub. It contains secrets like IoT Hub connection strings.
.gitignore is configured to ignore:
.env
__pycache__/
*.pyc

Author
Raghavendra Saiteja Basani
B.Tech – Electrical & Electronics Engineering
Project focused on IIoT, real-time monitoring, and data visualization.

