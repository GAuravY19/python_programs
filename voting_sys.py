
candidate_1 = input("Enter the candidate 1 name :- ")
candidate_2 = input("Enter the candidate 2 name :- ") 
c1_votes = 0
c2_votes = 0
voters_id = [1,2,3,4,5,6,7,8,9,0]
no_of_votes = len(voters_id)


while True:
    voters = int(input("Enter your voter Id :- "))
    if voters in voters_id:
        print(" Your Identity is confirmed! You're now eligible for voting")
        voters_id.remove(voters) 
    
    else:
        print(" Your Identity is not cofirmed! You're not eligible for voitng")
        break
    
    print(f"To vote for {candidate_1}, press key 1.")
    print(f"To vote for {candidate_2}, press key 2.")
    vote = int(input("Enter Your Valuable Vote :- "))
    
    if vote == 1:
        c1_votes += 1
        print("Thanks for voting...!")
    
    elif vote == 2:
        c2_votes += 1
        print("Thanks for voting...!")
        
    elif vote > 2 or vote == 0:
        print("Your are pressing the wrong key")
        break
    
    if voters_id == []:
        print("Voting session is Over...!")
        break

percent_1 = ((c1_votes) / no_of_votes) * 100  
percent_2 = ((c2_votes) / no_of_votes) * 100 
       
if percent_1 > percent_2:
    print(f"The {candidate_1} won with {percent_1}% votes")

elif percent_1 < percent_2:
    print(f"The {candidate_2} won with {percent_2}% votes")
    