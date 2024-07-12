import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Button

class BlochSphere:
    def __init__(self):
        self.fig = plt.figure(figsize=(10, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.setup_sphere()
        self.setup_buttons()
        self.state_vector = None

    def setup_sphere(self):
        u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
        x = np.cos(u)*np.sin(v)
        y = np.sin(u)*np.sin(v)
        z = np.cos(v)
        self.ax.plot_wireframe(x, y, z, color="lightgray", alpha=0.2)

        self.ax.quiver(0, 0, -1, 0, 0, 2, color='k', arrow_length_ratio=0.05)
        self.ax.quiver(0, -1, 0, 0, 2, 0, color='k', arrow_length_ratio=0.05)
        self.ax.quiver(-1, 0, 0, 2, 0, 0, color='k', arrow_length_ratio=0.05)

        self.ax.text(0, 0, 1.2, r'$\left|0\right>$', fontsize=15)
        self.ax.text(0, 0, -1.3, r'$\left|1\right>$', fontsize=15)
        self.ax.text(1.2, 0, 0, r'$x$', fontsize=15)
        self.ax.text(0, 1.2, 0, r'$y$', fontsize=15)

        self.ax.set_axis_off()
        self.ax.view_init(elev=20, azim=45)

    def setup_buttons(self):
        button_zero = plt.axes([0.7, 0.05, 0.1, 0.075])
        button_one = plt.axes([0.81, 0.05, 0.1, 0.075])
        button_plus = plt.axes([0.7, 0.15, 0.1, 0.075])
        button_minus = plt.axes([0.81, 0.15, 0.1, 0.075])
        
        # probability of 1 and 0 setup -1
        button_A = plt.axes([0.7, 0.25, 0.1, 0.075])
        button_B = plt.axes([0.81, 0.25, 0.1, 0.075])

        self.b_zero = Button(button_zero, '|0⟩')
        self.b_one = Button(button_one, '|1⟩')
        self.b_plus = Button(button_plus, '|+⟩')
        self.b_minus = Button(button_minus, '|-⟩')
        
        # probability of 1 and 0 setup -2
        self.b_A = Button(button_A, '<P(0)')
        self.b_B = Button(button_B, '<P(1)')

        self.b_zero.on_clicked(self.zero_state)
        self.b_one.on_clicked(self.one_state)
        self.b_plus.on_clicked(self.plus_state)
        self.b_minus.on_clicked(self.minus_state)
        
        # probability of 1 and 0 setup -3
        self.b_A.on_clicked(self.A_state)
        self.b_B.on_clicked(self.B_state)

    def update_state(self, x, y, z):
        if self.state_vector:
            self.state_vector.remove()
        self.state_vector = self.ax.quiver(0, 0, 0, x, y, z, color='r', arrow_length_ratio=0.05)
        self.fig.canvas.draw_idle()

    def zero_state(self, event):
        self.update_state(0, 0, 1)

    def one_state(self, event):
        self.update_state(0, 0, -1)

    def plus_state(self, event):
        self.update_state(1/np.sqrt(2), 0, 1/np.sqrt(2))

    def minus_state(self, event):
        self.update_state(-1/np.sqrt(2), 0, 1/np.sqrt(2))
    
    # probability of 1 and 0 setup -4
    def A_state(self, event):
        self.update_state(1/np.sqrt(2), 0, 1/np.sqrt(2))

    def B_state(self, event):
        self.update_state(1/np.sqrt(2), 0, -1/np.sqrt(2))
        


    def show(self):
        plt.tight_layout()
        plt.show()

bloch = BlochSphere()
bloch.show()