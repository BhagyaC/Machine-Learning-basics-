# Machine-Learning-basics-

### Gradient descent algorithm.
**Cost function or error function** are the method of calculating how much error that causes occurs in the predictions.
Gradient descetn algorithm is nothing but a way to select the optimized variables which reducec the cost function.

so imagine the variable with a minimal value say 0. then fit it to the cost function and take the derivative(delta). Derivative are nothing but slop which gaves an intution on the direction which way the value should move inorder to optimize.

variable = variable - (alpha * delta). Alph  is the learning parameter.

### Feature scale:
If the values in the data set is of different range then make them to a small scale .It have two advantages one the gradient descent algorithm will work faster and all variables will be in same range.

the general way is that variable = (variable - mean) / range . range = highest value of variable - lowest value.
