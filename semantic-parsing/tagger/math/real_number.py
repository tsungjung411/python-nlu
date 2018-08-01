from concept import Concept
from tagger.math.integer_number import IntegerNumber

class RealNumber(IntegerNumber):
    '''
    Defines the real-number class for tagging.
    
    @since 2018.07.13
    @author tsungjung411@gmail.com
    '''
    
    def __init__(self):
        self.__CLASS = RealNumber
        super(self.__CLASS, self).__init__()
    # end-of-def
    
    def get_dependent_tagger_list(self):
        return [IntegerNumber]
    # end-of-def
    
    def _tag(self, sentence, index = 0):
        region_start = None
        region_end = None
        ch = None
        
        for i in range(index, sentence.length()):
            concept_list = sentence.get_prefix_concept_list(
                i, IntegerNumber)
            if len(concept_list) == 0:
                continue
            # end-of-if
            
            for integer_concept in concept_list:
                at = integer_concept.end
                if at >= sentence.length():
                    break
                # end-of-if
                
                ch = sentence[at]
                if ch != '.':
                    continue
                else:
                    at += 1
                # end-of-if
                
                # found a floating point
                decimal_concept_list = sentence.get_prefix_concept_list(
                    at, IntegerNumber)
                if len(decimal_concept_list) == 0:
                    continue
                else:
                    decimal_concept = decimal_concept_list[0]
                # end-of-if
                
                region_start = integer_concept.start
                region_end = decimal_concept.end
                
                entity = sentence[region_start : region_end]
                entity = "".join(entity)
                concept_values = {'value': float(entity)}
                
                sentence.remove_concept(integer_concept)
                sentence.remove_concept(decimal_concept)
                
                concept = Concept(
                    region_start, region_end, 
                    entity, self.__CLASS, concept_values)
                sentence.add_concept(concept)
            # end-of-if
        # end-of-for
    # end-of-def
    
    @classmethod
    def get_precedence(klass):
        return klass.PRECEDENCE_REAL_NUMBER
    # end-of-def
    
# end-of-class
