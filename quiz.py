## QUESTION AND OPTIONS 

questions = [
    ["Besides Sachin Tendulkar, who is the only other Indian cricketer to have scored over 13,000 runs in test cricket?",
    "A. Virat Kohli","B. Sunil Gavaskar","C. VVS laxman","D. Rahul Dravid", "D", 1000],
    
    ["Ranthambore, Sariska and Keoladeo Ghana are all names of what?",
    "A. National Parks","B. Goosebumps","C. Mountains","D. Rivers", "A", 2000],
    
    ["India’s official entry to Oscars 2021, ” Jallikattu” is, a film in which language?",
    "A. Hindi","B. Punjabi","C. Kannada","D. Malayalam", "D", 3000],
    
    ["In terms of production, which of these is the largest train coach manufacturing unit in the world?",
    "A. Integral Coach Factory, Bangalore","B. Integral Coach Factory, Mumbai","C. Integral Coach Factory, Chennai","D. Integral Coach Factory, Kolkata","C", 5000],
    
    ["In 2020, Louise Gluck won the Nobel Prize in which category?",
    "A. Music","B. Sports","C. Literature","D. Dance", "C", 10000],
    
    ["Which of the following companies was originally started as a loom manufacturing unit in 1909?",
    "A. Suzuki","B. CEAT","C. Honda","D. Mercedes", "A", 20000],
    
    ["In 1994, who became the winner of the first-ever Filmfare R D Burman Award for New Music Talent?",
    "A. Udit Narayan","B. A. R. Rahman","C. Lata Mangeshkar","D. Raj Burman", "B", 40000],
    
    ["What colour did Lord Shiva’s throat turn into when he drank the deadly poison during Samudra Manthan?",
    "A. Red","B. Yellow","C. Blue","D. Black", "C", 80000],
    
    ["What is the profession of Kabir in the film Kabir Singh?",
    "A. Engineer","B. Cricketor","C. Athlete","D. Doctor", "D", 160000],
    
    ["Which of these national parks is named after the river that flows through the park?",
    "A. Pench","B. Tadoba","C. Vrindavan","D. Wildera", "A", 320000],
    
    ["Which state is the largest producer of sugarcane in India?",
    "A. Maharashtra","B. Karnataka","C. Madhya Pradesh","D. Uttar Pradesh", "D", 640000],
    
    ["Which of these colors when mixed with red will produce the color orange?",
    "A. Violet","B. Green","C. Orange","D. Yellow", "D", 1250000],
    
    ["Which of these is an ashram set up by Gandhiji set up near Wardha in Maharashtra?",
    "A. Sri Aurobindo Ashram","B. Parmarth Niketan Ashram","C. Sevagram","D. Sivananda Ashram", "C", 5000000],
    
    [" Who of the following personalities is not married to a sports person?",
    "A. Anushka Sharma","B. Sakshi Singh Rawat","C. Mahesh Bhupathi","D. Sharmila Tagore", "C", 10000000],
    
    ["Which part of the plant absorbs water and nutrients from the soil?",
    "A. Stem","B. Buds","C. Leafs","D. Root", "D", 70000000],
    
]


## Main code

print("WARNING :- If at any level you loose the game, you will loose all your money also.")
for i in questions:
    print("Your question is :- ", i[0])
    #options
    print(i[1])
    print(i[2])
    print(i[3])
    print(i[4])
    print("----------------------")
    ans = input("Enter the Option in capital fonts :- ")
    if ans == i[5]:
        print("Your answer is correct.")
        print(f"You won {i[6]} rupees.")
    else:
        print("Your answer is wrong.")
        print("Your take home money is 0.")
        break

    print("   -------------------   -----------------   ------------------     ")
