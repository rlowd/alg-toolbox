import max_pairwise_product_fast
import max_pairwise_product
import random

def stress_test(N,M):
    
    while True:
            n = random.randint(2, N) 
            print(n)

            rand_list = random.sample(range(M),n)
            #rand_list_chr = [x for x in rand_list]
            #print(rand_list)
            #print(rand_list_chr)
            #print(' '.join(rand_list_chr)+'\n')
            input_numbers = rand_list


            res1 = max_pairwise_product.max_pairwise_product(input_numbers)
            print(res1)
            res2 = max_pairwise_product_fast.max_pairwise_product(input_numbers)
            print(res2)

            if(res1 != res2 ):
                print('Wrong answer: {} {}'.format(res1, res2))
                break
            else:
                print('OK')


if __name__ == '__main__':
    N = int(input())
    M = int(input())
    stress_test(N,M)
    