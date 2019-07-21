#python3 hungman_1.py

word = input('Player1 Input: ')
word_ = (len(word)*"_")
print("{}: {} characters".format(word_, len(word_)))

corr_times = 0
miss_times = 0
a = ' '
b = ' '
c = ' '
d = ' '
e = ' '
f = ' '  
g = ' '

while (corr_times != len(word) and miss_times != 7):   
 turn_2 = input ('Player2 Input: ')
 if len(turn_2) == 1:
     if turn_2 in word:
         corr_times += 1
         index = word.index(turn_2)
         top_ = word_[0:index]
         middle_ = turn_2
         bottom_ = word_[index+1:]
         word_ = (top_+middle_+bottom_)

         top = word[0:index]
         middle = '_'
         bottom = word[index+1:]
         word = (top+middle+bottom)

     elif turn_2 not in word:
         miss_times += 1
         if miss_times == 1:
             a = '|'
         elif miss_times == 2:
             b = 'O'
         elif miss_times == 3:
             c = '|'
         elif miss_times == 4:
             d = '\\'
         elif miss_times == 5:
             e = '/'
         elif miss_times == 6:
             f = '/'
         elif miss_times == 7:
             g = '\\'
         
     print(word_)    
     print(
             "-----     \n\
|   {0}     \n\
|   {1}     \n\
|  {3}{2}{4}    \n\
|  {5} {6}    \n\
|         ".format(a,b,c,d,e,f,g))
             
 
 else:
     print('Error! Just a character!')

if corr_times == len(word) :
    print("Winner Player 2")
elif miss_times == 7:
    print ("Winner Player 1")