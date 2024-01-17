#  Winter break Python Mad libs 
# Create a short mad lib story about your winter break. 
# Your mad lib should include 6 input fields for users to enter data.
# Your mad lib program should prompt the user to enter 2 nouns, 2 verbs, and 2 adjectives. 
# Your mad lib should be written in complete sentences. 
# Once completed, submit your madlib to your github repository by using the source control tool in codespaces. 

def madLib():
    adj_1= input('please enter an adjective')
    adj_2= input('please enter another adjective')
    noun_1= input("please enter a noun ")
    noun_2= input( "please enter another noun ")
    verb_1= input('please enter a verb ')
    verb_2= input('please enter another verb ')

    print(f'My holiday was {adj_1}. I recieve a {noun_1} from my {adj_2} aunt. I also went to {noun_2}. it was a {adj_1} time.')

madLib()