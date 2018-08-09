from concept import Concept

class Sentence(list):
    '''
    Defines the sentence structure which can hold the meanings of 
    phrases (part of sentence)
    
    @since 2018.07.13
    @author tsungjung411@gmail.com
    '''
    
    def __init__(self, sentence):
        '''
        Sample:
            sentence: "我要17.3吋筆電"
            sequence: '17.3吋'
             - start: 2
             - end: 7 (excluded)
             - entity: '17.3吋'
             - concept_type: NumberInchUnit
             - concept_values: {'value': '17.3', 'unit': '吋'}
        '''
        super(Sentence, self).__init__(sentence)
        
        # holds length, sentence
        self.__length = len(sentence)
        self.__sentence = sentence
        
        # initializes the prefix/suffux concept list  
        self.__prefix_concept_list = [None] * self.__length
        self.__suffix_concept_list = [None] * self.__length
        
        for idx in range(self.__length):
            start = idx 
            end = idx + 1 # excluded (i.e. not included)
            entity = self[idx] # i.e. the char itself
            concept_type = None # no concept
            
            self.__prefix_concept_list[idx] \
                = [Concept(start, end, entity, concept_type)]
            
            # note: index = end - 1
            self.__suffix_concept_list[idx] \
                = [Concept(start, end, entity, concept_type)]
        # end-of-for
        
        # used to save taggers which have already been executed
        self.__tagger_set = set()
    # end-of-def
    
    def length(self):
        '''
        Returns the length of the sentence.
        '''
        return self.__length
    # end-of-def
    
    def __raise_immutable_exception(self):
        '''
        @see https://docs.python.org/3/tutorial/datastructures.html
        @since 2018.07.19
        '''
        raise Exception("The string is immutable")
    # end-of-if
    
    def append(self, item):
        '''
        Add an item to the end of the list. Equivalent to 
        a[len(a):] = [x].
        '''
        self.__raise_immutable_exception()
    # end-of-if
    
    def extend(self, iterable):
        '''
        Extend the list by appending all the items from the iterable.
        Equivalent to a[len(a):] = iterable
        '''
        self.__raise_immutable_exception()
    # end-of-if
    
    def insert(self, index, item):
        '''
        Insert an item at a given position.
        '''
        self.__raise_immutable_exception()
    # end-of-if
    
    def remove(self, item):
        '''
        Remove the first item from the list whose value is equal to x.
        '''
        self.__raise_immutable_exception()
    # end-of-if
    
    def pop(self, index):
        '''
        Remove the item at the given position in the list, and return
        it.
        '''
        self.__raise_immutable_exception()
    # end-of-if
    
    def clear():
        '''
        Remove all items from the list. Equivalent to del a[:].
        '''
        self.__raise_immutable_exception()
    # end-of-if
    
    def startswith(self, sentence_region_start, sequence, 
            ignore_case = True):
        
        # checks the ending position
        region_end = sentence_region_start + len(sequence)
        if region_end > self.__length:
            return False # out-of-bound
        # end-of-if
        
        region_start = sentence_region_start
        
        # compares each char
        for i in range(region_start, region_end):
            ch1 = self[i]
            ch2 = sequence[i - region_start]
            
            if ignore_case:
                ch1 = ch1.lower()
                ch2 = ch2.lower()
            # end-of-if
            
            if ch1 != ch2:
                return False
            # end-of-if
        # end-of-for
        
        return True
    # end-of-def
    
    def add_concept(self, concept):
        '''
        Adds a concept under the given position (where is at 
        concept.start)
        '''
        # checks the parameter
        if concept == None:
            raise Exception("concept could not be null")
        # end-of-if
        
        i_th = concept.start
        self.__prefix_concept_list[i_th].append(concept)
        i_th = concept.end - 1
        self.__suffix_concept_list[i_th].append(concept)
    # end-of-def
    
    def remove_concept(self, concept) -> 'True or False':
        prefix_flag = self.__remove_prefix_concept(concept)
        suffix_flag = self.__remove_suffix_concept(concept)
        if prefix_flag != suffix_flag:
            self.dump()
            raise Exception(
                'prefix_flag and suffix_flag are not consistent'
                + '\n - prefix_flag:' + str(prefix_flag)
                + '\n - suffix_flag:' + str(suffix_flag)
                + '\n - concept:' + str(concept))
        # end-of-if
        return prefix_flag or suffix_flag
    # end-of-def
    
    def __remove_prefix_concept(self, concept) -> 'True or False':
        # checks the parameter
        i_th = concept.start
        if i_th >= len(self.__prefix_concept_list):
            raise IndexError(
                "len(self.__prefix_concept_list): {}\nconcept: {}\n{}".format(
                str(len(self.__prefix_concept_list)),
                str(concept),
                'the index of the given concept is out of range'))
        # end-of-if

        # gets the concept list under the specified position
        i_th_concept_list = self.__prefix_concept_list[i_th]
        return self.__remove_concept_from(concept, i_th_concept_list)
    # end-of-def
    
    def __remove_suffix_concept(self, concept) -> 'True or False':
        # checks the parameter
        i_th = concept.end - 1
        if i_th < 0:
            raise IndexError(
                "len(self.__suffix_concept_list): {}\nconcept: {}\n{}".format(
                str(len(self.__suffix_concept_list)),
                str(concept),
                'the index of the given concept is out of range'))
        # end-of-if

        # gets the concept list under the specified position
        i_th_concept_list = self.__suffix_concept_list[i_th]
        return self.__remove_concept_from(concept, i_th_concept_list)
    # end-of-def
    
    def __remove_concept_from(self, concept, i_th_concept_list) -> 'True or False':
        # removes the target concept
        deleted_flag = False
        for idx in reversed(range(len(i_th_concept_list))):
            deleting_concept = i_th_concept_list[idx]
            if concept == deleting_concept:
                del i_th_concept_list[idx]
                deleted_flag = True
                # keeps searching the next one
            # end-of-if
        # end-of-for
        return deleted_flag
    # end-of-def
    
    def __get_concept_list(self, internal_concept_list, *grabbed_concept_type_list_in_tuple):
        '''
        Gets the concept list which are satisfied with:
        
        Where those concepts are:
         - at the index
         - compatible with one of concepts in the given list
        '''
        concept_list = []
        
        for self_concept in internal_concept_list:
            if self_concept.type == None:
                continue # default: char type (TBD)
            # end-of-if
            
            for concept_type in grabbed_concept_type_list_in_tuple:
                #
                # issubclass(IntegerNumber, IntegerNumber) = True
                # i.e. 'IntegerNumber' is a sub-class of 'IntegerNumber'
                # 
                # issubclass(RealNumber, IntegerNumber) = True
                # i.e. 'RealNumber' is a sub-class of 'IntegerNumber'
                #
                # if one of concept_type is matched,
                # we need to break the loop to avoid from adding twice
                #
                derived_class = self_concept.type
                parent_class = concept_type
                if issubclass(derived_class, parent_class):
                    concept_list.append(self_concept)
                    break # avoid from adding twice
                # end-of-if
            # end-of-if
        # end-of-if
        
        return concept_list
    # end-of-def
    
    def get_prefix_concept_list(self, index, *grabbed_concept_type_list_in_tuple):
        # index, index+1, index+2, ..., index+n
        # is compatible with one of concepts in the given list 
        return self.__get_concept_list(
            self.__prefix_concept_list[index],
            *grabbed_concept_type_list_in_tuple)
    # end-of-def
    
    def get_suffix_concept_list(self, index, *grabbed_concept_type_list_in_tuple):
        # index-n, ..., index-2, index-1, index
        # is compatible with one of concepts in the given list 
        return self.__get_concept_list(
            self.__suffix_concept_list[index],
            *grabbed_concept_type_list_in_tuple)
    # end-of-def
    
    def get_prefix_dominated_concept(self, index, *concept_type_list_in_tuple):
        '''
        Gets the dominator from the concept list which are satisfied 
        with:
        
        Where those concepts are:
         - at the index
         - compatible with one of concepts in the given list
         
        Context:
         - 3萬5百:
           [13:14] 5
           [13:14] 5 (IntegerNumber): {'value': 5}
           [13:15] 5百 (百): {'value': 500.0, 'prefix': '百', 'number': 5}
           [14:15] 百
           
           3萬5 -> 35000
           3萬5百 -> 30500
           get_prefix_dominate_concept('5', '5百') = '5百'
        '''
        prefix_concept_list = self.get_prefix_concept_list(
            index, *concept_type_list_in_tuple)
        
        if len(prefix_concept_list) == 0:
            return None
        else:
            # finds the max end
            concept_dominator = prefix_concept_list[0]
            max_end = prefix_concept_list[0].end
            
            for idx in range(1, len(prefix_concept_list)):
                concept = prefix_concept_list[idx]
                
                if concept.end > max_end:
                    concept_dominator = concept
                    max_end = concept.end
                # end-of-if
            # end-of-for
            return concept_dominator
        # end-of-if
    # end-of-def
    
    def get_suffix_dominated_concept(self, index, *concept_type_list_in_tuple):
        '''
        Gets the dominator from the concept list which are satisfied 
        with:
        
        Where those concepts are:
         - at the index
         - compatible with one of concepts in the given list
         
        Context:
         - 3萬5百元:
           [11:12] 3
           [12:13] 萬
           [11:13] 3萬
           [11:15] 3萬5百
           [13:14] 5 (IntegerNumber): {'value': 5}
           [13:15] 5百 (百): {'value': 500.0, 'prefix': '百', 'number': 5}
           [14:15] 百
           
           5百元 -> 500元
           3萬5百元 -> 30500元
           get_suffix_dominate_concept('5百', '3萬5百') = '3萬5百'
        '''
        suffix_concept_list = self.get_suffix_concept_list(
            index, *concept_type_list_in_tuple)
        
        if len(suffix_concept_list) == 0:
            return None
        else:
            # finds the min start
            concept_dominator = suffix_concept_list[0]
            min_start = suffix_concept_list[0].start
            
            for idx in range(1, len(suffix_concept_list)):
                concept = suffix_concept_list[idx]
                
                if concept.start < min_start:
                    concept_dominator = concept
                    min_start = concept.start
                # end-of-if
            # end-of-for
            return concept_dominator
        # end-of-if
    # end-of-def
    
    def register_tagger(self, tagger):
        self.__tagger_set.add(tagger)
    # end-of-def
    
    def has_tagged_by(self, tagger):
        return tagger in self.__tagger_set
    # end-of-def
    
    def __str__(self):
        return self.__sentence
    # end-of-def
    
    def __repr__(self):
        '''
        What is the difference between __str__ and __repr__?
        
        str:
        - means 'string'
        - the info is friendly, it is for users to use
        repr: 
        - means 'representation'
        - the info is unfriendly, it is for developers to use
        
        @see https://stackoverflow.com/questions/1436703/difference-between-str-and-repr
        @see https://blog.csdn.net/luckytanggu/article/details/53649156
        '''
        output = ''
        
        output += "Sentence: {}, len={}".format(
            self.__sentence, self.__length)
        
        output += '\n----------------------------'
        
        output += '\n' + 'dump the prefix:'
        for i_th in range(self.__length):
            i_th_concept_list = self.__prefix_concept_list[i_th]
            i_th_concept_list_length = len(i_th_concept_list)
            
            if i_th_concept_list_length <= 1:
                output += '\n ├──[{}] {}'.format(i_th, i_th_concept_list[0])
            else:
                output += '\n ├──[{}]'.format(i_th)
                for j_th, concept in enumerate(i_th_concept_list):
                    if j_th < i_th_concept_list_length - 1:
                        output += '\n │   ├── ' + str(concept)
                    else:
                        output += '\n │   └── ' + str(concept)
                    # end-of-if
                # end-of-if
            # end-of-if
        # end-of-for
        
        output += '\n' + '----------------------------'
        
        output += '\n' + 'dump the suffix:'
        for i_th in range(self.__length):
            i_th_concept_list = self.__suffix_concept_list[i_th]
            i_th_concept_list_length = len(i_th_concept_list)
            
            if i_th_concept_list_length <= 1:
                output += '\n ├──[{}] {}'.format(i_th, i_th_concept_list[0])
            else:
                output += '\n ├──[{}]'.format(i_th)
                for j_th, concept in enumerate(i_th_concept_list):
                    if j_th < i_th_concept_list_length - 1:
                        output += '\n │   ├── ' + str(concept)
                    else:
                        output += '\n │   └── ' + str(concept)
                    # end-of-if
                # end-of-if
            # end-of-if
        # end-of-for
        
        output += '\n' + '----------------------------'
        
        return output
    # end-of-def
    
    def dump(self):
        print(self.__repr__())
    # end-of-def
    
# end-of-class
