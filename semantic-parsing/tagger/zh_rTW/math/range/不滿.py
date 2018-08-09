from tagger.math.range._lt_postrange import _LtPostrange

class 不滿(_LtPostrange): # TBD/TODO, 複合修飾詞
    '''
     - 不滿一萬
     - 不滿萬元者，以萬元計算
     - 金額不滿1千元的消費
     
    @since 2018.08.07
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_list(self):
        return ['不滿']
    # end-of-def
    
# end-of-class
