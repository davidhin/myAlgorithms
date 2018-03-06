import mnist_loader
training_data, validation_data, test_data = \
mnist_loader.load_data_wrapper()

import network2

net = network2.Network([784, 30, 10], cost=network2.CrossEntropyCost)
net.SGD(training_data, 30, 10, 0.5,
lmbda = 25,
evaluation_data=validation_data,
monitor_evaluation_accuracy=True
#,
#monitor_evaluation_cost=True,
#monitor_training_accuracy=True,
#monitor_training_cost=True
)

# 5, 10, 15, 20
