import re
import timeit
import time
def is_simple(x):
    if x == 0:
        return False

    if x<=3:
        return True
    if not x%2:
        return False
    multiplier = 3
    while pow(multiplier,2)<=x:
        if x%multiplier:
            multiplier += 1
            continue
        else:
            return False
    return True

def max_simple1(lst_num):
    lst_sim = list()

    for x in lst_num:
        if is_simple(x):
            lst_sim.append(x)

    return max(lst_sim)

def get_lst_of_complicated(n):
    multiplier = 2
    compl_lst = list()
    for multiplier in range(2, n+1):
        if pow(multiplier, 2) > n:
                break
        for j in range(multiplier*2, n+1, multiplier):
            if not j in compl_lst:
                compl_lst.append(j)

    if not compl_lst:
        return None

    return compl_lst

def max_simple2(lst_num):
    compl_lst = get_lst_of_complicated(max(lst_num))
    return max([x for x in lst_num if not compl_lst.count(x)])

def get_lst_of_simple(n):
        lst_simple = [x for x in range(1,n+1)]
        multiplier = 2

        while pow(multiplier,2) <= n:
            for i in range(multiplier*2,n+1,multiplier):
                if i in lst_simple:
                    lst_simple.remove(i)

            idx = lst_simple.index(multiplier)
            if (idx+1<len(lst_simple)):
                multiplier = lst_simple[idx+1]
            else:
                break
        if not lst_simple:
            return None
        return lst_simple

def max_simple3(lst_num):
    simp_lst = get_lst_of_simple(max(lst_num))
    return max([x for x in lst_num if x in simp_lst])



if __name__ == "__main__":
    data_str = ' jhkjhk 43 49 3511	3539	3541		3557	3559	' \
               '3571 7019		7027	8059	'




    lst_num = [int(x) for x in re.findall(r'[0-9]+',data_str)]
    t1=timeit.timeit()
    max_sim = max_simple1(lst_num)
    tdelta = timeit.timeit() -t1
    print(max_sim, 't_delta = {}'.format(tdelta))

    #use a list of complicated
    t1=timeit.timeit()
    max_sim = max_simple2(lst_num)
    tdelta = timeit.timeit()-t1
    print(max_sim, 't_delta = {}'.format(tdelta))

    # use a list of simple
    t1=timeit.timeit()
    max_sim = max_simple3(lst_num)
    tdelta = timeit.timeit()-t1
    print(max_sim, 't_delta = {}'.format(tdelta))

    #TODO WHY DO NEGATIVE DELTAS APPEAR?
