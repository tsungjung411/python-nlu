from concept import Concept
from tagger._postmodifier import _Postmodifier
from tagger.math.integer_number import IntegerNumber
from tagger.math.real_number import RealNumber
from tagger.math.unit._unit import _Unit

class NumberUnit(_Postmodifier):
    '''
    @since 2018.07.31
    @author tsungjung411@gmail.com
    '''
    
    def __init__(self):
        self.__CLASS = NumberUnit
        super(self.__CLASS, self).__init__()
    # end-of-def
    
    # --------------------------------------
    # pretoken
    # --------------------------------------
    def get_pretoken_label(self):
        return 'number'
    # end-of-def
    
    def get_number_label(self):
        return self.get_pretoken_label()
    # end-of-def
    
    # --------------------------------------
    # postmodifier
    # --------------------------------------
    def get_postmodifier_label(self):
        return 'unit'
    # end-of-def
    
    def get_unit_label(self):
        return self.get_postmodifier_label()
    # end-of-def
    
    
    def get_dependent_tagger_list(self):
        return [IntegerNumber, RealNumber]
    # end-of-def
    
    def get_pretoken_concept_list(self):
        return [IntegerNumber, RealNumber]
    # end-of-def
    
    def get_synonym_list(self):
        return [_Unit]
    # end-of-def
    
    def _on_create_concept(self, sentence, concept):
        pretoken = concept.concept_values[self.get_pretoken_label()]
        concept.concept_values['value'] = pretoken.concept_values['value']
        concept.sign(NumberUnit)
    # end-of-def
    
    @classmethod
    def get_precedence(klass):
        return klass.PRECEDENCE_NUMBER_UNIT
    # end-of-def
    
# end-of-class
