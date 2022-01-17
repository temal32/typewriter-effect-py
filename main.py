import time

print("This is a typewriter demo:") # You can remove this.
lmao = "......." # Put text to type here.
print("Loading", end="") # This is a string that will be printed before the typewriter effect starts, you can remove this.

class type: # Defining class
    def typewriter(text): # creating typewriter function
        return [char for char in text] # Splits string into a list of characters

    global final # Makes the variable to use it outside of the function
    final = typewriter(lmao)

    for x in final: # For loop that prints each character in the list
        print(x, end="") # Remove end tag to print each character on a new line
        time.sleep(0.5) # Timestamp between the next character gets printed out

type.typewriter(lmao)

# sry for my bad english lmao. I am trying my best and I hope you understand the code!
# Social: Temal#5222, https://discord.gg/3zxXCVsumx, https://temal.cf