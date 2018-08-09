from tagger.math.range._gt_postrange import _GtPostrange

class 超過(_GtPostrange): # TBD/TODO, 複合修飾詞
    '''
    - 【快去應徵】10種年薪超過10萬美元
    
    @since 2018.08.07
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_list(self):
        return ['超過']
    # end-of-def
    
# end-of-class
