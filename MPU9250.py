#!/usr/bin/python

"""

Riple-dribe Project

MPU9250 Gyro Class

Handles communication between a Raspberry Pi and a MPU6050
Gyroscope via I2C protocol using a FT232H device

FT232H acts as an USB to I2C interface and writes/reads data
to/from the gyroscope in the provided register addresses

MPU9250 is little-endian

Check official github for FT232 source code
https://github.com/adafruit/Adafruit_Python_GPIO/blob/master/Adafruit_GPIO/FT232H.py

"""
import CalcUtils as calc
import Adafruit_GPIO.FT232H as FT232H

class MPU9250:

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
    DEFAULT_I2C_ADDRESS = 0x69 # 0x68 -> AD0 = 0; 0x69 ->AD0 = 1
    WAKE = 0
    DEFAULT_SCALING = 16384.0 # (LSB/g) For Sensitivity Scale Factor AFS_SEL=0

    # Vars
    __address = None
    __ft232h = None
    __bus = None # holds actual I2C device

    def __init__( self, address=None, ft232h=None ):
        """
        Initializes address, bus, and ft232h/i2c devices
        """

        ##### CHECK FOR POSSIBLE EXCEPTIONS/ERRORS IN FUNCTIONS BELLOW
        # Temporarily disables FTDI serial drivers.
        FT232H.use_FT232H()

        # Initializes the address if not provided
        if not address: address = self.DEFAULT_I2C_ADDRESS
        self.__address = address

        # Finds the first FT232H device.
        if not ft232h:
            self.__ft232h = FT232H.FT232H()

        # Gets I2C instance from provided FT232H object
        self.__bus = self.__ft232h.get_i2c_device( self.__address )

        self.__bus.write8( PWR_MGMT_1, WAKE )

    def get_gyroXYZ( self ):
        """
        Gets gyroscope values
        """
        gyro_xout = self.__read_i2c_word( self.GYRO_XOUT0 )
        gyro_yout = self.__read_i2c_word( self.GYRO_YOUT0 )
        gyro_zout = self.__read_i2c_word( self.GYRO_ZOUT0 )
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

        Documentation
        https://pypkg.com/pypi/adafruit-gpio/f/Adafruit_GPIO/FT232H.py

        """
        if not regLow: regLow = regHigh + 1
        high = self.__bus.readU8( address, regHigh )
        low = self.__bus.readU8( address, regLow )
        return calc.transform_data( high, low )
