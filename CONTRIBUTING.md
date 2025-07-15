# 🤝 Contributing to Optimization Methods Implementation

Thank you for your interest in contributing to this advanced optimization algorithms repository! This document provides guidelines for contributing to ensure code quality and consistency.

## 📋 Table of Contents
- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation Requirements](#documentation-requirements)
- [Submission Process](#submission-process)

## 🌟 Code of Conduct
This project adheres to academic and professional standards. Please ensure:
- Respectful and constructive communication
- Focus on technical merit and scientific accuracy
- Proper attribution of algorithms and references
- Commitment to reproducible research

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- NumPy >= 1.19.0
- Basic understanding of numerical optimization
- Familiarity with linear algebra and calculus

### Development Environment
```bash
# Fork and clone the repository
git clone https://github.com/yourusername/optimization_methods_implementation.git
cd optimization_methods_implementation

# Create development branch
git checkout -b feature/your-feature-name

# Set up virtual environment
python -m venv dev-env
source dev-env/bin/activate  # Windows: dev-env\Scripts\activate

# Install development dependencies
pip install numpy
```

## 💻 Development Setup

### Project Structure
```
├── src/                    # Algorithm implementations
│   ├── 1.Setup and Initial Implementations/
│   ├── 2.Preconditioned Conjugate Gradient Solver and Newton Descent/
│   ├── 3.Wolfe-Powell Search and BFGS Descent/
│   ├── 4.Projected Methods/
│   ├── 5.Levenberg-Marquardt Descent/
│   └── 6.Augmented Lagrangian Methods/
├── tests/                  # Test suites
├── docs/                   # Documentation
└── README.md
```

## 📝 Coding Standards

### Python Style Guidelines
- Follow PEP 8 with 100-character line limit
- Use descriptive variable names (prefer `gradient` over `g`)
- Include type hints for function parameters and returns
- Use NumPy docstring format

### Example Function Template
```python
import numpy as np

def newton_descent(objective, x0: np.array, eps: float = 1.0e-3, 
                   verbose: int = 0) -> np.array:
    """
    Implement Newton descent for unconstrained optimization.
    
    Parameters
    ----------
    objective : object
        Objective function with methods .objective(), .gradient(), .hessian()
    x0 : np.array
        Initial point (column vector in R^n)
    eps : float, optional
        Tolerance for termination (default: 1.0e-3)
    verbose : int, optional
        Verbosity level (default: 0)
        
    Returns
    -------
    np.array
        Optimal point x* such that ||∇f(x*)|| <= eps
        
    Raises
    ------
    TypeError
        If eps <= 0 or input dimensions are incorrect
        
    Examples
    --------
    >>> obj = QuadraticObjective(A, b, c)
    >>> x0 = np.array([[1.0], [2.0]])
    >>> xmin = newton_descent(obj, x0, eps=1.0e-6)
    """
    # Implementation with proper error checking
    if eps <= 0:
        raise TypeError('Tolerance eps must be positive!')
    
    # Algorithm implementation...
    return x_optimal
```

### Mathematical Notation
- Use clear variable names reflecting mathematical meaning
- Include algorithm references in comments
- Document convergence properties and complexity

## 🧪 Testing Guidelines

### Test Structure
Each algorithm must include:
1. **Unit Tests**: Test individual components
2. **Integration Tests**: Test complete algorithm flow
3. **Benchmark Tests**: Validate against known solutions
4. **Performance Tests**: Measure convergence rates

### Test Example
```python
def test_newton_descent_quadratic():
    """Test Newton descent on quadratic function."""
    # Setup quadratic f(x) = 0.5 * x^T * A * x - b^T * x + c
    A = np.array([[4, 1], [1, 3]], dtype=float)
    b = np.array([[1], [2]], dtype=float)
    c = 0.0
    
    objective = QuadraticObjective(A, b, c)
    x0 = np.array([[10], [10]], dtype=float)
    
    # Run algorithm
    xmin = newton_descent(objective, x0, eps=1.0e-10)
    
    # Verify solution
    expected = np.linalg.solve(A, b)
    np.testing.assert_allclose(xmin, expected, atol=1.0e-8)
    
    # Verify optimality
    gradient_norm = np.linalg.norm(objective.gradient(xmin))
    assert gradient_norm < 1.0e-8
```

### Performance Benchmarks
Include timing and convergence analysis:
```python
def test_algorithm_performance():
    """Benchmark algorithm performance."""
    # Test problem setup
    times = []
    iterations = []
    
    for n in [10, 50, 100, 200]:
        # Generate test problem of size n
        start_time = time.time()
        result = algorithm(problem, x0)
        elapsed = time.time() - start_time
        
        times.append(elapsed)
        iterations.append(result.num_iterations)
    
    # Verify expected scaling
    assert all(it < 50 for it in iterations)  # Convergence check
```

## 📚 Documentation Requirements

### Algorithm Documentation
Each new algorithm must include:

1. **Mathematical Foundation**
   - Problem formulation
   - Algorithm description
   - Convergence theory
   - Complexity analysis

2. **Implementation Notes**
   - Key design decisions
   - Numerical considerations
   - Parameter selection guidelines

3. **Usage Examples**
   - Basic usage
   - Advanced configurations
   - Common pitfalls

### Docstring Requirements
```python
def algorithm_name(params) -> return_type:
    """
    Brief one-line description.
    
    Detailed description explaining the algorithm's purpose,
    mathematical background, and key features.
    
    Algorithm Reference
    -------------------
    Algorithm X.Y from "Numerical Optimization" by Nocedal & Wright
    or appropriate academic reference.
    
    Parameters
    ----------
    param1 : type
        Description with mathematical notation if applicable
        
    Returns
    -------
    type
        Description of return value
        
    Notes
    -----
    Convergence properties, computational complexity,
    and important implementation details.
    
    Examples
    --------
    >>> # Basic usage example
    >>> result = algorithm_name(input_data)
    """
```

## 🔄 Submission Process

### Before Submitting
1. **Run all tests**: `python -m pytest tests/`
2. **Check code style**: Ensure PEP 8 compliance
3. **Update documentation**: Include algorithm description
4. **Add benchmarks**: Performance and accuracy tests
5. **Verify examples**: Ensure all examples work

### Pull Request Template
```markdown
## Description
Brief description of the changes and motivation.

## Algorithm Details
- **Type**: [Newton Method/Quasi-Newton/Line Search/etc.]
- **Convergence Rate**: [Linear/Superlinear/Quadratic]
- **Computational Complexity**: [Per iteration cost]
- **Memory Requirements**: [Storage complexity]

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Benchmark tests included
- [ ] Performance analysis provided

## Documentation
- [ ] Algorithm description added
- [ ] Usage examples included
- [ ] Mathematical background documented
- [ ] References cited

## Checklist
- [ ] Code follows project style guidelines
- [ ] Tests cover new functionality
- [ ] Documentation is complete
- [ ] No breaking changes to existing APIs
```

### Review Process
1. **Automated Checks**: Style, tests, documentation
2. **Technical Review**: Algorithm correctness and efficiency
3. **Performance Review**: Benchmarks and scaling analysis
4. **Integration Testing**: Compatibility with existing code

## 🆘 Getting Help

### Resources
- **Algorithm Reference**: Nocedal & Wright "Numerical Optimization"
- **NumPy Documentation**: https://numpy.org/doc/
- **Project Discussions**: GitHub Issues and Discussions

### Common Issues
- **Convergence Problems**: Check algorithm parameters and initial conditions
- **Numerical Stability**: Review conditioning and scaling
- **Performance Issues**: Profile code and optimize bottlenecks

### Contact
For questions or guidance:
- Open a GitHub issue with the `question` label
- Reference specific algorithms or implementation details
- Provide minimal reproducible examples

---

Thank you for contributing to advancing numerical optimization methods! 🚀
