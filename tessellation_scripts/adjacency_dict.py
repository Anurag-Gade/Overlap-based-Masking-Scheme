def check_for_adjacency(my_dict):
    adj_dict = {} 
    for i in range(1,len(my_dict)+1):
        for j in range(i,len(my_dict)+1):
            key = i
            adj_dict.setdefault(key,[]) 
            if(my_dict[i][0] == my_dict[j][0] and my_dict[i][1] == my_dict[j][1]):
                if(i != j):
                    adj_dict[key].append(j)
            if(my_dict[i][0] == my_dict[j][0] and my_dict[i][2] == my_dict[j][2]):
                if(i != j):
                    adj_dict[key].append(j)
            if(my_dict[i][1] == my_dict[j][1] and my_dict[i][2] == my_dict[j][2]):
                if(i != j):
                    adj_dict[key].append(j)
    
    return adj_dict
