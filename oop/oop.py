class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        def force(self, particle2):
            pass


class ParticleWithMass(Particle):
    def __init__(self, x, y, m):
        super().__init__(x, y)
        self.m = m

    def force(self, particle2):
        f = [0, 0]
        m1 = self.m
        x1 = self.x
        y1 = self.y
        m2 = particle2.m
        x2 = particle2.x
        y2 = particle2.y
        f[0] = m1 * m2 * (x2 - x1) / ((x1 - x2) ** 2 + (y2 - y1) ** 2) ** 1.5
        f[1] = m1 * m2 * (y2 - y1) / ((x1 - x2) ** 2 + (y2 - y1) ** 2) ** 1.5
        return f


class ParticleWithCharge(Particle):
    def __init__(self, x, y, q):
        super().__init__(x, y)
        self.q = q

    def force(self, particle2):
        f = [0, 0]
        q1 = self.q
        x1 = self.x
        y1 = self.y
        q2 = particle2.q
        x2 = particle2.x
        y2 = particle2.y
        f[0] = q1 * q2 * (x1 - x2) / ((x1 - x2) ** 2 + (y2 - y1) ** 2) ** 1.5
        f[1] = q1 * q2 * (y1 - y2) / ((x1 - x2) ** 2 + (y2 - y1) ** 2) ** 1.5
        return f


class ParticleWithMassAndCharge(ParticleWithMass,ParticleWithCharge):
    def __init__(self, x, y, m, q):
        ParticleWithMass.__init__(self, x, y, m)
        ParticleWithCharge.__init__(self,x,y,q)


    def force(self,particle2):
        f1=ParticleWithMass.force(self,particle2)
        f2=ParticleWithCharge.force(self,particle2)
        return f1+f2

class Space:
    def __init__(self, particles: [Particle]):
        self.particles = particles


particle1=ParticleWithMassAndCharge(0,0,10,10)
particle2=ParticleWithMassAndCharge(3,4,10,10)
print(particle1.force(particle2))