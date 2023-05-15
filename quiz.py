'''

DESCRIPTION:- In this program I have tried to make a
simple quiz game almost similar to KBC model.
'''


question=[
['Besides Sachin Tendulkar, who is the only other Indian cricketer to have scored over 13,000 runs in test cricket?',
'Virat Kohli','Sunil Gavaskar','VVS laxman','Rahul Dravid',4],

['Ranthambore, Sariska and Keoladeo Ghana are all names of what?',
 'National Parks','Goosebumps','Mountains','Rivers',1],

[ 'India’s official entry to Oscars 2021, ” Jallikattu” is, a film in which language?',
 'Hindi','Punjabi' ,'Kannada','Malayalam',4],

[ 'In terms of production, which of these is the largest train coach manufacturing unit in the world?',
 'Integral Coach Factory, Bangalore','Integral Coach Factory, Mumbai','Integral Coach Factory, Chennai', 'Integral Coach Factory, Kolkata',3],

['In 2020, Louise Gluck won the Nobel Prize in which category?',
 'Music', 'Sports' ,'Literature','Dance',3],

['Which of the following companies was originally started as a loom manufacturing unit in 1909?',
 'Suzuki','CEAT','Honda','Mercedes',1],

['In 1994, who became the winner of the first-ever Filmfare R D Burman Award for New Music Talent?',
 'udit Narayan','A. R. Rahman','Lata Mangeshkar','Raj Burman',2],

['What colour did Lord Shiva’s throat turn into when he drank the deadly poison during Samudra Manthan?',
 'Red','Yellow','Blue','Black',3],

['What is the profession of Kabir in the film Kabir Singh?'
 ,'Engineer','Cricketor','Athlete', 'Doctor',4],

['Which of these national parks is named after the river that flows through the park?'
 ,'Pench','Tadoba','Vrindavan','Wildera',1],

['Which state is the largest producer of sugarcane in India?','Maharashtra' ,'Karnataka',
'Madhya Pradesh','Uttar Pradesh',4],

[ 'Which of t   hese colors when mixed with red will produce the color orange?'
 ,'Violet','Green','Orange','Yellow',4],

['Which of these is an ashram set up by Gandhiji set up near Wardha in Maharashtra?'
 ,'Sri Aurobindo Ashram','Parmarth Niketan Ashram','Sevagram','Sivananda Ashram',3],

['Who of the following personalities is not married to a sports person?'
 ,'Anushka Sharma','Sakshi Singh Rawat' ,'Mahesh Bhupathi','Sharmila Tagore',3],

['Which part of the plant absorbs water and nutrients from the soil?',
'Stem','Buds', 'Leafs','Root',4]
]

level=[1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money=0

for i in range(0, len(question)):
    ques=question[i]
    print(f"your question is for rupees{level[i]}")
    print(ques[i])
    print("a.",ques[1])
    print("b.",ques[2])
    print("c.",ques[3])
    print("d.",ques[4])
    reply=int(input("enter the number of the correct option"))
    if reply==0:
        print("your quit the game")
        break
    if reply==ques[5]:
        print("correct answer, you won Rs.",level[i])
        if i==4:
            money=10000
        elif i==9:
            money=320000
        elif i==14:
            money=5000000
    else:
        print("you lost ")
        break
        
    
    
print("your take home money is",money)
