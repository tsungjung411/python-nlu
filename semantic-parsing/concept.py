class Concept:
    '''
    Defines the abstract concept. The concept instance can be used to 
    tag a sequence (sub-string) to indicate what it is.
    
    For example, '17.3吋' means the length is 17.3 inches
    
    @since 2018.07.13
    @author tsungjung411@gmail.com
    '''
    
    def __init__(self, start, end, 
            entity, concept_type, concept_values = {}):
        '''
        Sample:
            sentence: "我要17.3吋筆電"
            sequence: '17.3吋'
             - start: 2
             - end: 7 (excluded)
             - entity: '17.3吋'
             - concept_type: NumberInchUnit
             - concept_values: {'value': '17.3', 'unit': '吋'}

        Input:
            start: 
                the start index of a sub-sentence in a sentence (included)
            end: 
                the end index of a sub-sentence in a sentence (excluded)
            entity: 
                the sub-sentence (i.e. part of sentence)
                in general, it is a meaningful phrase
            concept_type: 
                the sub-class of Concept
            concept_valus: 
                holds the (internal) values of this concept
        '''
        self.start = start
        self.end = end
        self.entity = entity
        self.type = concept_type
        self.concept_values = concept_values
    # end-of-def
    
    def __eq__(self, other):
        '''
        Implements 'equal-to' comparison: self = other
        
        @since 2018.07.13
        @see https://docs.python.org/3/reference/datamodel.html#object.__eq__
        '''
        if other == None:
            return False
        else:
            return self.start == other.start \
                and self.end == other.end \
                and self.entity == other.entity \
                and self.type == other.type
        # end-of-if
    # end-of-if
    
    def __le__(self, other):
        '''
        Implements 'less-than-or-equal-to' comparison: self ⊆ other
        
        @since 2018.07.13
        @see https://docs.python.org/3/reference/datamodel.html#object.__le__
        '''
        
        # IntegerNumber <= IntegerNumber
        #  - issubclass(IntegerNumber, IntegerNumber) = True
        # 
        # IntegerNumber <= RealNumber 
        # Note:
        #     The real number cover integer, but the real-number  
        #     class is extended from the integer class in 
        #     implementation
        #  - issubclass(RealNumber, IntegerNumber) = True
        #
        return self.start >= other.start \
            and self.end <= other.end \
            and issubclass(other.type, self.type)
    # end-of-if
    
    def __repr__(self):
        if self.type == None:
            return "[{}:{}] {}".format(
                self.start, self.end, 
                self.entity)
        else:
            return "[{}:{}] {} ({}): {}".format(
                self.start, self.end, 
                self.entity, self.type, 
                str(self.concept_values))
        # end-of-if
    # end-of-def
    
# end-of-class
