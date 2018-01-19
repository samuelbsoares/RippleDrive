#
#import InternalGyro
#import PowerManagement
#
#
#
#FT + test + Voltage test  => LINKEDS
#
#at end of interval => consolidate the values, end values => google cloud
#
#2 values 
#    -   max positive angle 
#    -   max negative angle (min angle)
#
#record gyro for 30 sec => find maxes => to cloud
#
#

#CLASS : Gyro for the Gyroscopes
#   params : 
#       - list of angles 
#       - maxAngle 
#       - minAngle
#       - 
#   functions : 
#       - init :
#           +   param : (int) 6050 or (int) 9250
#
#       - fetch data : 
#           +   add datas to list of angles  
#
#       - getMaxMin : 
#           +   get Max => put to maxAngle
#           +   get Min => assign to minAngle
#
#       - push : push maxAngle + minAngle to Google Drive
#           +   (do the pushing)
#
#
class Gyros(object):

    __devices = []
    __angles = []

    #init : 
    #   param : CODE : int to know what MPU this object is
    def __init__(self, CODE):

        #list of angles to do pushing
        if (not CODE or (CODE != 6050 and CODE != 9250)):
            raise ValueError
        
        self.__gyro = None
        self.maxAngle = -10000;
        self.minAngle = 10000;

        # init the Gyro Scope
        if CODE == 6050 : 
            # TODO: DO INIT FOR 6050
            import MPU6050
	        __gyro = MPU6050.MPU6050()
            return None

        elif CODE == 9250 : 
            # TODO: DO INIT FOR 9250

            import MPU9250
            __gyro = MPU9250.MPU9250()
            return None

        else : 
            return "error init, Wrong CODE of MPU"

    #fetch DATA : put all fetch data to a list
    def fetchDatas(self):
        self.__angles.append self.__gyro.get_anglesXY()
        
    #getMaxMin angles, put to class variables
    def getMaxMin(self):
        for angle in self.angles : 
            if angle > self.maxAngle : 
                self.maxAngle = angle 
            if angle < self.minAngle : 
                self.minAngle = angle;
    
    #push to Google drive
    def push(self):
        print ("doing the pushing");
        print (self.maxAngle)
        print (self.minAngle)
        #TODO: DO THE PUSHING
