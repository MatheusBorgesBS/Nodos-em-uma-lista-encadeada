from Lista import Lista

def main():
    a = Lista()
    a.add(3)
    a.add(2)
    a.add(45)
    a.add(77)
    a.append(298)
    print("a =",a,'\n')
    print("a[2] retorna", a[2],'\n')
    print("[a[2]] retorna", [a[2]],'\n')
    a[0] = 234
    print("a[0]= 234")
    print("a =",a,'\n')
    print("a.rem() retorna",a.rem())
    2
    print("a =",a,'\n')
    a.insert(9,2)
    print("a.insert(9,2)")
    print("a =",a,'\n')
    print("a.pop() retorna",a.pop())
    print("a =",a,'\n')
    print("a.pop(1) retorna",a.pop(1))
    print("a =",a,'\n')
    print("a.busca(20) retorna",a.busca(20))
    print("a.busca(3) retorna",a.busca(3))

if __name__ ==('__main__'):
    main()