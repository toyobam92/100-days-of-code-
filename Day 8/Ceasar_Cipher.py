import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def caesar(start_text, shift_amount, cipher_direction):
      cipher_list = []
      for i in start_text:
        cipher_list.append("_")
      

      end_text = ""
      if cipher_direction == "decode":
        shift_amount *= -1
      for charx in range(len(start_text)):
        if start_text[charx] not in alphabet:
        #TODO-3: What happens if the user enters a number/symbol/space?
        #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"
          wrong_value = start_text[charx]
          cipher_list[charx] = wrong_value
        else:
          position = alphabet.index(start_text[charx])
          new_position = position + shift_amount
          cipher_list[charx] = alphabet[new_position]
      
      for i in cipher_list:
        end_text += i
        
      print(f"Here's the {cipher_direction}d result: {end_text}")

     #   game_on = False
    #print("Good bye")
    
    #val = input(f" Type yes if you want to go again. #Otherwise type no") 

    #if val == 'yes':
     # game_on = True
    #else:
      #game_on = False
      #print("Good bye")

#TODO-1: Import and print the logo from art.py when the program starts.

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a new function that calls itself if they type 'yes'. 
game_on = True
while game_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
    #Try running the program and entering a shift number of 45.
    #Hint: Think about how you can use the modulus (%).

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    
    val = input(f" Type yes if you want to go again. Otherwise type no\n") 

    if val == 'yes':
      game_on = True   
    else:
      game_on = False
      print("Goodbye!")
