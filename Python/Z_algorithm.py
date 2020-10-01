def z_algo(text, pattern):
    List = []
    substring = ""

    for text_index in range(0, len(text) - len(pattern)+1):

        substring = text[text_index:text_index + len(pattern)]

        count = 0
        for substring_index in range(0, len(pattern)):

            if substring[substring_index] == pattern[substring_index]:
                count += 1

        if count == len(pattern):
            List.append(text_index)
    return List

if __name__ == '__main__':
    text = input("Enter Text : ")
    pattern = input("Enter pattern : ")
    
    positions = z_algo(text, pattern)

    if len(positions) != 0:
        for position in positions:
            print("The pattern is present at : " + str(position))

    else:
        print("Pattern Not Found !!!")

#Text: ababaa
#Pattern: aba
#Returns found pattern at index 0 and 2.