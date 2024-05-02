class table:
    '''this class prints a dictionary in a table format for example check demo_table.py'''
    def __init__(self,data):
        self.data=data
        for da in self.data:
            for kis,v in da.items():
                da[kis]=str(v)

    def print_table(self):
        self.string=""
        
        self.find_no_keys()
        self.for_all_cols()
        self.pr_heading()
        self.pr_dash()
        self.pr_row()


    def find_no_keys(self):
        '''finds the number of keys in dictionary'''
        
        self.no_keys=len(self.data[0])
        return self.no_keys
    
    def max_len_col(self,key):
        self.max_length=len(self.data[0][key])
        for i in self.data:
            if self.max_length<len(i[key]):
                self.max_length=len(i[key])
        
        if len(key)>self.max_length:
            self.max_length=len(key)
        return self.max_length+4
    
    def for_all_cols(self):
        self.max=[]
        for k in self.data[0].keys():
            a=self.max_len_col(k)
            self.max.append(a)
        return self.max
    
    def pr_heading(self):
        for a,q in enumerate(self.data[0].keys()):
            print(q,end=" "*(self.max[a]-len(q)))
        print('')

    def pr_dash(self):
        for el in self.max:
            print('-'*(el-1),end=' ')
        print('')

    def pr_row(self):
        for t in self.data:
            for indx,value in enumerate(t.values()):
                print(value,end=' '*(self.max[indx]-len(value)))
            print('')

