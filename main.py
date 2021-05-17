from kinetics import Electron
import geometry

CLUSTER_DIAMETER = 5.8e-9
M_TO_EFF = 0.014
AFFINITY = 3.16
FIELD = 1e7


class Simulation:
    def __init__(self):
        self.electron = Electron(0.01, M_TO_EFF)
        self.cluster = geometry.Cluster(d=CLUSTER_DIAMETER,
                                        m_to_eff=M_TO_EFF,
                                        height=AFFINITY,
                                        field=FIELD,
                                        electron=self.electron)

    def iterate(self, n):
        for i in range(n):
            self.cluster.iteration()
        velocity_x = self.electron.x / self.electron.t
        return velocity_x


def main():
    sim = Simulation()
    print('Mean velocity of electron is{}'.format(sim.iterate(1000)))


if __name__ == '__main__':
    main()
