standEerste = str(input())

if standEerste == "evenwicht":
    standTweede = str(input())
    if standTweede == "links":
        print('muntstuk #8 is vervalst')
    elif standTweede == "rechts":
        print('muntstuk #7 is vervalst')
    else:
        print('muntstuk #9 is vervalst')

elif standEerste == "links":
    standTweede = str(input())
    if standTweede == "links":
        print('muntstuk #5 is vervalst')
    elif standTweede == "rechts":
        print('muntstuk #4 is vervalst')
    else:
        print('muntstuk #6 is vervalst')

elif standEerste == "rechts":
    standTweede = str(input())
    if standTweede == "links":
        print('muntstuk #2 is vervalst')
    elif standTweede == "rechts":
        print('muntstuk #1 is vervalst')
    else:
        print('muntstuk #3 is vervalst')