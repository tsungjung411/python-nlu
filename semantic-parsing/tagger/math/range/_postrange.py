from tagger._premodifier import _Premodifier
from tagger.math.range._range import _Range
from tagger.math.integer_number import IntegerNumber
from tagger.math.real_number import RealNumber
from tagger.math.unit.number_unit import NumberUnit

class _Postrange(_Range, _Premodifier):
    '''
    Pattern: premodifier + [A, B]
    where [A, B] is called postrange
    
    @since 2018.08.06
    @author tsungjung411@gmail.com
    '''
    
    def get_posttoken_concept_list(self):
        return [IntegerNumber, RealNumber, NumberUnit]
    # end-of-def
    
    def _on_custom_unit(self, sentence, concept):
        posttoken = concept.concept_values[self.get_posttoken_label()]
        
        '''
        if posttoken.type == NumberUnit:
            # e.g. 3萬5000元以下 = [超過] + [3萬5000]
            #  - premodifier: [超過]
            #  - posttoken: [3萬5000元]
            #     - 'number': '35000' (raw data)
            #     - 'value': 30500.0
            #     - 'unit': '元'
        else:
            # e.g. 3萬5000以下 = [超過] + [3萬5000]
            #  - premodifier: [超過]
            #  - posttoken: [3萬5000]
            #     - 'value': '35000'
        # end-of-if     
        '''
        if issubclass(posttoken.type, NumberUnit):
            concept.concept_values['unit'] = posttoken.concept_values['unit']
        # end-of-if
    # end-of-def
    
# end-of-class
