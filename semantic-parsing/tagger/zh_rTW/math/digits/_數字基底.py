from tagger._token import _Token
from tagger.math.integer_number import IntegerNumber

class _數字基底(_Token, IntegerNumber):
    '''
    @since 2018.08.03
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_value(self):
        raise Exception(
            "need to implement 'get_synonym_value(self)' on "
            + str(self.__class__))
    # end-of-def
    
    def _on_create_concept(self, sentence, concept):
        concept.concept_values['value'] = self.get_synonym_value()
    # end-of-def
    
# end-of-class
