from enum import Enum


class SensorType(Enum):

    VISION 		= "vision"
    RADAR 		= "radar"
    LIDAR 		= "lidar"
    GPS 			= "gps"
    IMU 			= "imu"
    PROXIMITY = "proximity"