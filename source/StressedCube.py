# Module for calculations related to stress

import numpy as np

class StressedCube:

    def __init__(self, stressTensor, normalDirection):
        self.stressTensor = stressTensor
        self.normalDirection = normalDirection
        pass

    def getTraction(self):
        return np.matmul(self.stressTensor, self.normalDirection)
    
    def getTractionMagnitude(self):
        return np.linalg.norm(self.getTraction(), 2)
    
    def getPrincipalStressValues(self):
        return np.linalg.eigvals(self.stressTensor)
    
    def getPrincipalStressDirections(self):
        return np.linalg.eig(self.stressTensor)
    
    def getTractionNormalComponent(self):
        return np.matmul(
            self.getTraction(), self.normalDirection
        )
    
    def getTractionShearComponent(self):
        tin = self.getTraction()
        sigma_n = self.getTractionNormalComponent()
        return np.matmul(tin, tin) - sigma_n**2
    
    def getNormalStressAngle(self, angle='rad'):
        '''Calculates the normal stress angle
        parameters:
            angle: ('rad' or 'deg', 'rad' default) is the angle units.
        '''
        sigma_n = self.getTractionNormalComponent()
        result = np.arccos( sigma_n / self.getTractionMagnitude() )
        if angle == 'deg':
            result = result*(180/np.pi)
        return result