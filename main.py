import prob_calculator
from unittest import main

prob_calculator.random.seed(100)
hat = prob_calculator.Hat(blue=7, red=5, green=7)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"green": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=2000)
print("Probability:", probability)

# Run unit tests automatically
main(module='test_module', exit=False)
