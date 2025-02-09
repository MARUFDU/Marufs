
import numpy as np 
import matplotlib.pyplot as plt 
import mpl_toolkits.mplot3d 
import matplotlib.cm as cm 

# Generate grid 
x = np.linspace(-5, 5, 400) 
y = np.linspace(-5, 5, 400) 
X, Y = np.meshgrid(x, y) 
Z = 4 * X**2 + Y**2 

# Plot contour 
levels = [1, 4, 9, 16, 26, 36] 
plt.figure(figsize=(10, 10)) 
contour = plt.contour(X, Y, Z, levels=levels) 
plt.clabel(contour, inline=True, fontsize=8) 
plt.xlabel('x') 
plt.ylabel('y') 
plt.title('Contour plot of $4x^2 + y^2$') 
plt.grid() 
plt.show() 

# from mpl_toolkits.mplot3d import Axes3D 

fig = plt.figure() 
ax = fig.add_subplot(111, projection='3d') 

k_values = [1, 4, 9, 16, 26, 36] 
x = np.linspace(-10, 10, 100) 
y = np.linspace(-10, 10, 100) 
X, Y = np.meshgrid(x, y) 

for k in k_values: 
    Z_upper = np.sqrt(k + X**2 + Y**2) 
    Z_lower = -Z_upper 
    ax.plot_surface(X, Y, Z_upper, alpha=0.3) 
    ax.plot_surface(X, Y, Z_lower, alpha=0.3) 

ax.set_xlabel('x') 
ax.set_ylabel('y') 
ax.set_zlabel('z') 
ax.set_title('Level surfaces of $z^2 - x^2 - y^2 = k$') 
plt.show() 

# First 3D plot 
x = np.linspace(1, 7, 100) 
y = np.linspace(-5, 5, 100) 
X, Y = np.meshgrid(x, y) 
Z1 = Y**2 - 2 * Y * np.cos(X) 

fig = plt.figure() 
ax = fig.add_subplot(121, projection='3d') 
surf = ax.plot_surface(X, Y, Z1, cmap=cm.Blues, linewidth=1, antialiased=False) 
fig.colorbar(surf, shrink=0.5, aspect=5) 
ax.set_title('$f(x, y) = y^2 - 2y \cos x$') 

# Second 3D plot 
x = np.linspace(0, 2*np.pi, 100) 
y = np.linspace(0, 2*np.pi, 100) 
X, Y = np.meshgrid(x, y) 
Z2 = np.abs(np.sin(X) * np.sin(Y)) 

ax = fig.add_subplot(122, projection='3d') 
surf = ax.plot_surface(X, Y, Z2, cmap=cm.coolwarm, linewidth=1, antialiased=False) 
fig.colorbar(surf, shrink=0.5, aspect=5) 
ax.set_title('$f(x, y) = |\sin x \sin y|$') 
plt.show() 

x = np.linspace(-2, 2, 100) 
y = np.linspace(-2, 2, 100) 
X, Y = np.meshgrid(x, y) 
Z = 4 * X * Y - X**4 - Y**4 

fig = plt.figure() 
ax = fig.add_subplot(121, projection='3d') 
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm) 
ax.set_title('$f(x, y) = 4xy - x^4 - y^4$') 

x = np.linspace(-2, 2, 100) 
y = np.linspace(-1, 1, 100)  # Adjusted to avoid overflow 
X, Y = np.meshgrid(x, y) 
Z = 4 * X**2 * np.exp(Y) - 2 * X**4 - np.exp(4 * Y) 

ax = fig.add_subplot(122, projection='3d') 
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm) 
ax.set_title('$f(x, y) = 4x^2 e^y - 2x^4 - e^{4y}$') 
plt.show()
