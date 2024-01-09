from Interfaces.SolverInterface import SolverInterface
from Utils.Sigmoide import genererOrdre2
import numpy as np

# On postule que z est une sigmoïde

class Grapher():
    def __init__(self):
        pass

    def simulation(self, T : list[float], solver : SolverInterface, zc_max : float, tau : float, phi : float):
        import matplotlib.pyplot as plt
        from matplotlib.widgets import Slider
        
        z,v = solver.genererZV(zc_max, tau, phi)

        I = np.linspace(T[0], T[1], 1000)

        V,Z = v(I)*(1e6),z(I)

        ax = plt.axes([0.1, 0.20, 0.4, 0.75])
        ax.set_xlabel(r"Temps $t$")
        ax.set_ylabel(r"$V_{eau}$")
        graphe_V, = ax.plot(I,V)

        
        ax2 = plt.axes([0.55, 0.2, 0.4, 0.75])
        ax2.set_xlabel(r"Temps $t$")
        ax2.set_ylabel(r"Profondeur $z$")
        graphe_z, = ax2.plot(I, Z)


        ax_curseurZ = plt.axes([0.25, 0.05, 0.6, 0.03])
        curseurZ = Slider(ax_curseurZ, "Profondeur", 0, zc_max, valinit=zc_max)

        def update(event):
            zc = curseurZ.val
            tau = curseurTAU.val
            
            z,v = solver.genererZV(zc, tau, phi)

            VMODIFIE = v(I)*(1e6)
            ZMODIFIE = z(I)

            graphe_V.set_data(I, VMODIFIE)
            graphe_z.set_data(I, ZMODIFIE)
            print( f"Nouveau volume : V_MAX = {np.max(VMODIFIE)}", f" V_MIN = {np.min(VMODIFIE)}")
            plt.draw()

        curseurZ.on_changed(update)

        ax_curseurTAU = plt.axes([0.25, 0.01, 0.6, 0.03])
        curseurTAU = Slider(ax_curseurTAU, r"$\tau$", 0, 2*tau, valinit=tau)

        curseurTAU.on_changed(update)

        plt.show()