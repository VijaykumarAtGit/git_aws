import json
import numpy as np


def lambda_handler(event, context):
# def lambda_handler():
    origMatrix = [[1,2],[3,4]]
    print("Original Matrix is :-- \n", origMatrix)
    tranposeMatrix = np.transpose(origMatrix)
    print("Transposed Matrix is :-- \n", tranposeMatrix)

# if __name__ == "__main__":
#     lambda_handler()
