class big_O:

    values = [1,2,3,4,5,6,7,8,9,10]

    def func_constant(self):
        print("INSIDE BIG-O CONSTANT")
        print(self.values)

    def func_linear(self):
        print("INSIDE BIG-O LINEAR")
        for v in self.values:
            print(v)  


if __name__ == '__main__':
    big = big_O()
    big.func_constant()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    big.func_linear()
