#!/usr/bin/env python3

from commands2 import TimedCommandRobot
from wpilib._impl.main import run

from ctre import WPI_TalonSRX
from wpilib import DigitalInput,AnalogPotentiometer
from wpilib.interfaces import PIDSource
from rev import CANSparkMax,MotorType

import math
import shutil,sys

class MOTORtESTbOARD(TimedCommandRobot):
    def robotInit(self):
        # motor controllers
        self.talonMotor = WPI_TalonSRX(12)
        self.sparkMotor = CANSparkMax(1,MotorType.kBrushless)
        
        # potentiaionmersters
        self.potent1 = AnalogPotentiometer(1)
        self.potent2 = AnalogPotentiometer(0)
        
        # switches
        self.talonSwitchF = DigitalInput(0)
        self.talonSwitchB = DigitalInput(1)
        
        self.sparkSwitchF = DigitalInput(2)
        self.sparkSwitchB = DigitalInput(3)
    
    def getTalonDirection(self):
        if self.talonSwitchF.get():
            return "forward"
        elif self.talonSwitchB.get():
            return "backward"
        else:
            return "off"
        
    def getSparkDirection(self):
        if self.sparkSwitchF.get():
            return "forward"
        elif self.sparkSwitchB.get():
            return "backward"
        
    def setTalonSpeed(self,speeds):
        self.talonMotor.set(speeds)
        
    def setSparkSpeed(self,speeds):
        self.sparkMotor.set(speeds)
    
    def robotPeriodic(self):
        talonDir = self.getTalonDirection()
        sparkDir = self.getSparkDirection()
        potentTalVal = self.potent1.get()
        potentSparkVal = abs(1-self.potent2.get())
        
        if talonDir != "off":
            if talonDir == "forward":
                self.setTalonSpeed(potentTalVal)
            else:
                self.setTalonSpeed(-potentTalVal)
                
        if sparkDir != "off":
            if sparkDir == "forward":
                self.setSparkSpeed(potentSparkVal)
            else:
                self.setSparkSpeed(-potentSparkVal)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "deploy":
        shutil.rmtree("opkg_cache",ignore_errors=True)
        shutil.rmtree('pip_cache',ignore_errors=True)
    run(MOTORtESTbOARD)
