 ## Mini Batch gradient Descent
 - Only k data points are selected instead of N data points
 - If K = 1 it is called Stochastic gradient descent
 - In mini batch
 - 1. Draw a bunch of k examples (xi,yi)
 - 2. Randomly initialize parameters
 - 3. Repeat until convergence
 - Obtain the predictions from model
 - calculate loss on the batch
 - Calculate gradient of loss w.r.t parameters
 - w new = w old - alpha* gradient
 - Update simultaneously
 ### How do I know if my model is learning
 - Usually learnig curve reach to zero when the iteration increases
 - If the learning rate is small then the convergence is so slow
 - If the learning rate is large converge fastly
 - If the learning rate is too large then it will show a abnormal curve
 - By these evaluation we can understand that the learning rate is too high or not
