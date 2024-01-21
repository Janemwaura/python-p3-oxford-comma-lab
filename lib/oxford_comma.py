def oxford_comma(words):
    if len(words) == 0:
        return ""

    if len(words) == 1:
        return words[0]

    if len(words) == 2:
        return f"{words[0]} and {words[1]}"
    
    result = ", ".join(words[:-1]) + f", and {words[-1]}"

    return result


word_list = ["Jane", "oli", "ruth", "george"]
result_string = oxford_comma(word_list)
print(result_string)
