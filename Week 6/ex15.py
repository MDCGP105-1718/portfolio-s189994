def Word_Frequency (lyrics):
word_list = ['Jellicle', 'Cats', 'are', 'black', 'and', 'white,', 'Jellicle', 'Cats', 'are', 'rather', 'small;', 'Jellicle', 'Cats', 'are', 'merry', 'and', 'bright,', 'And', 'pleasant','to', 'hear', 'when', 'they', 'caterwaul.', 'Jellicle', 'Cats', 'have', 'cheerful', 'faces,', 'Jellicle', 'Cats', 'have', 'bright', 'black', 'eyes;', 'They', 'like', 'to', 'practise', 'their', 'airs', 'and', 'graces', 'And', 'wait', 'for', 'the', 'Jellicle', 'Moon', 'to', 'rise.','']:
 word_counter = {}
 for word in word_list:
         word_counter[word] += 1
     else:
         word_counter[word] = 1
            if word in myDict:
                myDict[word] += 1
            else:
                myDict[word] = 1
            return myDict
list.count(words)

    def to_Chars(lyrics):
        lyrics = lyrics.lower()
        words = ''
        for a in lyrics:
            if a in 'abcdefghijklmnopqrstuvwxyz ':
                words += a
        return words

print (words)
