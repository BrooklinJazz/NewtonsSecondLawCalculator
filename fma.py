import sys

F = sys.argv[1]  # Newtons
M = sys.argv[2]  # Kilograms
A = sys.argv[3]  # m/s^2


def parseFloatOrNone(floatOrNone):
    if floatOrNone == 'None':
        return None
    else:
        return float(floatOrNone)


class FMA:
    def __init__(self, force, mass, acceleration):
        self.force = parseFloatOrNone(force)
        self.mass = parseFloatOrNone(mass)
        self.acceleration = parseFloatOrNone(acceleration)

    def parameters(self):
        return [self.force, self.mass, self.acceleration]

    def numberOfUndefinedParams(self):
        numberOfUndefinedParams = 0
        for param in self.parameters():
            if param is None:
                numberOfUndefinedParams = numberOfUndefinedParams + 1
            pass
        return numberOfUndefinedParams

    def isSolvable(self):
        return self.numberOfUndefinedParams() <= 1

    def calcForce(self):
        return self.mass * self.acceleration

    def calcMass(self):
        return self.force / self.acceleration

    def calcAcceleration(self):
        return self.force / self.mass

    def solveForX(self):
        if self.isSolvable() is False:
            raise Exception("equation is not solvable")
        pass
        if self.acceleration is None:
            return FMA(self.force, self.mass, self.calcAcceleration())
        pass
        if self.force is None:
            return FMA(self.calcForce(), self.mass, self.acceleration)
        pass
        if self.mass is None:
            return FMA(self.force, self.calcMass(), self.acceleration)
        pass

    def toString(self):
        return "force: {}, mass: {}, acceleration: {}".format(
            self.force, self.mass, self.acceleration)

    def verifyAcceleration(self):
        return self.calcAcceleration() == self.acceleration

    def verifyMass(self):
        return self.calcMass() == self.mass

    def verifyForce(self):
        return self.calcForce() == self.force

    def checkMath(self):
        return  self.verifyAcceleration() and self.verifyForce() and self.verifyMass()

def main():
    equation = FMA(F, M, A)
    if equation.numberOfUndefinedParams() == 0 and equation.checkMath():
        return print(equation.toString(), "is correct!")
        pass
    elif (equation.numberOfUndefinedParams() == 0):
        return print(equation.toString(), "is incorrect")
    else:
        return print(equation.solveForX().toString())

main()