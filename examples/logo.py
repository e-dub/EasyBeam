from EasyBeam import Beam2D
import numpy as np

Test = Beam2D()
# Knoten
Test.N = np.array([[ 100, 100],  # 0 E
                   [   0, 100],  # 1 E
                   [   0,  50],  # 2 E
                   [ 100,  50],  # 3 E
                   [   0,   0],  # 4 E
                   [ 100,   0],  # 5 E/A
                   [ 150,  50],  # 6 A
                   [ 200, 100],  # 7 A
                   [ 200,   0],  # 8 A/S
                   [ 350,   0],  # 9 S/Y
                   [ 350,  50],  # 10 S
                   [ 250,  50],  # 11 S
                   [ 250, 100],  # 12 S
                   [ 350, 100],  # 13 S/Y
                   [ 400,  50],  # 14 Y
                   [ 450, 100],  # 15 Y/B
                   [ 450,  50],  # 16 B
                   [ 450,   0],  # 17 B
                   [ 550,   0],  # 18 B/E
                   [ 550,  50],  # 19 B/E
                   [ 550, 100],  # 20 B/E
                   [ 650, 100],  # 21 E
                   [ 650,  50],  # 22 E
                   [ 650,   0],  # 23 E/A
                   [ 750, 100],  # 24 A/M
                   [ 750,   0],  # 25 A/M
                   [ 850,   0],  # 26 M
                   [ 850, 100],  # 27 M
                   [ 950,   0]])  # 28 M
# Elemente: welche Knoten werden verbunden?
Test.El = np.array([[0, 1],
                    [1, 2],
                    [2, 3],
                    [2, 4],
                    [4, 5],
                    [5, 6],
                    [6, 7],
                    [7, 8],
                    [8, 9],
                    [9, 10],
                    [10, 11],
                    [11, 12],
                    [12, 13],
                    [13, 14],
                    [14, 15],
                    [14,  9],
                    [15, 16],
                    [16, 17],
                    [17, 18],
                    [18, 19],
                    [16, 19],
                    [20, 19],
                    [15, 20],
                    [21, 20],
                    [22, 19],
                    [18, 23],
                    [23, 24],
                    [25, 24],
                    [24, 26],
                    [26, 27],
                    [27, 28]])
# Boundary conditions and loads
Test.BC = [0, 1, 2]
Test.Load = [[26, -10],
             [27, -10],
             [18, -10],
             [19, -10]]
Test.Initialize()
# Querschnitte
b = 10      # mm
h = 10      # mm
Test.eU = np.ones([Test.nEl, 1])*h/2
Test.eL = np.ones([Test.nEl, 1])*-h/2
Test.A = np.ones([Test.nEl, 1])*b*h     # mm^2
Test.I = np.ones([Test.nEl, 1])*b*h**3/12    # mm^4
# Hier den E-Modul definieren!
Test.E = np.ones([Test.nEl, 1])*210000        # MPa
Test.Solve()
Test.Scale = 10
Test.ComputeStress()
Test.PlotMesh(ElementNumber=False)
Test.PlotMesh(NodeNumber=False)
Test.PlotStress(stress="all")
Test.PlotDisplacement()
Test.PlotDisplacement()