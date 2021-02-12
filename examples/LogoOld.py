from EasyBeam import Beam2D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

Logo = Beam2D()
b = 10      # mm
h = 20      # mm
Logo.Properties = [['Prop1', 7.85e-9, 210000, 0.3, 1, b, h]]
# Knoten [mm]
Logo.Nodes = np.array([[ 90, 100],
                       [ 10, 100],
                       [  0,  90],
                       [  0,  50],
                       [  0,  10],
                       [ 10,   0],
                       [ 90,   0],
                       [ 80,  50],
                       [120,   0],  # a
                       [170,   0],
                       [180,  10],
                       [180,  35],
                       [180,  60],
                       [170,  70],
                       [120,  70],
                       [110,  10],
                       [110,  25],
                       [120,  35],
                       [200,   0],  # s
                       [260,   0],
                       [270,  10],
                       [270,  25],
                       [260,  35],
                       [210,  35],
                       [200,  45],
                       [200,  60],
                       [210,  70],
                       [270,  70],
                       [290,  70],  # y
                       [290,  10],
                       [300,   0],
                       [350,   0],
                       [360,  10],
                       [360,  70],
                       [360, -25],
                       [350, -35],
                       [300, -35],
                       [380,   0],  # B
                       [380,  50],
                       [380, 100],
                       [460, 100],
                       [470,  90],
                       [470,  60],
                       [460,  50],
                       [470,  40],
                       [470,  10],
                       [460,   0],
                       [500,   0],  # e
                       [560,   0],
                       [490,  10],
                       [490,  35],
                       [490,  60],
                       [500,  70],
                       [550,  70],
                       [560,  60],
                       [560,  45],
                       [550,  35],
                       [590,   0],  # a
                       [580,  10],
                       [580,  25],
                       [590,  35],
                       [650,  35],
                       [640,   0],
                       [650,  10],
                       [650,  60],
                       [640,  70],
                       [590,  70],
                       [670,   0],
                       [670,  60],
                       [680,  70],
                       [710,  70],
                       [720,  60],
                       [720,   0],
                       [730,  70],
                       [760,  70],
                       [770,  60],
                       [770,   0]])
# Elemente: welche Knoten werden verbunden?
Logo.El = np.array([[ 0,  1],
                    [ 1,  2],
                    [ 2,  3],
                    [ 3,  4],
                    [ 4,  5],
                    [ 5,  6],
                    [ 3,  7],
                    [ 6,  8],
                    [ 8,  9],
                    [ 9, 10],
                    [10, 11],
                    [11, 12],
                    [12, 13],
                    [13, 14],
                    [ 8, 15],
                    [15, 16],
                    [16, 17],
                    [17, 11],
                    [ 9, 18],
                    [18, 19],
                    [19, 20],
                    [20, 21],
                    [21, 22],
                    [22, 23],
                    [23, 24],
                    [24, 25],
                    [25, 26],
                    [26, 27],
                    [27, 28],
                    [28, 29],
                    [29, 30],
                    [30, 31],
                    [31, 32],
                    [32, 33],
                    [32, 34],
                    [34, 35],
                    [35, 36],
                    [31, 37],
                    [37, 38],
                    [38, 39],
                    [39, 40],
                    [40, 41],
                    [41, 42],
                    [42, 43],
                    [43, 44],
                    [44, 45],
                    [45, 46],
                    [46, 37],
                    [38, 43],
                    [46, 47],
                    [47, 48],
                    [47, 49],
                    [49, 50],
                    [50, 51],
                    [51, 52],
                    [52, 53],
                    [53, 54],
                    [54, 55],
                    [55, 56],
                    [56, 50],
                    [48, 57],
                    [57, 58],
                    [58, 59],
                    [59, 60],
                    [60, 61],
                    [57, 62],
                    [62, 63],
                    [63, 61],
                    [61, 64],
                    [64, 65],
                    [65, 66],
                    [62, 67],
                    [67, 68],
                    [68, 69],
                    [69, 70],
                    [70, 71],
                    [71, 72],
                    [71, 73],
                    [73, 74],
                    [74, 75],
                    [75, 76]])
Logo.PropID = ["Prop1"]*len(Logo.El)
# Randbedingungen und Belastung [N] bzw. [Nmm]
Logo.Disp = [[ 0, [0, 0, 0]]]
Logo.Load = [[76, [0, -200, 0]]]
Logo.nStep = 100
Logo.Initialize()

Logo.StaticAnalysis()
Logo.Scale = 2
Logo.ComputeStress()

Logo.PlotMesh()
Logo.PlotDisplacement()
