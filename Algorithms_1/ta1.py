mylist=[]
menu='''1. 이름 추가
2. 이름 삭제
3. 이름 수정
4. 종료'''



while True:
    print(menu)
    choice=int(input('메뉴 선택 : '))
    if choice==1:
        name=input('이름 : ')
        if name in mylist:
            print('이미 있는 이름')
        else:
            mylist.append(name)
        print(mylist)

    elif choice==2:
        name=input('이름 : ')
        if name in mylist:
            mylist.remove(name)
            print(mylist)
        else:
            print('해당 이름 없음')

    elif choice==3:
        name=input('이름 : ')
        if name in mylist:
            mylist.remove(name)
            new=input('새 이름 : ')
            mylist.append(new)
            print(mylist)
        else:
            print('해당 이름 없음')
    elif choice==4:
        break
    else:
        print("다시 입력하세요")