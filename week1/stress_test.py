import max_pairwise_product_fast
import max_pairwise_product
import random


if __name__ == '__main__':
    n = random.randint(2, 30)
    print(n)
    
    rand_list = random.sample(range(100),n)
    rand_list_chr = [str(x) for x in rand_list]
    print(rand_list)
    print(rand_list_chr)
    print(' '.join(rand_list_chr)+'\n')
    
    
    #answer = max_pairwise_product_fast.max_pairwise_product(input_numbers)
    #print(answer)