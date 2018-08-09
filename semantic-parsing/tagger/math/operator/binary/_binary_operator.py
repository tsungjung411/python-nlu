from concept import Concept
from tagger._token import _Token
from tagger.math.integer_number import IntegerNumber
from tagger.math.real_number import RealNumber
from tagger.math.unit.metric_prefix._metric_prefix_unit import _MetricPrefixUnit

class _BinaryOperator(_Token):
    '''
    @since 2018.08.06
    @author tsungjung411@gmail.com
    '''
    
    def _tag(self, sentence, index = 0):
        region_start = index
        region_end = None
        ch = length = None
        
        synonym_list = self.get_synonym_list()
        
        for i in range(index, sentence.length()):
            
            length = 0 # the length of a synonym
            for synonym in synonym_list:
                if sentence.startswith(i, synonym):
                    length = len(synonym)
                    break
                # end-of-if
            # end-of-for
            
            if length == 0:
                continue
            # end-of-if
            
            at = i - 1
            at = self._skip_whitespaces_reversely(sentence, at)
            if at < 0:
                continue
            # end-of-if
            
            num1_concept = sentence.get_suffix_dominated_concept(
                at, IntegerNumber, RealNumber, _MetricPrefixUnit)
            # Case for _MetricPrefixUnit: 
            # - 十乘十, 十 is not only a nuit, but also a number
            
            if num1_concept == None:
                continue
            # end-of-if
            
            at = i + len(synonym)
            at = self._skip_whitespaces(sentence, at)
            if at >= sentence.length():
                continue
            # end-of-if
            
            num2_concept = sentence.get_prefix_dominated_concept(
                at, IntegerNumber, RealNumber, _MetricPrefixUnit)
            # Case for _MetricPrefixUnit: 
            # - 十乘十, 十 is not only a nuit, but also a number
            
            if num2_concept == None:
                continue
            # end-of-if
            
            region_start = i
            region_end = i + len(synonym)
            self._tagging1(sentence, 
                           region_start, region_end, 
                           synonym)
            self._tagging2(sentence, 
                           num1_concept, num2_concept)
        # end-of-for
    # end-of-def
    
    def _tagging1(self, sentence,
                 region_start, region_end, synonym):
        
        entity = sentence[region_start : region_end]
        entity = "".join(entity)
        
        derived_class = self.__class__
        
        concept_values = {
            'operator': self.get_formal_operator()
        }
        
        # creates a concept to wrap the above info
        concept = Concept(
            region_start, region_end, 
            entity, derived_class, concept_values)
        self._on_create_concept(sentence, concept)

        sentence.add_concept(concept)
        self._on_add_concept(sentence, concept)
    # end-of-def
    
    def _tagging2(self, sentence,
                 num1_concept, num2_concept):
        
        region_start = num1_concept.start
        region_end = num2_concept.end
        entity = sentence[region_start : region_end]
        entity = "".join(entity)
        
        derived_class = RealNumber
        
        num1_value = num1_concept.concept_values['value']
        num2_value = num2_concept.concept_values['value']
        value = self.evaluate(num1_value, num2_value)

        concept_values = {
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
    
    def get_formal_operator(self):
        raise Exception(
            "need to implement 'get_formal_operator(self)' on "
            + str(self.__class__))
    # end-of-if
    
    def evaluate(self, num1, num2):
        raise Exception(
            "need to implement 'evaluate(self, num1, num2)' on "
            + str(self.__class__))
    # end-of-if
    
    @classmethod
    def get_precedence(klass):
        raise Exception(
            "need to implement 'get_precedence(klass)' on "
            + str(self.__class__))
    # end-of-def
    
# end-of-class
