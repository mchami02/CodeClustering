num_test_phrase = test['Phrase'].size
clean_test_phrase = []
for i in range(0, num_test_phrase):
    if( (i+1)%10000 == 0 ):
        print ("Review %d of %d\
" % ( i+1, num_test_phrase ))
    clean_test_phrase.append(phrase_to_words(test['Phrase'][i]))'