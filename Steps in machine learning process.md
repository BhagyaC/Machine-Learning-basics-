# STEPS
- Data preprocessing : maintaning the data quality of the data
  - Normalisation
- Model
  - Linear regression
  - Logistic regression : a linear function followed with a sigmoid function
  - In some cases the decision boundary will not be linear and then we have to use feature crossing so that the x1, x2 like parameters are used to create more parameters like x1^2 x2^2 and x1*x2
  - Manually doing this kind of task is very risky process and the neural network concepts helps in this (feed forward neural network).
  - In neural network there is a linear summation with a non linear activation function
  ## Loss function in machine learning
  -  Loss function is use to get the model parameter
  - We select the model with lower loss
  - We have actual and predicted label
  - Cross entropy loss - used for binary classification
  - For multiclass classification - categorical cross entropy
  - Cross entropy is a method of calculating the error
 ## Gradient Descent
 - It is an example of optimization function
 - The loss function j(w,b) is defined on the w and the b
 - For each data we have ordered pairs of features and the label 
 - we have a model and the loss as the half of the sum of the squared difference between the model calculated and the output(label)
 -  In a single parameter model the loss function graph will give a contour and each point in the graph will give a line
 - Our objective is that we have to select a model that have a less loss
 - Our learning problem is find w and b such that loss is minimized 
 - Loss j(w,b)
 - y = b+ w1x1
 - Find out w1 such that j() is minimized
 - randomly initialize the weights   
 - Loss calculation
 - calculate the gradient of the loss and move next point where the gradient is smaller (update the wieghts till it converge and the learning rate is constant)
 
  
  
