from concept import Concept
from tagger.tagger import _Tagger

class _Object(_Tagger):
    '''
    Defines the abstract universal-object class for tagging.
    
    @since 2018.07.24
    @author tsungjung411@gmail.com
    '''
    
    def __init__(self):
        self.__CLASS = _Object
        super(self.__CLASS, self).__init__()
    # end-of-def
    
    def get_entity_label(self):
        raise Exception(
            "need to implement 'get_entity_label(self)' on "
            + str(self.__class__))
    # end-of-def
    
    def get_synonym_list(self):
        raise Exception(
            "need to implement 'get_synonym_list(self)' on "
            + str(self.__class__))
    # end-of-def
    
    def _tag(self, sentence, index = 0):
        region_start = None
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
            
            if length > 0:
                region_start = i
                region_end = i + length
                
                # entity: '公', '尺' -> '公尺'
                entity = sentence[region_start : region_end]
                entity = "".join(entity)
                
                # handled class
                derived_class = self.__class__
                
                # entity label
                label = self.get_entity_label()
                concept_values = {label: entity}
                
                # creates a concept to wrap the above info
                concept = Concept(
                    region_start, region_end, 
                    entity, derived_class, concept_values)
                self._on_create_concept(sentence, concept)
                
                # adds the concept on the sentence
                sentence.add_concept(concept)
                self._on_add_concept(sentence, concept)
            # end-of-if
    # end-of-def
    
    def _on_create_concept(self, sentence, concept):
        '''
        Define the callback to let the clients have a chance to 
        update the concept, such as metric_prefix_unit (30k->30000)
        
        @since 2018.07.24
        @author tsungjung411@gmail.com
        '''
    # end-of-def
    
    def _on_add_concept(self, sentence, concept):
        '''
        Define the callback to let the clients have a chance to 
        listen to the add-concept event, such as:
        
            - 2萬5, concept='2萬', we also need to handle '5'
              where 5 means 5000 (=5*10000/10)
              
            - 2千5, concept='2千', we also need to handle '5'
              where 5 means 500 (=5*1000/10)
        
        @since 2018.07.26
        @author tsungjung411@gmail.com
        '''
    # end-of-def
        
# end-of-class

# ===================================================================

class _Postmodifier(_Object): # 後修飾子
    '''
    Defines the abstract universal-object class that is used as 
    a post-modifer.
    
    In English grammar, a postmodifier is a modifier that follows the
    word or phrase it limits or qualifies. Modification by a 
    postmodifier is called postmodification. 
    @see https://www.thoughtco.com/postmodifier-grammar-1691519
    
    A modifier placed before the head is called a premodifier; 
    one placed after the head is called a postmodifier.
    @see https://en.wikipedia.org/wiki/Grammatical_modifier
     
    @since 2018.08.01
    @author tsungjung411@gmail.com
    '''
    
    FIELD_HEAD = 'head'
    FIELD_POSTMODIFER = 'postmodifer'
    
    def _tag(self, sentence, index = 0):
        region_start = None
        region_end = None
        at = 0
        
        synonym_list = self.get_synonym_list()
        
        for i in range(index, sentence.length()):
            
            length = 0 # the length of a synonym
            for synonym in synonym_list:
                if sentence.startswith(i, synonym):
                    length = len(synonym)
                    break
                # end-of-if
            # end-of-for
            
            if length == 0 or i == 0:
                continue
            # end-of-if
            
            at = i - 1
            if at < 0:
                break
            # end-of-if
            
            at = self._skip_whitespaces_reversely(sentence, at)
            if at < 0:
                break
            # end-of-if
            
            head_concept_list = self._get_head_concept_list()
            head_concept = sentence.get_suffix_dominated_concept(
                at, *head_concept_list)
            
            if head_concept == None:
                continue
            # end-of-if

            region_start = head_concept.start
            region_end = i + length
            self._tagging(
                sentence, 
                region_start, region_end, 
                head_concept, synonym)
        # end-of-for
    # end-of-def
    
    def _get_head_concept_list(self):
        raise Exception(
            "need to implement '_get_head_concept_list(self)' on "
            + str(self.__class__))
    # end-of-def
    
    def _tagging(self, sentence, 
                 region_start, region_end, 
                 head_concept: 'e.g. a number, like 22k of "22k左右"', 
                 postmodifer: 'e.g. a , like 左右 of "22k左右"'):
        
        entity = sentence[region_start : region_end]
        entity = "".join(entity)

        # handled class: the derived class itself
        derived_class = self.__class__

        # entity label
        label = self.get_entity_label()
        
        # 22k of "22k左右"
        number = head_concept.concept_values['value']
        
        concept_values = {
            label: entity,
            self.FIELD_HEAD: head_concept,
            self.FIELD_POSTMODIFER: postmodifer
        }
        
        # creates a concept to wrap the above info
        concept = Concept(
            region_start, region_end, 
            entity, derived_class, concept_values)
        self._on_create_concept(sentence, concept)

        sentence.add_concept(concept)
        self._on_add_concept(sentence, concept)
    # end-of-def
    
# end-of-class
