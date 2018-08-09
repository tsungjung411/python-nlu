from tagger.math.range._gt_eq_postrange import _GtEqPostrange

class 至少(_GtEqPostrange): # TBD/TODO, 複合修飾詞
    '''
     - 數量至少上萬件
     - 至少月入三萬元的小眾經濟
     - 至少準備250萬
     - 退休金必須至少準備約1,600萬元
    
    @since 2018.08.01
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_list(self):
        return ['至少']
    # end-of-def
    
# end-of-class
