def line(data,width,sep='|'):
    '''
    Supporting function to print a line.
        Facilitates design of line
    '''
    
    sep2 = '-' # Default 'margin fill' to [HIPHEN].
    if sep == '|':
        sep2 = ' ' # setting 'margin fill' to [SPACE].
        
    print(sep,end='')
    a = 0
    while a < len(width):
        s = str(data[a])
        left = width[a] - len(s) + 1 # calculating Empty space (margin)
        print(sep2 + s + (sep2 * left) + sep,end='')
        a+=1
    print()


def print_it(data,heads,widths):
    '''
    To print whole table
    '''
    
    if len(data) == 0:
        print('Empty set')
        return
    
    # top border
    d = ['']*len(heads)
    line(d,widths,'+')
    # printing heads
    line(heads,widths)
    # heads bottom border
    d = ['']*len(heads)
    line(d,widths,'+')
    # data
    for a in data:
        line(a,widths)
    # bottom border
    d = ['']*len(heads)
    line(d,widths,'+')
    
    print(len(data),'set.')


def find_width(heads,datas):
    '''
    It Finds width required forone column.
        takes max with of data that the column / field has.
    '''
    
    pool = [] # to store temprary mex width required in all columns.
    
    # taking head value as initial width value.
    for a in heads:
        pool.append(len(a))
    
    # To find max width required in columns
    for x in range(len(pool)):
        for y in datas:
            if len(str(y[x])) > pool[x]:
                pool[x] = len(str(y[x]))
    
    return pool # returning max width required for different columns.


def from_cursor(crx,head):
    '''
    Handle Operation before printing table.
    '''
    
    heads = list(head) # to stop effect on mutable argument.
    col = len(heads)
    width_of_col = []
    data = crx.fetchall()
    
    # to check if all heads are given.
    if len(data[0]) < col:
        # Removing remaining heads.
        heads = heads[:len(data[0])]
    elif len(data[0]) > col:
        heads += (['Null'] * (len(data[0]) - col))
    
    width_of_col = find_width(heads,data)
    
    # Send to print table in display.
    print_it(data,heads,width_of_col)