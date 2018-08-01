from concept import Concept
from tagger.math.unit.unit import _Unit
from tagger.math.real_number import RealNumber
from tagger.math.integer_number import IntegerNumber

class _MetricPrefixUnit(_Unit):
    '''
    Defines the abstract metrix-prefix-unit class for tagging.
    
    @since 2018.07.25
    @author tsungjung411@gmail.com
    @see http://www.measuring.org.tw/knowledge/knowledge_detail.asp?id=1
    '''
    
    def get_entity_label(self):
        return 'value'
    # end-of-def
    
    def get_unit_size(self):
        # for example,
        #     g: return 1000000000
        #     m: return 1000000
        #     k: return 1000
        #     h: return 100
        #     da: return 10
        raise Exception("need to implement 'get_unit_size(self)'")
    # end-def
    
    def _tag(self, sentence, index = 0):
        region_start = None
        region_end = None
        ch = None
        at = 0
        
        for i in range(index, sentence.length()):
            itself = _MetricPrefixUnit
            number_concept_list = sentence.get_prefix_concept_list(
                i, IntegerNumber, RealNumber, itself)
            if len(number_concept_list) == 0:
                continue
            # end-of-if
            
            for number_concept in number_concept_list:
                at = number_concept.end
                if at >= sentence.length():
                    break
                # end-of-if
                
                at = self._skip_whitespaces(sentence, at)
                if at >= sentence.length():
                    break
                # end-of-if
                
                length = 0 # the length of a synonym
                synonym_list = self.get_synonym_list()
                for synonym in synonym_list:
                    if sentence.startswith(at, synonym):
                        length = len(synonym)
                        break
                    # end-of-if
                # end-of-for
            
                if length > 0:
                    region_start = i
                    region_end = at + length
                    self._tagging(
                        sentence, 
                        region_start, region_end, 
                        number_concept, synonym)
                #end-of-if
            # end-of-if
        # end-of-for
    # end-of-def
    
    def _tagging(self, sentence, 
                 region_start, region_end, 
                 number_concept: 'a number, like 22 of 22k', 
                 synonym: 'a unit, like k of 22k'):
        
        entity = sentence[region_start : region_end]
        entity = "".join(entity)

        # handled class
        derived_class = RealNumber #self.__class__

        # entity label
        label = self.get_entity_label()

        # 22k = 22 x 1000 = 22000
        number = number_concept.concept_values['value']
        value = number * self.get_unit_size()

        concept_values = {
            label: entity,
            'number': number,
            'metric_prefix': synonym,
            'value': value
        }

        # creates a concept to wrap the above info
        concept = Concept(
            region_start, region_end, 
            entity, derived_class, concept_values)
        self._on_create_concept(sentence, concept)

        sentence.add_concept(concept)
        self._on_add_concept(sentence, concept)
    # end-of-def
    
    @classmethod
    def get_precedence(klass):
        return klass.PRECEDENCE_NUMBER_SCALE
    # end-of-def
    
# end-of-class
