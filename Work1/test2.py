def process_string(s):

    reversed_s = ""
    for ch in s:
        reversed_s = ch + reversed_s

    upper_s = reversed_s.upper()
    lower_s = reversed_s.lower()

    return (upper_s, lower_s)

print(process_string("hello"))
