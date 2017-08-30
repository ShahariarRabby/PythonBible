cinema = {
    #Key = Movie name
    #Value[0] = Age
    #Value[1] = Sits
    'FF8'.upper(): [8, 2],
    'Spider Man 2'.upper(): [8, 5],
    'Fifty Shades of Gray'.upper(): [18, 5]
}
print 'Available Cinema are:', cinema.keys()


while True:
    name = raw_input('Enter a cinema name: ').upper()

    for l in cinema.keys():

        if l == name:

            if cinema[name][1] > 0:

                if int(raw_input('What is your age?')) >= cinema[name][0]:
                    cinema[name][1] = cinema[name][1] - 1
                    print 'Enjoy The Film'
                    break

                else:
                    print 'You are not allowed to enjoy the film'
                    break

            else:
                print 'Sorry no sit available'
                break

    else:
        print 'Sorry!! Movie Not Found'
