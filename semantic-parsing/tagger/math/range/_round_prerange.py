from concept import Concept
from tagger.math.range._prerange import _Prerange

class _RoundPrerange(_Prerange):
    '''
    round prerange = [A, B] + suffix_modifier
    
    @since 2018.08.01
    @author tsungjung411@gmail.com
    '''
    
    def _on_create_concept(self, sentence, concept):
        head = concept.concept_values[self.FIELD_PRETOKEN]
        head_value = head.concept_values['value']
        
        epsilon = head_value * 0.07
        from_value = head_value - epsilon
        to_value = head_value + epsilon
        concept.concept_values['value'] = [from_value, to_value]
    # end-of-def
    
# end-of-class
