from tagger._postmodifier import _Postmodifier
from tagger.math.range._range import _Range
from tagger.math.integer_number import IntegerNumber
from tagger.math.real_number import RealNumber
from tagger.math.unit.number_unit import NumberUnit

class _Prerange(_Range, _Postmodifier):
    '''
    Pattern: [A, B] + premodifier
    where [A, B] is called prerange
    
    @since 2018.08.01
    @author tsungjung411@gmail.com
    '''
    
    def get_pretoken_concept_list(self):
        return [IntegerNumber, RealNumber, NumberUnit]
    # end-of-def
    
    def _on_custom_unit(self, sentence, concept):
        pretoken = concept.concept_values[self.get_pretoken_label()]
        
        '''
        if pretoken.type == NumberUnit:
            # e.g. 3萬5000元以下 = [3萬5000元] + [以下]
            #  - pretoken: [3萬5000元]
            #     - 'number': '35000' (raw data)
            #     - 'value': 30500.0
            #     - 'unit': '元'
            #  - postmodifier: [以下]
        else:
            # e.g. 3萬5000以下 = [3萬5000] + [以下]
            #  - pretoken: [3萬5000]
            #     - 'value': '35000'
            #  - postmodifier: [以下]
        # end-of-if     
        '''
        if issubclass(pretoken.type, NumberUnit):
            concept.concept_values['unit'] = pretoken.concept_values['unit']
        # end-of-if
    # end-of-def
    
# end-of-class
