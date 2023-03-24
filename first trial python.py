# def pyr():
    
#     height=int(input("enter height: "))
#     height+=1
#     for i in range(height):
#         for j in range(height-i):
#             print(" ",end="")
#         for k in range(i):
#             print("#",end="")
      
#         print()


# def double_pyr():
#     height=int(input("enter height: "))
#     height+=1
#     for i in range(height):
#         for j in range(height-i):
#             if j==height-i-1:
#                 print(" ",end="")
#             else:
#                 print(" ",end="")
#         for k in range(i):
#             if k==i-1:
#                 print("#",end="  ")
#             else:
#                 print("#",end="")
        
#         for m in range (i):
#              print("#",end="")
#         print()
#     print()
     
# def main():




# import random
# def change_left(returned):
#     change={
#         "quarters": 0.25,
#         "dimes": 0.10,
#         "nickels":0.05,
#         "pennies":0.01
#     }
#     sum=0
#     count=0
    
#     while True==True:
#         while True==True:
#             sum= sum+ random.choice(list(change.values()))
#             count+=1
#             if(returned==sum):
#                 print(count)
#                 break
      
#         sum=0
#         change_left(returned)
#         break   
       

# def main():
#     returned = float(input("cange owed: "))
#     change_left(returned)   

# main()     







# def change_left(returned):
#     change=[0.25,0.10,0.05,0.01]
#     sum=0
#     count=0
#     i=0
#     while sum!=returned:
#         if sum+change[i]<=returned:
#             sum+=change[i]
#             count+=1
#         else:
#             i+=1
    
#     print(count)

# def main():
#     returned=float(input("change owed: "))
#     change_left(returned)

# main() 







# def sentence():
#     text = input("enter text: ")
#     letters=0
#     for letter in text:
      
#         if letter.isalpha()==True:
#             letters+=1
#     words = text.count(" ")+1
#     sentences = text.count(".")+text.count("?")+text.count("!")
#     grade(letters,words,sentences)


# def grade(letters, words, sentences):
    
#     wordsMul = 100/words
#     avgLetters100=letters*wordsMul
#     avgSentece100=sentences*wordsMul
#     index =  0.0588 * avgLetters100 - 0.296 * avgSentece100 - 15.8
#     if(index<1):
#         print("before grade 1")
#     elif index>16:
#         print("grade 16+")
#     else:
#         index = round(index)
#         print(f"grade {index}")
    

# def main():
#     sentence()

# main()







