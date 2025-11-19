from app1 import add, dev, mul,sub 

def test_add():
    x,y=2,3
    res=add(x,y)
    assert res == 5
def test_sub():
    x,y=3,2
    res=sub(x,y)
    assert res ==1
def test_n_sub():   
    x,y=2,3
    res=sub(x,y)
    assert res ==-1 
def test_mul():
    x,y=3,2
    res=mul(x,y)
    assert res==6
def test_n_mul():
    x,y=3,-2
    res=mul(x,y)
    assert res==-6 
def test_dev():
    x,y=4,2
    res=dev(x,y)
    assert res==2
 

    