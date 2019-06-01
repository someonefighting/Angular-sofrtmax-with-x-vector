dict_label = {}
dict_pred = {}
acc = 0
total = 0
cut = 0
decode_list = []
cut_num = 0
with open('index', 'r') as f:
    list1 = f.readlines()
    for i in range(0, len(list1)):
        list1[i] = list1[i].strip('\n')
        list1[i] = list1[i].strip(']')
        ll = list1[i].split("[")
        #ll = list1[i].split(' ', 1 ); 
        predstr = ll[1].strip().split(" ")
        pred = [str(i) for i in predstr]
        pred = list(map(int, pred))
        #l = eval(ll[1])
        #print(ll[0])
        #print(pred.count(-1))
        ll[0]=ll[0].strip()
        print(ll[0],"a")
        dict_pred[ll[0]] = pred
      
with open('all_test_labels', 'r') as f:
    list1 = f.readlines()
    for i in range(0, len(list1)):
        list1[i] = list1[i].strip('\n')
        #list1[i] = list1[i].strip(']')
        #ll = list1[i].split("[")
        ll = list1[i].split(' ', 1 ); 
        predstr = ll[1].strip().split(" ")
        pred = [str(i) for i in predstr]
        pred = list(map(int, pred))
        predlist = pred
        #predlist = [val for val in pred for i in range(5)]
        #l = eval(ll[1])
        #print(ll[0])
        #print(predlist.count(1))
        print(ll[0],"a")        
        dict_label[ll[0]] = predlist

with open('WakeuponlyFileName.txt', 'r') as f:
    list1 = f.readlines()
    for i in range(0, len(list1)):
        list1[i] = list1[i].strip('\n')
        print(list1[i],"a")
        decode_list.append(list1[i])
        
for key in decode_list:
    #print(key)
    if key in dict_label:
        print(key)
        print(dict_label[key])
        print(dict_pred[key])
        if len(dict_label[key])==len(dict_pred[key]):
            print(key)
            c = [dict_pred[key][i] - dict_label[key][i] for i in range(len(dict_label[key]))]
            acc += c.count(c==0)
            num = len(dict_label[key])
            cut = dict_pred[key].count(-1)
            cut_num += cut
            total += num-cut
    
print(acc)
print(total)
print(cut_num)
         