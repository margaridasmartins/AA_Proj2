"""

Project 2 Advanced Algorithmts 2021/22
Margarida Martins

"""

import math
from counters import exact_count
from counters import fixed_probability_count
from counters import decreasing_probability_count

# Save info of the exact counter
def info(count, file):
    file = open(file, "w")
    letter_rank= sorted(count.keys(), key=lambda k : count[k], reverse=True)
    total_count= sum(count.values())
    print("{:^20s} | {:^20} | {:^20}".format("letter", "absolute count", "relative count (%)"))
    print("letter absolute count relative count (%)", file=file)
    for l in letter_rank:
        print("{:^20s} | {:^20d} | {:^20.2f}".format(l,count[l], count[l]/total_count*100))
        print("{:s} {:d} {:.2f}".format(l,count[l], count[l]/total_count*100 ), file=file)
    file.close()


# Save info of the approximated counters
def statistic_info(counter_type, probability, iterations, infile, outfile, convert_count=0):
    avg_count=dict()
    high_count=dict()
    lower_count=dict()
    avg_estimate=dict()
    high_estimate=dict()
    lower_estimate=dict()
    
    for i in range(iterations):
        if counter_type == "F":
            count,estimate = fixed_probability_count(infile, probability)
        else:
            count,estimate= decreasing_probability_count(infile, probability, convert_count)
        for k,v in count.items():
            avg_count[k]= (avg_count.get(k,0)*(i) + v)/(i+1)
            avg_estimate[k]=(avg_estimate.get(k,0)*(i) + estimate[k])/(i+1)
            if (k in high_count and v> high_count[k]) or k not in high_count:
                high_count[k]= v
                high_estimate[k]=estimate[k]
            if (k in lower_count and v< lower_count[k]) or k not in lower_count:
                lower_count[k]= v
                lower_estimate[k]=estimate[k]
    letter_rank= sorted(avg_count.keys(), key=lambda k : avg_count[k], reverse=True)

    with open(outfile, "w") as outfile:
        print("{:^20s} | {:^20} | {:^20} | {:^20} | {:^20} | {:^20} | {:^20} | {:^20} | {:^20}".format("letter", "average estimate",  "relative estimate count (%)", "highest estimated value", "lowest estimated value", "average counter value",  "relative average counter value (%)", "highest counter value", "lowest counter value"))
        print("letter average estimate relative estimate count (%) highest estimated value lowest estimated value average count relative average count (%) highest value lowest value", file=outfile)
        for l in letter_rank:
            print("{:^20s} | {:^20.2f} | {:^20.2f} | {:^20.2f} | {:^20.2f} | {:^20.2f} | {:^20.2f} | {:^20d} | {:^20d}".format(l, avg_estimate[l], avg_estimate[l]/sum(avg_estimate.values())*100, high_estimate[l], lower_estimate[l], avg_count[l], avg_count[l]/sum(avg_count.values())*100, high_count[l], lower_count[l]))
            print("{:s} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:.2f} {:d} {:d}".format(l, avg_estimate[l], avg_estimate[l]/sum(avg_estimate.values())*100, high_estimate[l], lower_estimate[l], avg_count[l], avg_count[l]/sum(avg_count.values())*100, high_count[l], lower_count[l]),file=outfile)

#Don Quixote English edition
print("\n{:^66}\n".format("Don Quixote English"))
info(exact_count("Texts/Don_Quixote/eng.txt"), "Tests/Don_Quixote/eng_exact")
statistic_info("F", 1/64, 20, "Texts/Don_Quixote/eng.txt", "Tests/Don_Quixote/eng_fixed")
statistic_info("D", lambda k : 1/math.pow(math.sqrt(2),k), 20, "Texts/Don_Quixote/eng.txt","Tests/Don_Quixote/eng_decreasing", lambda k : (math.pow(math.sqrt(2),k)-math.sqrt(2)+1)/ (math.sqrt(2)-1))

#Don Quixote Spanish edition
print("\n{:^66}\n".format("Don Quixote Spanish"))
info(exact_count("Texts/Don_Quixote/spa.txt"), "Tests/Don_Quixote/spa_exact")
statistic_info("F", 1/64, 20, "Texts/Don_Quixote/spa.txt", "Tests/Don_Quixote/spa_fixed")
statistic_info("D", lambda k : 1/math.pow(math.sqrt(2),k), 20, "Texts/Don_Quixote/spa.txt","Tests/Don_Quixote/spa_decreasing", lambda k : (math.pow(math.sqrt(2),k)-math.sqrt(2)+1)/ (math.sqrt(2)-1))

#Don Quixote Dutch edition
print("\n{:^66}\n".format("Don Quixote Dutch"))
info(exact_count("Texts/Don_Quixote/deu.txt"), "Tests/Don_Quixote/deu_exact")
statistic_info("F", 1/64, 20, "Texts/Don_Quixote/deu.txt", "Tests/Don_Quixote/deu_fixed")
statistic_info("D", lambda k : 1/math.pow(math.sqrt(2),k), 20, "Texts/Don_Quixote/deu.txt","Tests/Don_Quixote/deu_decreasing", lambda k : (math.pow(math.sqrt(2),k)-math.sqrt(2)+1)/ (math.sqrt(2)-1))

#Don Quixote French edition
print("\n{:^66}\n".format("Don Quixote French"))
info(exact_count("Texts/Don_Quixote/fre.txt"), "Tests/Don_Quixote/fre_exact")
statistic_info("F", 1/64, 20, "Texts/Don_Quixote/fre.txt", "Tests/Don_Quixote/fre_fixed")
statistic_info("D", lambda k : 1/math.pow(math.sqrt(2),k), 20, "Texts/Don_Quixote/fre.txt","Tests/Don_Quixote/fre_decreasing", lambda k : (math.pow(math.sqrt(2),k)-math.sqrt(2)+1)/ (math.sqrt(2)-1))

#Don Quixote Hungarian edition
print("\n{:^66}\n".format("Don Quixote Hungarian"))
info(exact_count("Texts/Don_Quixote/hun.txt"), "Tests/Don_Quixote/hun_exact")
statistic_info("F", 1/64, 20, "Texts/Don_Quixote/hun.txt", "Tests/Don_Quixote/hun_fixed")
statistic_info("D", lambda k : 1/math.pow(math.sqrt(2),k), 20, "Texts/Don_Quixote/hun.txt","Tests/Don_Quixote/hun_decreasing", lambda k : (math.pow(math.sqrt(2),k)-math.sqrt(2)+1)/ (math.sqrt(2)-1))


#Lusiadas Portuguese edition
print("\n{:^66}\n".format("Lusiadas Portuguese"))
statistic_info(exact_count("Texts/lusiadas/por.txt"))
statistic_info(fixed_probability_count("Texts/lusiadas/por.txt",1/64))
statistic_info(decreasing_probability_count("Texts/lusiadas/por.txt",lambda k : 1/math.pow(math.sqrt(2),k)))

#Lusiadas Spanish edition
print("\n{:^66}\n".format("Luisiadas Spanish"))
statistic_info(exact_count("Texts/lusiadas/spa.txt"))
statistic_info(fixed_probability_count("Texts/lusiadas/spa.txt",1/64))
statistic_info(decreasing_probability_count("Texts/lusiadas/spa.txt",lambda k : 1/math.pow(math.sqrt(2),k)))

#Lusiadas English edition
print("\n{:^66}\n".format("Lusiadas English"))
statistic_info(exact_count("Texts/lusiadas/eng.txt"))
statistic_info(fixed_probability_count("Texts/lusiadas/eng.txt",1/64))
statistic_info(decreasing_probability_count("Texts/lusiadas/eng.txt",lambda k : 1/math.pow(math.sqrt(2),k)))




