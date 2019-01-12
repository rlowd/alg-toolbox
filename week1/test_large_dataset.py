import max_pairwise_product_fast

input_numbers = [x for x in range(1, (2*10**5)+1)]
print(input_numbers[0:3])
print(input_numbers[len(input_numbers)-2:len(input_numbers)])

if __name__ == '__main__':
    answer = max_pairwise_product_fast.max_pairwise_product(input_numbers)
    print(answer)