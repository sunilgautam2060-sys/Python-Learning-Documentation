
String = "eceba"

Left = 0
MaxLength = 0
Dictionary = {}

for Right in range(len(String)):

    # Add the new character
    if String[Right] not in Dictionary:
        Dictionary[String[Right]] = 1
    else:
        Dictionary[String[Right]] += 1

    # If more than 2 different characters,
    # shrink the window from Left
    while len(Dictionary) > 2:

        Dictionary[String[Left]] -= 1

        if Dictionary[String[Left]] == 0:
            del Dictionary[String[Left]]

        Left += 1

    # Calculate current valid window
    Count = Right - Left + 1

    if Count > MaxLength:
        MaxLength = Count
        Start = Left
        End = Right

print("Longest Substring:", String[Start:End + 1])
print("Length:", MaxLength)

