import numpy as np
import matplotlib.pyplot as plt

# AND dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1], [0.5, 0.5], [0.1, 0]])
y = np.array([-1, -1, -1, 1, 1, -1])


# Pure perceptron (learning rate=1, sign activation)
class PurePerceptron:
    def __init__(self, input_dim, n_iters=10):
        self.w = np.zeros(input_dim)
        self.b = 0
        self.n_iters = n_iters

    def fit(self, X, y):
        for _ in range(self.n_iters):
            updates = 0
            for xi, yi in zip(X, y):
                if yi * (np.dot(self.w, xi) + self.b) <= 0:
                    self.w += yi * xi
                    self.b += yi
                    updates += 1
            if updates == 0:
                break

    def predict(self, X):
        return np.sign(np.dot(X, self.w) + self.b)


# Train perceptron
p = PurePerceptron(input_dim=2, n_iters=10)
p.fit(X, y)

# Decision regions
xx, yy = np.meshgrid(np.linspace(-0.1, 1.1, 200), np.linspace(-0.1, 1.1, 200))
grid = np.c_[xx.ravel(), yy.ravel()]
Z = p.predict(grid).reshape(xx.shape)

# Plot
plt.figure(figsize=(6, 6))
# Fill decision regions
plt.contourf(xx, yy, Z, levels=[-1, 0, 1], alpha=0.3)

# Plot training points
for label, marker in zip([-1, 1], ["x", "o"]):
    pts = X[y == label]
    plt.scatter(pts[:, 0], pts[:, 1], marker=marker, s=100, label=f"Class {label}")

plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1.1)
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Perceptron Decision Regions with Training Points")
plt.grid(True)
plt.legend()
plt.gca().set_aspect("equal", adjustable="box")
plt.show()
