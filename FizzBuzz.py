import numpy as np

def fizzbuzz(x):



    if type(x) is int:


        if x%5 == 0 and x%3 == 0:
             return "FizzBuzz"
        if x%3 == 0:
             return "Fizz"
        elif x%5 == 0:
             return "Buzz"
        else:
             return x

    else:
        new_x = []
        for i in x:
            print (i)
            new = fizzbuzz(i)
            print(new)
            new_x.append(new)

        return new_x



    # else:
    #     new_x = np.zeros(x.shape)

    #     print(new_x)

    #     for i in range(0, x.shape[0]):
    #         if i%5 == 0 and i%3 == 0:
    #              new_x[i] = "FizzBuzz"
    #         if i%3 == 0:
    #              new_x[i] = "Fizz"
    #         elif i%5 == 0:
    #              new_x[i] =  "Buzz"
    #         else:
    #              new_x[i] = i

    # return new_x


if __name__ == '__main__':
     #print("FizzBuzz")
     print(fizzbuzz(7))
     print(fizzbuzz(15))
     print(fizzbuzz(6))
     print(fizzbuzz([1, 15, 66, 27, 90]))
     print(fizzbuzz([9, 4, 1, 5, 1, 8]))