from tagger.math.unit.metric_prefix._metric_prefix_unit import _MetricPrefixUnit

class tera(_MetricPrefixUnit):
    '''
    Define the tera unit.
    
    @since 2018.07.25
    @author tsungjung411@gmail.com
    '''
    
    def get_synonym_list(self):
        return ['t', 'tera'] 
    # end-of-def
    
    def get_unit_size(self):
        return 1e12
    # end-def
    
# end-of-class
