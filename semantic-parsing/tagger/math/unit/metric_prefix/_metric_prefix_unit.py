from concept import Concept
from tagger.math.unit._unit import _Unit
from tagger.math.real_number import RealNumber
from tagger.math.integer_number import IntegerNumber

class _MetricPrefixUnit(_Unit):
    '''
    Defines the abstract metrix-prefix-unit class for tagging.
    
    @since 2018.07.25
    @author tsungjung411@gmail.com
    @see http://www.measuring.org.tw/knowledge/knowledge_detail.asp?id=1
    '''
    
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
        at = length = 0
        
        for i in range(index, sentence.length()):
            
            # finds the metric-prefix unit
            synonym = self.match_prefix_synonym_at(sentence, i)
            # all of synonyms are concrate concepts, not abstract
            
            if synonym == None:
                continue
            # end-of-if
            
            # tags the unit itself
            self._tagging_unit(
                sentence, 
                region_start = i, 
                region_end = i + len(synonym), 
                synonym = synonym
            )
            
            # parses the number part if existed
            at = i - 1
            at = self._skip_whitespaces_reversely(sentence, at)
            if at < 0:
                # a metric-prefix unit without the number part
                # such as '萬一', '千二', '百九'
                # the default numbber is 1
                
                number_concept = Concept(
                    start = i, 
                    end = i, # a dummy number
                    entity = '1', 
                    concept_type = IntegerNumber, 
                    concept_values = {'value': 1}
                )
            else:
                # a metric-prefix unit with the number part
                # such as '一萬一', '一千二', '一百九'
                
                number_concept = sentence.get_suffix_dominated_concept(
                    at, IntegerNumber, RealNumber)
                if number_concept == None:
                    continue
                # end-of-if
            # end-of-if
            
            # tags the [number unit]
            self._tagging_number_and_unit(
                sentence, 
                region_start = number_concept.start, 
                region_end = i + len(synonym), 
                number_concept = number_concept, 
                synonym = synonym
            )
            
        # end-of-for
    # end-of-def
    
    def _tagging_unit(self, sentence, 
            region_start, region_end, 
            synonym: 'just the unit itself'):
        
        entity = sentence[region_start : region_end]
        entity = "".join(entity)

        # handled class
        derived_class = self.__class__
        
        concept_values = {
            'unit': synonym,
            'value': self.get_unit_size()
        }

        # creates a concept to wrap the above info
        concept = Concept(
            region_start, region_end, 
            entity, derived_class, concept_values)
        concept.sign(_MetricPrefixUnit)
        #self._on_create_concept(sentence, concept)

        sentence.add_concept(concept)
        #self._on_add_concept(sentence, concept)
    # end-of-if
    
    def _tagging_number_and_unit(self, sentence, 
            region_start, region_end, 
            number_concept: 'a number, like 22 of 22k', 
            synonym: 'a unit, like k of 22k'):
        
        entity = sentence[region_start : region_end]
        entity = "".join(entity)

        # handled class
        derived_class = RealNumber #self.__class__
        
        # 22k = 22 x 1000 = 22000
        number = number_concept.concept_values['value']
        value = number * self.get_unit_size()
        
        concept_values = {
            'number': number,
            'metric_prefix': synonym,
            'value': value
        }
        
        # creates a concept to wrap the above info
        concept = Concept(
            region_start, region_end, 
            entity, derived_class, concept_values)
        concept.sign(_MetricPrefixUnit)
        self._on_create_concept(sentence, concept)
        
        sentence.add_concept(concept)
        self._on_add_concept(sentence, concept)
    # end-of-def
    
    @classmethod
    def get_precedence(klass):
        return klass.PRECEDENCE_NUMBER_SCALE
    # end-of-def
    
# end-of-class
