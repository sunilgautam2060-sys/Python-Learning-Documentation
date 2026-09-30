


String="kabdfedaeabdc"
n=len(String) #Length Of String.

LeftWindow=0 #Left Window Initialization.

LongestSubstring=0 #Initializing The Longest Substring as 0 At Start.

StartingIndex=0
EndingIndex=0

for RightWindow in range(n): #It Introduce New Character Of String At Window.

    for K in range (LeftWindow , RightWindow):#This Toolbox checks the Introduced Character From Right Side
                   # One by One With All The Element Inside The Window.

         if String[K]==String[RightWindow]:#If equals only than 
              LeftWindow=K+1
              break
                    
            

    if (RightWindow-LeftWindow)+1 > LongestSubstring:# if current window is bigger than maximum window size up to now than replace ,
                                                     #the maximum window with current window for sure.
         
         LongestSubstring=RightWindow-LeftWindow+1 # Size of the window.
         StartingIndex=LeftWindow # it just stores the Start index of the window.
         EndingIndex=RightWindow # it just stores the  End index of the window.

# It prints the longest substring value.
print("The Longest Substring Without Repeting Character is : " , LongestSubstring)          
print(String[StartingIndex:EndingIndex+1])# It prints the longest substring without repeating character.    

