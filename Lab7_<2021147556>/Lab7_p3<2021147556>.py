
class not2DError(Exception):
# Error for 1D list
    def __str__(self):
        return '[ERROR]: list is not 2D.'

class unevenListError(Exception):
# Error for uneven list
    def __str__(self):
        return '[ERROR]: inner lists are not same in length.'

class improperMatrixError(Exception):
# Error for incompatible matmul pair
    def __str__(self):
        return '[ERROR]: [a][b]*[c][d] not b==c.'


def mul1d(arr1,arr2):
    # arr1 * arr2
    # [1,2,3] * [4,5,6]
    # return  1*4 + 2*5 + 3*6
    sum = 0
    for i in range(len(arr1)):
        sum+=arr1[i]*arr2[i]
    return sum

class list_D2(list):
    def __init__(self,arr):
        
        ### YOUR CODE HERE ###
        if not isinstance(arr, list):
            raise not2DError()

        for sublist in arr:
            if not isinstance(sublist, list):
                raise  not2DError()

        if len(set(len(sublist) for sublist in arr)) > 1:
            raise unevenListError()

        self.data=arr
        ######

        self.extend(arr)

    def __str__(self):

        ### YOUR CODE HERE ###
        return f"list_2D: {len(self.data)}*{len(self.data[0])}"

        ######

    def transpose(self):

        ### YOUR CODE HERE ###
        transposed = []
        for i in range(len(self.data[0])):
            temp = []
            for j in range(len(self.data)):
                temp.append(self.data[j][i])
            transposed.append(temp)

        return list_D2(transposed)
        
        ######


    def __matmul__(self, others):
        ### YOUR CODE HERE ###
        if len(self.data[0]) != len(others.data):
            raise improperMatrixError()

        result = []
        transposed_other = others.transpose().data
        for row in self.data:
            new_row = []
            for col in transposed_other:
                new_row.append(mul1d(row, col))
            result.append(new_row)

        return list_D2(result)
        ######

    def avg(self):

        ### YOUR CODE HERE ###
        total = 0
        count = 0
        for row in self.data:
            for element in row:
                total += element
                count += 1

        return total / count

        ######
