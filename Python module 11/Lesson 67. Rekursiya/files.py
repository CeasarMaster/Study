def file(question, incorrect='Incorrect input, yes or no?', count=3):
    if count == 0:
        return 0
    else:
        print(question)
        n = input()
        if n=='no':
            return 0
        if n=='yes':
            question='Delete file?'
            return file(question,incorrect,count)
        else:
            print(incorrect)
            count-=1
            print(f'Tries: {count}')
            return file(question,incorrect,count)




q = 'Want to exit?'
print(file(q))
