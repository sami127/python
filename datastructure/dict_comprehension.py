
state = ['Telangana', 'Maharashtra', 'Rajasthan']
capital = ['Hydrabad', 'Mumbai', 'Jaipur']

output_dict = {}

# {state:capital}

for (k,v) in zip(state,capital):
    output_dict[k] = v

print(output_dict)

dict_using_comp = {k:v for k,v in zip(state,capital)}
print(dict_using_comp)