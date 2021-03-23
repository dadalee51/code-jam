for n in range(1,11):
    for p in range(1,11):
        if n<p:continue
        flip=p//2
        midflip=n//2/2
        print(f'flips:{flip}, midflip:{midflip},number of pages:{n},targetpage:{p}',end='')
        if flip > midflip: #handle even and odd number of pages in a book
            if n%2==1:
                flip=(n-p)//2
            else:
                flip=(n-p+1)//2
        print(f"---endFlip {flip}")
        return flip
