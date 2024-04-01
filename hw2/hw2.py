"(hello world)"
n1, n2 = 10, 20
print(n1 > n2)
print(n1 >= n2)
print(n1 < n2)
print(n1 <= n2)
print(n1 == n2)
print(n1 != n2)
print(1 == 1 and 3 == 3)
print(1 == 1 and 2 == 3)

#hours = int(input("Enter Hours: "))
#if hours >= 12:
    #print("PM")
    #print("kggy")
#else:
    #print("AM")

    #2
#if 12 <= hours < 24:
    #print("PM")
#elif 0 <= hours < 12:
    #print("AM")
#else:
    #print("Incorrect hours!")
film_rating = int(input("Enter Film Rating: "))
if film_rating >0 and film_rating <= 5:
    if film_rating == 4 or film_rating == 5:
        print("Ok")
    else:
        print("Not Ok")
else:
    print("incorrect rating")



