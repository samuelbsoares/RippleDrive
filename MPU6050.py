#!/usr/bin/python

"""

Riple-dribe Project

MPU6050 Gyro Class
Handles communication between a Raspberry Pi and
the MPU6050 Gyroscope using I2C protocol

MPU6050 is big-endian

"""

import CalcUtils
import smbus

class MPU6050:

    # Registers
    PWR_MGMT_1 = 0x6B
    PWR_MGMT_2 = 0x6C
    # LOW = HIGH + 1
    GYRO_XOUT0 = 0x43
    GYRO_YOUT0 = 0x45
    GYRO_ZOUT0 = 0x47
    ACCEL_XOUT0 = 0x3B
    ACCEL_YOUT0 = 0x3D
    ACCEL_ZOUT0 = 0x3F

    # Constants
    DEFAULT_I2C_ADDRESS = 0x68 # 0x68 -> AD0 = 0; 0x69 ->AD0 = 1
    WAKE = 0
    DEFAULT_BUS = 1
    DEFAULT_SCALING = 16384.0  # (LSB/g) For Sensitivity Scale Factor AFS_SEL=0

    # Vars
    __address = None
    __bus = None # holds actual I2C device

    def __init__( self, address = None, smbus = None ):
        """
        Initializes address and bus
        Wakes up device from sleeping mode

        ### COULD CHECK FOR THE CORRECT DEVICE AND TEST IT

        """

        if not address: address = self.DEFAULT_I2C_ADDRESS
        self.__address = address
        if not bus: bus = self.DEFAULT_BUS
        self.__bus = bus

        self.__bus.write_byte_data( address, PWR_MGMT_1, WAKE )

    def get_gyroXYZ( self ):
        """
        Gets gyroscope values
        """
        gyro_xout = self.__read_i2c_word( GYRO_XOUT0 )
        gyro_yout = self.__read_i2c_word( GYRO_YOUT0 )
        gyro_zout = self.__read_i2c_word( GYRO_ZOUT0 )
        return [gyro_xout, gyro_yout, gyro_zout]

    def get_accelXYZ( self ):
        """
        Gets gyroscope values
        """
        accel_xout = self.__read_i2c_word( ACCEL_XOUT0 )
        accel_yout = self.__read_i2c_word( ACCEL_YOUT0 )
        accel_zout = self.__read_i2c_word( ACCEL_ZOUT0 )
        accel_xout_scaled = accel_xout / self.DEFAULT_SCALING
        accel_yout_scaled = accel_yout / self.DEFAULT_SCALING
        accel_zout_scaled = accel_zout / self.DEFAULT_SCALING
        return [accel_xout_scaled, accel_yout_scaled, accel_zout_scaled]

    def get_anglesXY( self ):
        """
        Gets acceleration data and calculates angles for X and Y
        """
        [accel_xout_scaled, accel_yout_scaled, _] = self.get_accelXYZ()
        rot_x = get_x_angle( accel_xout_scaled, accel_yout_scaled, accel_zout_scaled )
        rot_y = get_y_angle( accel_xout_scaled, accel_yout_scaled, accel_zout_scaled )
        return [rot_x, rot_y]

    def __read_i2c_word( self, regHigh, regLow=None ):
        """
        Reads 16-bit values, concatenates them
        and transforms from two's complement

        ### TODO: CHECK IF BIG-ENDIAN!!!

        High and low registers are sequential

        Documentation ???????????
        https://github.com/bivab/smbus-cffi/blob/master/smbus/smbus.py

        """
        if not regLow: regLow = regHigh + 1
        high = self.__bus.read_byte_data( self.__address, regHigh )
        low = self.__bus.read_byte_data( self.__address, regLow )
        return transform_data( high, low )
