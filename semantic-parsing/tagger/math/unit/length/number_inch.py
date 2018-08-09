from tagger.math.unit.number_unit import NumberUnit
from tagger.math.integer_number import IntegerNumber
from tagger.math.unit.length.inch_unit import InchUnit

class NumberInch(NumberUnit):
    '''
    Pattern: Number + InchUnit
    
    @since 2018.08.08
    @author tsungjung411@gmail.com
    '''
    
    def get_pretoken_label(self):
        return 'integer_part'
    # end-of-def
    
    def get_synonym_list(self):
        return [InchUnit]
    # end-of-def
    
    def _on_create_concept(self, sentence, concept):
        super(NumberInch, self)._on_create_concept(sentence, concept)
        
        # ..., 至少14"
        if concept.end >= sentence.length():
            return
        # end-of-if
        
        decimal_part = sentence.get_prefix_dominated_concept(
            concept.end, IntegerNumber)
        if decimal_part == None:
            return
        # end-of-if
        
        concept.end = decimal_part.end
        concept.entity = ''.join(sentence[concept.start : concept.end])
        concept.concept_values['decimal_part'] = decimal_part
        
        integer_part = concept.concept_values['value']
        decimal_part = decimal_part.concept_values['value']
        number = '{}.{}'.format(integer_part, decimal_part)
        value = float(number)
        concept.concept_values['value'] = value
        
        concept.sign(NumberInch)
    # end-of-def
# end-of-class
