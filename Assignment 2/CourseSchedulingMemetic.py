from random import randint
from collections import Counter
from copy import deepcopy
import time
from operator import attrgetter


# 1 course in a class at a particular time slot
# 1 course class per week
# 1 professor -> 1 class per day
# 1 professor -> max 2 courses
# professor has at least 1 course


#profs = 6
#courses = 10
#classes = 7
#time = 8

class Gene:

    def __init__(self, p, m, n, t):
        self.p = p
        self.m = m
        self.n = n
        self.t = t


class Chromosome:
    fitness = 0

    def __init__(self, chromosome):
        self.chromosome = chromosome

    def __lt__(self, other):
        return self.fitness < other.fitness


def checkClassFitness(time_slots_set,c):

    k = -1
    for i in range(time_slots_set.__len__()):
        for j in Counter(time_slots_set.__getitem__(i)):
            if Counter(time_slots_set.__getitem__(i)).get(j)>1:
                # print("hello")
                k=1
                break
            if k==1:
                break

    if k==-1:
        c.fitness+=1


def checkProfFitness(prof,c):

    for j in range(6):
        if prof[j] == 1:
            c.fitness += 1


def checkProfCoursesFitness(prof_course, c):

    for i in range(6):
        if 2 > prof_course[i].__len__() > 0:
            # print("hi")
            c.fitness += 1


def checkCourseFitness(courses, c):

    for j in range(6):
        if courses[j] == 1:
            c.fitness += 1


def evaluate_fitness(c):
    courses = [0 for i in range(11)]
    prof_course = [set() for i in range(7)]

    for i in range(5):
        time_slots_set = [[] for i in range(9)]
        prof = [0 for i in range(7)]
        for j in range(8):
            if not (c.chromosome[i][j].p == 0 or c.chromosome[i][j].m == 0 or c.chromosome[i][j].n == 0 or c.chromosome[i][j].t == 0):

                # print(c.chromosome[i][j].p,end=' ')
                # print(c.chromosome[i][j].m, end=' ')
                # print(c.chromosome[i][j].n, end='  ***  ')

                time_slots_set[c.chromosome[i][j].t].append(c.chromosome[i][j].n)
                # print(time_slots_set[c.chromosome[i][j].t])
                prof[c.chromosome[i][j].p] += 1

                courses[c.chromosome[i][j].m] += 1
                if c.chromosome[i][j].m not in prof_course[c.chromosome[i][j].p]:
                    prof_course[c.chromosome[i][j].p].add(c.chromosome[i][j].m)
        # print()


        checkClassFitness(time_slots_set,c)
        checkProfFitness(prof,c)

    checkProfCoursesFitness(prof_course,c)
    checkCourseFitness(courses,c)
    # print("hi "  + str(c.fitness))


def calculateBestChromosomes(chromosome_set):

    return sorted(chromosome_set,reverse=True)

def removeChromosomes(chromosome_set):


    while chromosome_set.__len__()!=10:
        chromosome_set.pop()


    return chromosome_set


def findBestNeighbours(c):


    chromosome_set = []
    chromosome_set.append(c)


    for i in range(5):
        for j in range(8):
            chrom = deepcopy(c.chromosome)
            if c.chromosome[i][j].p==1:
                chrom[i][j].p  = c.chromosome[i][j].p + 1
                d = Chromosome(chrom)
                evaluate_fitness(d)
                chromosome_set.append(d)
            elif c.chromosome[i][j].p==6:
                chrom[i][j].p = c.chromosome[i][j].p - 1
                d = Chromosome(chrom)
                evaluate_fitness(d)
                chromosome_set.append(d)
            else:
                chrom[i][j].p = c.chromosome[i][j].p + 1
                d = Chromosome(chrom)
                evaluate_fitness(d)
                chromosome_set.append(d)

                chrom[i][j].p = c.chromosome[i][j].p - 1
                d = Chromosome(chrom)
                evaluate_fitness(d)
                chromosome_set.append(d)

            chrom = deepcopy(c.chromosome)
            if c.chromosome[i][j].m==1:
                chrom[i][j].m  = c.chromosome[i][j].m + 1
                d = Chromosome(chrom)
                evaluate_fitness(d)
                chromosome_set.append(d)
            elif c.chromosome[i][j].m==10:
                chrom[i][j].m = c.chromosome[i][j].m - 1
                d = Chromosome(chrom)
                evaluate_fitness(d)
                chromosome_set.append(d)
            else:
                chrom[i][j].m = c.chromosome[i][j].m + 1
                d = Chromosome(chrom)
                evaluate_fitness(d)
                chromosome_set.append(d)

                chrom[i][j].m = c.chromosome[i][j].m - 1
                d = Chromosome(chrom)
                evaluate_fitness(d)
                chromosome_set.append(d)

            chrom = deepcopy(c.chromosome)
            if c.chromosome[i][j].t == 1:
                chrom[i][j].t = c.chromosome[i][j].t + 1
                d = Chromosome(chrom)
                evaluate_fitness(d)
                chromosome_set.append(d)
            elif c.chromosome[i][j].t == 8:
                chrom[i][j].t = c.chromosome[i][j].t - 1
                d = Chromosome(chrom)
                evaluate_fitness(d)
                chromosome_set.append(d)
            else:
                chrom[i][j].t = c.chromosome[i][j].t + 1
                d = Chromosome(chrom)
                evaluate_fitness(d)
                chromosome_set.append(d)

                chrom[i][j].t = c.chromosome[i][j].t - 1
                d = Chromosome(chrom)
                evaluate_fitness(d)
                chromosome_set.append(d)

    # for i in chromosome_set:
    #     print(type(i))
    chromosome_set = calculateBestChromosomes(chromosome_set)

    return chromosome_set.pop(0)



def crossoverDays(chromosome_set, temp):

    # print(chromosome_set[0].chromosome[0][1].p, chromosome_set[1].chromosome[0][1].p)
    a = randint(0,9)
    b = randint(0,9)
    chromosome1 = chromosome_set[a].chromosome

    # print(chromosome1[0][1].p, end=' ')
    # print(chromosome1[0][1].m, end=' ')
    # print(chromosome1[0][1].n)
    chromosome2 = chromosome_set[b].chromosome
    # print(chromosome2[0][1].p, end=' ')
    # print(chromosome2[0][1].m, end=' ')
    # print(chromosome2[0][1].n, end='  ***  ')
    c = randint(0,4)
    new_chromosome = Chromosome(chromosome1[:c] + chromosome2[c:])

    evaluate_fitness(new_chromosome)

    new_chromosome = findBestNeighbours(new_chromosome)


    temp.append(new_chromosome)
    # print(a,end=' ')
    # print(b, end=' ')
    # print(c)
    # print("hi" + str(new_chromosome.fitness))

    new_chromosome = Chromosome(chromosome2[:c] + chromosome1[c:])
    evaluate_fitness(new_chromosome)

    new_chromosome = findBestNeighbours(new_chromosome)
    temp.append(new_chromosome)

    return temp


def multiCrossoverDays(chromosome_set, temp):
    a = randint(0, 9)
    b = randint(0, 9)
    chromosome1 = chromosome_set[a].chromosome
    chromosome2 = chromosome_set[b].chromosome
    c = randint(0,4)
    d = randint(0,4)
    while d==c :
        d = randint(0, 4)

    new_chromosome = Chromosome(chromosome1[:c] + chromosome2[c:d] + chromosome1[d:])


    evaluate_fitness(new_chromosome)
    new_chromosome = findBestNeighbours(new_chromosome)
    temp.append(new_chromosome)

    new_chromosome = Chromosome(chromosome2[:c] + chromosome1[c:d] + chromosome2[d:])
    evaluate_fitness(new_chromosome)
    new_chromosome = findBestNeighbours(new_chromosome)
    temp.append(new_chromosome)

    return temp


def mutation(chromosome_set, temp):
    a = randint(0, 9)
    chromosome1 = chromosome_set.__getitem__(a).chromosome
    b = randint(0,39)
    day = int(b/8)
    time = b%8
    while chromosome1[day][time].p == 0:
        b = randint(0, 39)
        day = int(b / 8)
        time = b % 8

    c = randint(1,6)
    chromosome1[day][time].p = c

    new_chromosome = Chromosome(chromosome1)
    evaluate_fitness(new_chromosome)
    new_chromosome = findBestNeighbours(new_chromosome)
    temp.append(new_chromosome)

    return temp





start = time.time()
chromosome_set = []

for k in range(100):
    # courses = [0 for i in range(11)]
    # prof_course = [set() for i in range(7)]

    chromosome = [[Gene(-1, -1, -1, -1) for i in range(8)] for j in range(5)]
    for i in range(5):
        for j in range(8):
            p = randint(0, 6)
            m = randint(0, 10)
            n = randint(0, 7)
            t = randint(0, 8)
            if p==0 or m==0 or n==0 or t==0:
                chromosome[i][j] = Gene(0, 0, 0, 0)
            else:
                chromosome[i][j] = Gene(p, m, n, t)


    # time_slots_set = [[] for i in range(9)]
    # prof = [0 for i in range(7)]
    c = Chromosome(chromosome)

    evaluate_fitness(c)
    chromosome_set.append(c)

    # print(c.chromosome[0][1].p)
    # print("BC")
    # for j in range(chromosome_set.__len__()):
    #     for k in range(5):
    #         for l in range(8):
    #             print(chromosome_set[j].chromosome[k][l].p, end = " ")
    #         print()
    #     print()

for i in range(1000):
    print(i)
    chromosome_set = calculateBestChromosomes(chromosome_set)
    # print("DFDSDSF", chromosome_set[0].chromosome[0][1].p, chromosome_set[4].chromosome[0][1].p, chromosome_set[0].fitness)


    chromosome_set = removeChromosomes(chromosome_set)
    for j in range(chromosome_set.__len__()):
        print("new fitness " + str(chromosome_set.__getitem__(j).fitness))
    print()
    #     print("p: ", chromosome_set.__getitem__(j).chromosome[0][1].n)

    temp = deepcopy(chromosome_set)

    for j in range(20):
        temp = crossoverDays(chromosome_set,temp)

    print("hauujda")

    for j in range(20):
        temp = multiCrossoverDays(chromosome_set, temp)

    print("uwuuw")

    for j in range(10):
        temp = mutation(chromosome_set,temp)

    print("pqpq")

    chromosome_set = temp
    print("new size " + str(chromosome_set.__len__()))

end = time.time()
print("time : " + str(end - start))

