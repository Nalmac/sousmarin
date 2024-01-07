from Interfaces.SolverInterface import SolverInterface
from Utils.Sigmoide import genererOrdre2
import numpy as np

# On postule que z est une sigmoïde

class Grapher():
    def __init__(self):
        pass

    def simulation(self, I : np.ndarray, solver : SolverInterface, zc_max : float, tau : float, phi : float):
        import matplotlib.pyplot as plt
        
        z,dz,d2z = genererOrdre2(zc_max, tau, phi)
        rho = solver.solveRho(dz, d2z)
        v = solver.vEauFromRho(rho)

        V,Z = v(I),z(I)

        ax = plt.axes([0.1, 0.20, 0.4, 0.75])
        graphe_V, = ax.plot(I,V)

        ax2 = plt.axes([0.55, 0.2, 0.4, 0.75])
        graphe_z, = ax2.plot(I, Z)


        ax_curseurZ = plt.axes([0.25, 0.05, 0.6, 0.03])
        curseurZ = Slider(ax_curseurZ, "Profondeur", 0, zc_max, valinit=zc_max)

        def updateZ(event):
            zc = curseurZ.val
            tau = curseurTAU.val
            
            z,dz,d2z = genererOrdre2(zc, tau, phi)
            rho = solver.solveRho(dz, d2z)
            v = solver.vEauFromRho(rho)

            VMODIFIE = v(I)
            ZMODIFIE = z(I)

            graphe_V.set_data(I, VMODIFIE)
            graphe_z.set_data(I, ZMODIFIE)
            print( f"Nouveau volume : V_MAX = {np.max(VMODIFIE)}", f" V_MIN = {np.min(VMODIFIE)}")
            plt.draw()

        curseurZ.on_changed(updateZ)

        ax_curseurTAU = plt.axes([0.25, 0.01, 0.6, 0.03])
        curseurTAU = Slider(ax_curseurTAU, r"$\tau$", 0, tau+1, valinit=tau)

        def updateTAU(event):
            zc = curseurZ.val
            tau = curseurTAU.val
            
            z,dz,d2z = genererOrdre2(zc, tau, phi)
            rho = solver.solveRho(dz, d2z)
            v = solver.vEauFromRho(rho)

            VMODIFIE = v(I)
            ZMODIFIE = z(I)

            graphe_V.set_data(I, VMODIFIE)
            graphe_z.set_data(I, ZMODIFIE)
            print( f"Nouveau volume : V_MAX = {np.max(VMODIFIE)}", f" V_MIN = {np.min(VMODIFIE)}")
            plt.draw()

        curseurTAU.on_changed(updateTAU)

        plt.show()