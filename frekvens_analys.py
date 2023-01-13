#1. Hur mycket tid trodde du att det skulle ta att lösa den här uppgiften?
#Cirka 24 h
#2. Hur mycket tid har du lagt ned på att lösa uppgiften?
#Löste själva uppgiften på kanske 16 h, men 'buggtesting' och att fixa koden så den klarar testet tog kanske extra 10 h, så tot 26 h
"""
Olivers Frekvens Analys
"""

def frequency(filnamn):
    filnamn = open(filnamn)
    filnamn = filnamn.read()
    filnamn = filnamn.lower()
    #filnamn.close()
    freq_dict = {}
    lst = filnamn.split()
    for word in lst:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    # sorted_freq_dict = sorted(freq_dict.items(),key=lambda x: x[1], reverse=True)
    # print(sorted_freq_dict)
    #print(freq_dict)
    return freq_dict

def most_frequent(freq_dict):
    sorted_freq_dict = sorted(freq_dict.items(),key=lambda x: x[1], reverse=True)[:10] #lambda?
    top_dict = dict(sorted_freq_dict)
    
    return top_dict

def word_count(freq_dict):
    lenght_count = sum(freq_dict.values())
    #print("Totalt", lenght_count, "ord")

    return lenght_count

def unique_words(freq_dict):
    lenght_unique = len(freq_dict)
    #print("Totalt", lenght_unique, "unika ord")

    return lenght_unique

def mean_frequency(freq_dict):
    mean_value = sum(freq_dict.values())/(len(freq_dict))
    return mean_value

def median_frequency(freq_dict):
  
  my_list = []
  result = sorted(freq_dict.items(), key=lambda x: x[1])
  
  for word, number in result:
    my_list.append(number)
  
  size = len(my_list)
  median_value = 0
  
  if size % 2 == 0:
    index = size / 2
    index = int(index)
    index1 = index - 1
    median_value = (my_list[index1] + my_list[index])/2

  else:
    index = size // 2
    median_value = my_list[index]
  return median_value

def closest_word(freq_dict, rate):
  
  my_list = []
  result = sorted(freq_dict.items(), key=lambda x: x[1])
  
  for word, number in result:
    my_list.append(number)
    
  final_result = my_list[min(range(len(my_list)), key = lambda i: abs(my_list[i]-rate))] #https://stackoverflow.com/questions/7934547/python-find-closest-key-in-a-dictionary-from-the-given-input-key/22997000
  print("closest result: ", final_result)                                                #är använd men verifierad
#  Vad koden gör mellan my_list är att den returnerar positionen på värdet som är närmst.
# Lamdba funktionen skapar en list på skillnaden mellan my_list[i] och rate. dvs 
# {my_list[0]-rate, my_list[1]-rate, ...}

# sedan vad min()-funktionen gör är att den returnerar positionen på önskade värdet. I andra ord så plockar den det minsta värdet
# i listan dvs positionen på vårt önskade värde.
  return list(freq_dict.keys())[list(freq_dict.values()).index(final_result)]

    
def main():
    filnamn = str(input("Skriv din textfil: "))

    freq_dict = frequency(filnamn)
    print("\n---------------------------------------")
    print("Här är de 10 vanligaste orden i filen i fallande ordning.")
    print("\nOrd            Antal förekomster")
    print("---------------------------------------")
    for item, amount in most_frequent(freq_dict).items(): #https://stackoverflow.com/questions/44689546/how-to-print-out-a-dictionary-nicely-in-python/44689627
        
        print(f"{item:<4s}      |       {amount:>4}")

    print("---------------------------------------\n")
    print("Antalet ord: ", word_count(freq_dict))
    print("Unika ord:",unique_words(freq_dict))
    print("Medelvärdet är: ", mean_frequency(freq_dict))
    rate = mean_frequency(freq_dict)
    print("Medianen är: ", median_frequency(freq_dict))
    print("Ordet närmast är: ", closest_word(freq_dict, rate))
  

if __name__ == "__main__":
    main()

