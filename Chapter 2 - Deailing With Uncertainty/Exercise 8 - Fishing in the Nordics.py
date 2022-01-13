countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26] 

def guess(winner_gender):
    if winner_gender == 'female':
        fishers = female_fishers
    else:
        fishers = male_fishers

    # write your solution here
    total_Population = 0
    for i in populations:
        total_Population += i
    fishers_Total = 0
    for i in fishers:
        fishers_Total += i
    j = 0
    temp = (populations[0] / total_Population) * (fishers[0] / populations[0])

    while j < len(populations):
        
        if (populations[j] / total_Population) * (fishers[j] / populations[j]) > temp:
            temp = (populations[j] / total_Population) * (fishers[j] / populations[j])
            guess = countries[j]
            biggest = fishers[j] / fishers_Total * 100
        j+=1
    
    return (guess, biggest)  

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

main()
