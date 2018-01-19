import time as t

class Gyros( object ):

    anglesMPU6050 = []
    anglesMPU9250 = []

    #init : 
    def __init__( self ):

        self.maxAngle = float('-inf');
        self.minAngle = float('+inf');

        import MPU6050
        self.mpu6050 = MPU6050.MPU6050()

        import MPU9250
        self.mpu9250 = MPU9250.MPU9250()


    #fetch DATA : put all fetch data to a list
    def fetchDatas( self ):
        for _ in range(300):
            self.anglesMPU6050.append( self.mpu6050.get_anglesXY() )
            self.anglesMPU9250.append( self.mpu9250.get_anglesXY() )
            t.sleep(.1)
                    
    #getMaxMin angles, put to class variables
    """
    Returns:
    [ max_MPU6050_X_angle, max_MPU6050_Y_angle, min_MPU6050_X_angle, 
    min_MPU6050_Y_angle], [ max_MPU9250_X_angle, max_MPU9250_Y_angle, 
    min_MPU9250_X_angle, min_MPU9250_Y_angle ]
    """
    def getMaxMin( self ):
         return [ [ max( self.anglesMPU6050, key = lambda x: x[0] )[0],
                  max( self.anglesMPU6050, key = lambda x: x[1] )[1],
                  min( self.anglesMPU6050, key = lambda x: x[0] )[0],
                  min( self.anglesMPU6050, key = lambda x: x[1] )[1] ],
                  [ max( self.anglesMPU9250, key = lambda x: x[0] )[0],
                  max( self.anglesMPU9250, key = lambda x: x[1] )[1],
                  min( self.anglesMPU9250, key = lambda x: x[0] )[0],
                  min( self.anglesMPU9250, key = lambda x: x[1] )[1] ] ]
    
    #push to Google drive
    def push(self):
        print( getMaxMin() )
        print ("doing the pushing");

if __name__ == "__main__":
    g = Gyros()
    g.fetchDatas()
    g.push()
