# 📚 Algorithm Documentation

## Overview of Implemented Algorithms

### 1. Preconditioned Conjugate Gradient (PCG) Solver
**Purpose**: Efficiently solve large sparse linear systems Ax = b

**Algorithm**: 
- Uses incomplete Cholesky decomposition as preconditioner
- Achieves O(n√κ) convergence rate where κ is condition number
- Particularly effective for positive definite systems

**Mathematical Foundation**:
```
minimize φ(x) = (1/2)x^T A x - b^T x
```

**Key Features**:
- Memory efficient: O(n) storage
- Robust for ill-conditioned systems
- Adaptive convergence criteria

---

### 2. Newton Descent Method
**Purpose**: Find local minima of twice-differentiable functions

**Algorithm**:
- Uses second-order Taylor approximation
- Requires Hessian matrix computation
- Q-quadratic convergence near solution

**Mathematical Foundation**:
```
x_{k+1} = x_k - H_k^{-1} ∇f(x_k)
where H_k is the Hessian matrix
```

**Convergence Properties**:
- Local q-quadratic convergence
- Requires positive definite Hessian
- Fast convergence in neighborhood of solution

---

### 3. BFGS Quasi-Newton Method
**Purpose**: Approximate Newton method without computing Hessian

**Algorithm**:
- Builds Hessian approximation using gradient information
- Uses rank-2 updates (BFGS formula)
- Maintains positive definiteness

**Mathematical Foundation**:
```
B_{k+1} = B_k + (y_k y_k^T)/(y_k^T s_k) - (B_k s_k s_k^T B_k)/(s_k^T B_k s_k)
where s_k = x_{k+1} - x_k, y_k = ∇f(x_{k+1}) - ∇f(x_k)
```

**Advantages**:
- No Hessian computation required
- Superlinear convergence
- Memory efficient with L-BFGS variant

---

### 4. Wolfe-Powell Line Search
**Purpose**: Find suitable step sizes satisfying strong Wolfe conditions

**Conditions**:
1. **Sufficient Decrease**: f(x + αp) ≤ f(x) + c₁α∇f(x)^T p
2. **Curvature Condition**: |∇f(x + αp)^T p| ≤ c₂|∇f(x)^T p|

**Parameters**: 
- c₁ ∈ (0, 1/2): typically 10⁻⁴
- c₂ ∈ (c₁, 1): typically 0.9

---

### 5. Projected Methods for Box Constraints
**Purpose**: Solve optimization problems with simple bounds

**Constraint Set**: x ∈ [a, b] = {x : aᵢ ≤ xᵢ ≤ bᵢ}

**Projection Operator**:
```
P(x)ᵢ = max(aᵢ, min(xᵢ, bᵢ))
```

**Key Algorithm**: Projected Inexact Newton-CG
- Combines Newton method with CG solver
- Handles active constraints through projection
- Maintains feasibility throughout iterations

---

### 6. Levenberg-Marquardt Algorithm
**Purpose**: Solve non-linear least squares problems

**Problem Formulation**:
```
minimize f(x) = (1/2) Σᵢ rᵢ(x)²
where rᵢ(x) are residual functions
```

**Algorithm Update**:
```
(J^T J + λI) δ = -J^T r
x_{k+1} = x_k + δ
```

**Adaptive Damping**: λ parameter balances between Gauss-Newton and gradient descent

---

### 7. Augmented Lagrangian Method
**Purpose**: Handle equality constraints and box constraints simultaneously

**Augmented Lagrangian**:
```
L_A(x, λ, μ) = f(x) + λ^T h(x) + (μ/2) ||h(x)||²
```

**Algorithm**:
- Alternate between minimizing augmented Lagrangian
- Update multipliers: λ ← λ + μh(x)
- Increase penalty parameter μ when needed

**Convergence**: Achieves superlinear convergence to KKT points
