from concept import Concept
from tagger._tagger import _Tagger

class IntegerNumber(_Tagger):
    '''
    Defines the integer class for tagging.
    
    @since 2018.07.13
    @author tsungjung411@gmail.com
    '''
    
    def __init__(self):
        self.__CLASS = IntegerNumber
        super(self.__CLASS, self).__init__()
    # end-of-def
    
    def _tag(self, sentence, index = 0):
        region_start = index
        region_end = None
        ch = None
        
        for i in range(index, sentence.length()):
            ch = sentence[i]
            
            # normalize
            # '０'(=65296) -> '0'
            # ...
            # '９'(=65305) -> '9'
            if '０' <= ch and ch <= '９':
                ch = chr(ord(ch) - ord('０') + ord('0'))
                
                # update back to the source
                sentence[i] = ch
            # end-of-if
            
            if '0' <= ch and ch <= '9':
                continue
            else:
                region_end = i
                break;
            # end-of-if
        # end-of-for
        
        if region_end == None:
            region_end = sentence.length()
        # end-of-if
        
        if region_end > region_start:
            entity = sentence[region_start : region_end]
            entity = "".join(entity)
            concept_values = {'value': int(entity)}
            concept = Concept(
                region_start, region_end, 
                entity, self.__CLASS, concept_values)
            sentence.add_concept(concept)
        # end-of-if
        
        # not meet the ending, continue to tag?
        if region_end < sentence.length():
            if region_start == region_end:
                # not found the entity
                self._tag(sentence, region_end + 1)
            else:
                # found the entity
                self._tag(sentence, region_end)
        # end-of-if
    # end-of-def
    
    @classmethod
    def get_precedence(klass):
        return klass.PRECEDENCE_INTEGER_NUMBER
    # end-of-def
    
# end-of-class
