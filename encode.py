# Unicode the You Text

User = input('You want to encode your text (yes or no):')
if User.lower() == 'yes':
    def Unicode():
        emty_List = []
        User =  input('Type Your Text:')
        for i in User:
            emty_List.append(str(ord(i)))
        print(f'The unicode => {emty_List}')
        return ','.join(emty_List)
    
    result = Unicode()
    
    User = input('You want to convert the text converted to code back to text (yes or no):')
    if User.lower() == 'yes':
        def Un_unicode(Text):
            empty_List = []
            for i in Text.split(','):
                empty_List.append(chr(int(i)))
            print(f'The Un Unicode => {empty_List}')
            return ''.join(empty_List)

        print(Un_unicode(result))
    else:
        print('Bay')
else:
    print('''Note: You must do a few things to use the program:
    1 - Your internal value must not be anything other than yes and no
    2 - Your second internal value must not be empty''')
    print('Bay')
