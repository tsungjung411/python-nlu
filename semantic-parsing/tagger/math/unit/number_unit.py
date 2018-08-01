from concept import Concept
from tagger.object import _Object
from tagger.math.integer_number import IntegerNumber
from tagger.math.real_number import RealNumber
from tagger.math.unit.unit import _Unit

class NumberUnit(_Object):
    '''
    @since 2018.07.31
    @author tsungjung411@gmail.com
    '''
    
    def __init__(self):
        self.__CLASS = NumberUnit
        super(self.__CLASS, self).__init__()
    # end-of-def
    
    def get_dependent_tagger_list(self):
        return [RealNumber]
    # end-of-def
    
    def _tag(self, sentence, index = 0):
        region_start = None
        region_end = None
        ch = length = None
        
        for i in range(index, sentence.length()):
            # Pattern: number + \s* + unit
            
            number_concept_list = sentence.get_prefix_concept_list(
                i, IntegerNumber, RealNumber)
            
            for number_concept in number_concept_list:
                at = number_concept.end
                if at >= sentence.length():
                    break
                # end-of-if
                
                at = self._skip_whitespaces(sentence, at)
                if at >= sentence.length():
                    break
                # end-of-if
                
                unit_concept_list = sentence.get_prefix_concept_list(
                    at, _Unit)
                
                if len(unit_concept_list) == 0:
                    continue
                # end-of-if
                
                unit_concept = unit_concept_list[0]
                region_start = i
                region_end = unit_concept.end
                
                entity = sentence[region_start : region_end]
                entity = "".join(entity)
                derived_class = unit_concept.type
                concept_values = {
                    'value': number_concept.concept_values['value'],
                    'unit': unit_concept.entity}
                
                concept = Concept(
                    region_start, region_end, 
                    entity, derived_class, concept_values)
                self._on_create_concept(sentence, concept)
                
                sentence.add_concept(concept)
                self._on_add_concept(sentence, concept)
                
            # end-of-for
        # end-of-for
    # end-of-def
# end-of-class
