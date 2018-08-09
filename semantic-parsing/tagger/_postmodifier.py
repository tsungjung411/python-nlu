from concept import Concept
from tagger._token import _Token

class _Postmodifier(_Token): # 後修飾子
    '''
    Pattern: pretoken +  postmodifier
    
    Defines the abstract universal-object class that is used as 
    a post-modifer.
    
    In English grammar, a postmodifier is a modifier that follows the
    word or phrase it limits or qualifies. Modification by a 
    postmodifier is called postmodification. 
    @see https://www.thoughtco.com/postmodifier-grammar-1691519
    
    A modifier placed before the head is called a premodifier; 
    one placed after the head is called a postmodifier.
    @see https://en.wikipedia.org/wiki/Grammatical_modifier
     
    @since 2018.08.02
    @author tsungjung411@gmail.com
    '''
    
    FIELD_PRETOKEN = 'pretoken'
    FIELD_POSTMODIFIER = 'postmodifier'
    
    def get_pretoken_label(self):
        return self.FIELD_PRETOKEN 
    # end-of-def
    
    def get_postmodifier_label(self):
        return self.FIELD_POSTMODIFIER 
    # end-of-def
    
    def get_pretoken_concept_list(self):
        raise Exception(
            "need to implement '_get_pretoken_concept_list(self)' on "
            + str(self.__class__))
    # end-of-def
    
    def _tag(self, sentence, index = 0):
        region_start = None
        region_end = None
        at = 0
        synonym_list = self.get_synonym_list()
        
        # pretoekn might be at 0, 
        # so postmodifier should starts from max(index, 1)
        for i in range(max(index, 1), sentence.length()):
            
            synonym = self.match_prefix_synonym_at(
                sentence, i, synonym_list)
            if synonym == None:
                continue
            # end-of-if
            
            at = i - 1
            at = self._skip_whitespaces_reversely(sentence, at)
            if at < 0:
                # cannot find the modified token
                continue
            # end-of-if
            
            pretoken_concept_list = self.get_pretoken_concept_list()
            pretoken_concept = sentence.get_suffix_dominated_concept(
                at, *pretoken_concept_list)
            
            if pretoken_concept == None:
                continue
            # end-of-if

            region_start = pretoken_concept.start
            if type(synonym) == Concept:
                region_end = i + len(synonym.entity)
            else:
                region_end = i + len(synonym)
            # end-of-if
            
            self._tagging(
                sentence, 
                region_start, region_end, 
                pretoken_concept, synonym)
        # end-of-for
    # end-of-def
    
    def _tagging(self, sentence, 
                 region_start, region_end, 
                 pretoken: 'e.g. a number, like 22k of "22k左右"', 
                 postmodifier:   'e.g. a , like 左右 of "22k左右"'):
        
        entity = sentence[region_start : region_end]
        entity = "".join(entity)

        # handled class: the derived class itself
        derived_class = self.__class__
        
        concept_values = {
            self.get_pretoken_label():     pretoken,
            self.get_postmodifier_label(): postmodifier
        }
        
        # creates a concept to wrap the above info
        concept = Concept(
            region_start, region_end, 
            entity, derived_class, concept_values)
        concept.sign(_Postmodifier)
        self._on_create_concept(sentence, concept)

        sentence.add_concept(concept)
        self._on_add_concept(sentence, concept)
    # end-of-def
    
# end-of-class
