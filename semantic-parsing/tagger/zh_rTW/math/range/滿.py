from tagger.math.range._gt_eq_postrange import _GtEqPostrange

class 滿(_GtEqPostrange): # TBD/TODO, 複合修飾詞
    '''
     - 滿千回饋5%
     - 滿千送千
     
    @since 2018.08.07
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_list(self):
        return ['滿']
    # end-of-def
    
# end-of-class
