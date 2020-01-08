## Data preperation
- Data can be read from memory and the data can be created from altering the values.
- The data can be readed to the tensorflow variable through
- tf.data.DataSet.from_tensor_slices()
- for modifying the existing dataset then within this function use some tf.random.uniform()
- The final dataset will contain elements with same structure and tf.TypeSpec allow us to understand the structure of the each element
- and also the dateset.element_spec will give a the element component in detail
## Reading input data
- consuming the numpy array
- consuming python generators
- consuming text data
- consuming set of files
## Batching the data elements
- The simplest form of batching stacks n consecutive elements in a dataset to a single element
- Dataset.Batch() exactly perform this with the same constraints as the tf.stack() for each element i it must have a tensor of exactly same size
- we can iterate to the result from the batch function to get the indivitual data set
- If the tensors are with same size the batching will work if the tensors are of different size then the padded tensors are taken for batching
- Dataset.padded_batch() transformation enables you to batch tensors of different size which they may be padded
## Training workflows
- for different epochs we can use a method call repeat where it will repeat the dataset ovet the epochs
- we will bach the data and then repeat for the epoch (the main reason for that is the Dataset.repeat() transformation will concatenates the arguments without signaling the one epoch and beginning of the next epoch
- Because of this the batch function called after the repeat will mix the epoch boundaries
- There is a function called Dataset.shuffle() - it passes the input through the random shuffle queue
- It maintains a fixed sized buffer and chooses the next element uniformly at random from that buffer
- The large buffer size will shuffle more thorougly but it will take a lot of memory (the buffer size is the attribute to the function shuffle())
- Preprocessing the data such that converting all the input into a fixed size and the normalizing will play a big role in training and learning
- we can preprocess the data using tf.py_function() but tensorflow preprocessing methods are convinient
- There are two high level API to use the data preprocessing
- tf.Keras and tf.estimator
