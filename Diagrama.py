import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch, ConnectionPatch
import numpy as np

def draw_dfa_before(ax):
    """Dibuja el DFA antes de la minimización"""
    
    # Posiciones de los nodos
    pos_q0 = (-1.5, 0)
    pos_q1 = (0.5, 1)
    pos_q2 = (0.5, -1)
    
    # Dibujar nodos
    # q0 - estado inicial
    circle_q0 = plt.Circle(pos_q0, 0.3, color='white', ec='black', linewidth=2, zorder=3)
    ax.add_patch(circle_q0)
    ax.text(pos_q0[0], pos_q0[1], 'q₀', ha='center', va='center', fontsize=12, fontweight='bold', zorder=5)
    
    # q1
    circle_q1 = plt.Circle(pos_q1, 0.3, color='white', ec='black', linewidth=2, zorder=3)
    ax.add_patch(circle_q1)
    ax.text(pos_q1[0], pos_q1[1], 'q₁', ha='center', va='center', fontsize=12, fontweight='bold', zorder=5)
    
    # q2 - estado de aceptación (doble círculo)
    circle_q2_outer = plt.Circle(pos_q2, 0.3, color='white', ec='black', linewidth=2, zorder=3)
    circle_q2_inner = plt.Circle(pos_q2, 0.24, color='none', ec='black', linewidth=2, zorder=4)
    ax.add_patch(circle_q2_outer)
    ax.add_patch(circle_q2_inner)
    ax.text(pos_q2[0], pos_q2[1], 'q₂', ha='center', va='center', fontsize=12, fontweight='bold', zorder=5)
    
    # Flecha de entrada a q0
    ax.annotate('', xy=(pos_q0[0] - 0.3, pos_q0[1]), xytext=(pos_q0[0] - 0.8, pos_q0[1]),
                arrowprops=dict(arrowstyle='->', lw=2, color='black'))
    
    # Transiciones
    # q0 -> q1 (a) - flecha que termine exactamente en el borde de q1
    start_x = pos_q0[0] + 0.3 * np.cos(np.radians(30))
    start_y = pos_q0[1] + 0.3 * np.sin(np.radians(30))
    end_x = pos_q1[0] - 0.3 * np.cos(np.radians(210))
    end_y = pos_q1[1] - 0.3 * np.sin(np.radians(210))
    
    arrow1 = FancyArrowPatch((start_x, start_y), (end_x, end_y),
                            connectionstyle="arc3,rad=0.1", 
                            arrowstyle='->', lw=1.5, color='black', zorder=1)
    ax.add_patch(arrow1)
    ax.text(-0.7, 0.6, 'a', ha='center', va='center', fontsize=10, fontweight='bold')
    
    # q0 -> q2 (b) - flecha que termine exactamente en el borde de q2
    start_x = pos_q0[0] + 0.3 * np.cos(np.radians(-30))
    start_y = pos_q0[1] + 0.3 * np.sin(np.radians(-30))
    end_x = pos_q2[0] - 0.3 * np.cos(np.radians(150))
    end_y = pos_q2[1] - 0.3 * np.sin(np.radians(150))
    
    arrow2 = FancyArrowPatch((start_x, start_y), (end_x, end_y),
                            connectionstyle="arc3,rad=-0.1",
                            arrowstyle='->', lw=1.5, color='black', zorder=1)
    ax.add_patch(arrow2)
    ax.text(-0.7, -0.6, 'b', ha='center', va='center', fontsize=10, fontweight='bold')
    
    # q1 -> q1 (self loop) - solo círculo sin flecha adicional
    loop_q1 = plt.Circle((pos_q1[0], pos_q1[1] + 0.6), 0.3, color='none', ec='black', linewidth=1.5, zorder=2)
    ax.add_patch(loop_q1)
    
    # q1 -> q2 (b) - flecha vertical que termine exactamente en el borde de q2
    start_x = pos_q1[0]
    start_y = pos_q1[1] - 0.3
    end_x = pos_q2[0]
    end_y = pos_q2[1] + 0.3
    
    arrow3 = FancyArrowPatch((start_x, start_y), (end_x, end_y),
                            arrowstyle='->', lw=1.5, color='black', zorder=1)
    ax.add_patch(arrow3)
    ax.text(pos_q1[0] + 0.2, 0, 'b', ha='center', va='center', fontsize=10, fontweight='bold')

# Crear la figura
fig, ax = plt.subplots(1, 1, figsize=(8, 6))

# DFA antes de la minimización
draw_dfa_before(ax)
ax.set_xlim(-2.5, 1.5)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axis('off')
ax.set_title('DFA before minimization', fontsize=14, fontweight='bold', pad=20)

# Mostrar la gráfica
plt.tight_layout()
plt.show()

# Información sobre el autómata
print("DFA antes de la minimización:")
print("Estados: q₀ (inicial), q₁, q₂ (aceptación)")
print("Transiciones:")
print("  q₀ --a--> q₁")
print("  q₀ --b--> q₂")
print("  q₁ --a--> q₁")
print("  q₁ --b--> q₂")