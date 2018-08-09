from concept import Concept
from tagger._token import _Token
from tagger.math.unit.number_unit import NumberUnit

class _Range(_Token):
    '''
    @since 2018.08.01
    @author tsungjung411@gmail.com
    '''
    
    # https://zh.wikipedia.org/wiki/%E5%8D%80%E9%96%93
    # http://ocw.aca.ntu.edu.tw/ocw_files/100S111/100S111_CS01L01.pdf
    # [註] 無限區間 (a,∞) 不可記為 (a,∞]。因為 ∞ 不是 (a,∞) 的邊界點
    FIELD_BOUNDARY_LABEL = 'boundary'
    FIELD_BOUNDARY_EXCLUSIVE = 0
    FIELD_BOUNDARY_INCLUSIVE = 1
    
    def _on_create_concept(self, sentence, concept):
        self._on_custom_value_range(sentence, concept)
        self._on_custom_interval(sentence, concept)
        self._on_custom_unit(sentence, concept)
    # end-of-def
    
    def _on_custom_value_range(self, sentence, concept):
        raise Exception(
            "need to implement '_on_custom_value_range(self, sentence, concept)' on "
            + str(self.__class__))
    # end-of-def
    
    def _on_custom_interval(self, sentence, concept):
        raise Exception(
            "need to implement '_on_custom_interval(self, sentence, concept)' on "
            + str(self.__class__))
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
    
    @classmethod
    def get_precedence(klass):
        return klass.PRECEDENCE_RANGE
    # end-of-def
    
# end-of-class
