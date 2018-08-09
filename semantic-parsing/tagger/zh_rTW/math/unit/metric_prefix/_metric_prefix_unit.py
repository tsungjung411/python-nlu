from concept import Concept
from tagger.math.unit.metric_prefix._metric_prefix_unit import _MetricPrefixUnit as rawMetricPrefixUnit
from tagger.math.real_number import RealNumber
from tagger.math.integer_number import IntegerNumber

class _MetricPrefixUnit(rawMetricPrefixUnit):
    '''
    @since 2018.07.25
    @author tsungjung411@gmail.com
    '''
    
    def _on_add_concept(self, sentence, concept):
        at = concept.end
        
        at = self._skip_whitespaces(sentence, at)
        if at >= sentence.length():
            return
        # end-of-if
        
        # ------------------------------------------
        # Handles the decimal part
        #
        #    integer_part + unit + 'decimal_part'
        # ------------------------------------------
       
        # finds the dominator of number concepts
        decimal_concept = sentence.get_prefix_dominated_concept(
            at, IntegerNumber, RealNumber, rawMetricPrefixUnit)
        if decimal_concept == None:
            
            # handles the case '一萬萬'
            #self.handle_postponed_evaluation(sentence, concept, at)
            return
        # end-of-if
        
        region_start = concept.start
        region_end = decimal_concept.end
        
        entity = sentence[region_start : region_end]
        entity = "".join(entity)
        
        derived_class = RealNumber
        
        # [concept_values] decimal part
        value = decimal_concept.concept_values['value']
        if issubclass(decimal_concept.type, rawMetricPrefixUnit):
            # 2萬2百 -> [2萬]+[2百], [2百] is rawMetricPrefixUnit
            # 2 doesn't mean 2000
            pass # nothing to change
        else:
            if value < 10:
                # 2萬5, 5 means 5000 (=5*10000/10)
                # 2千5, 5 means 500 (=5*1000/10)
                value = value * self.get_unit_size() / 10
            else:
                # 2萬5000, 5000 is still 5000
                # 2千500, 500 is still 500
                pass # decimal part: nothing to change
        # end-of-if
        
        # [concept_values] plus integer part
        value += concept.concept_values['value']
        
        concept_values = {
            'tagger': self.__class__,
            'value': value,
        }
        
        # creates a concept to wrap the above info
        concept = Concept(
            region_start, region_end, 
            entity, derived_class, concept_values)
        concept.sign(_MetricPrefixUnit)
        sentence.add_concept(concept)
    # end-of-def
    
    # deprecated, no longer in use
    def handle_postponed_evaluation(self, sentence, concept, at):
        '''
        Handles the case '一萬萬', where the second 萬 has not been 
        tagged, so we could not convert '一萬萬' into a value.
        
        More examples, '一萬萬萬', '一億億'
        '''
        for synonym in self.get_synonym_list():
            if sentence.startswith(at, synonym):
                region_start = concept.start
                region_end = at + len(synonym)
                number_concept = concept
                
                # recursively merges the concept with the same unit
                self._tagging_number_and_unit(
                    sentence,
                    region_start, region_end, 
                    number_concept, synonym)
                break
            # end-of-if
    # end-of-def
    
# end-of-class
