sensitive_value = list(input('Enter a sensitive value: '))
# print(sensitive_value)
thelength = len(sensitive_value[0:-4])
last_four = sensitive_value[-4::1]
# print(last_four)
# print(thelength)
xlist = list('x' * thelength)
# print(xlist)
xlist.extend(last_four)
print(''.join(xlist))

new_sensitive_value = input('Enter a sensitive value: ')
get_last_four = new_sensitive_value[-4::1]
get_value_length = len(new_sensitive_value[0:-4])
# print(get_value_length)
censored_value = 'x'*get_value_length + get_last_four
print(censored_value)
