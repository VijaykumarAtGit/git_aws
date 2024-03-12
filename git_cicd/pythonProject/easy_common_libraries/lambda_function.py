import json
from  math_functions import *


# def lambda_handler(event, context):
def lambda_handler():
    num = 100
    print("Square of the number is :-- ", getSquare(num))
    return getSquare(num)


# if __name__ == "__main__":
#     lambda_handler()
