def kwargs_test(**kwargs):
    print(kwargs);
    print("First argument is {first}".format(**kwargs));
    print("Second argument is {second}".format(**kwargs));
    print("Third argument is {third}".format(**kwargs));

kwargs_test(first=1, second=2, third=3);