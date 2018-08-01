import os
from inspect import isclass

class TaggerManager:
    '''
    A utiltity to manage tagger.
    
    @since 2018.07.17
    @author tsungjung411
    '''
    __instance = None
    __tagger_list = None
    
    @classmethod
    def get_instance(klass, force = False):
        if klass.__instance == None:
            klass.__instance = klass()
        # end-of-if
        return klass.__instance
    # end-of-def
    
    def __init__(self):
        self.__create_char_to_class_mapping_table()
    # end-of-def
    
    def __create_char_to_class_mapping_table(self):
        self.__map = [None] * 65536
        self.__get_tagger_list()
    # end-of-def
    
    def get_tagger_list(self):
        if self.__tagger_list == None:
            tagger_list = self.__get_tagger_list()
            self.sort_by_precedence(tagger_list)
            self.__tagger_list = tagger_list
        # end-of-if
        return list(self.__tagger_list) # a copy
    # end-of-def
    
    def __get_tagger_list(self):
        file_path = __file__
        
        # <your_app_path>/tagger
        # - parent_file = <your_app_path>
        # - tagger_dir = <your_app_path>/tagger
        # - tagger_module = tagger
        parent_file = os.path.abspath(os.path.join(file_path, os.pardir))
        tagger_dir = os.path.join(parent_file, 'tagger')
        tagger_module = 'tagger'
        
        tagger_list = list()
        self.__gather_tagger_list__by_postorder(
            tagger_dir, tagger_module, tagger_list)
        return tagger_list
    # end-of-def
    
    def __gather_tagger_list__by_postorder(
            self, folder, module, tagger_list):
        
        # splits file_name_list into dir and file
        file_name_list = os.listdir(folder)
        dir_list = []
        file_list = []
        
        # gathers the module info to build fully qualified names
        sub_module_list = []
        
        for file_name in file_name_list:
            full_file_path = os.path.join(folder, file_name)
            
            if os.path.isdir(full_file_path):
                dir_list.append((full_file_path, file_name))
            elif os.path.isfile(full_file_path):
                file_list.append((full_file_path, file_name))
            # end-of-if
        # end-of-for
                
        # sorts by short file names
        # item[0]: full_file_path
        # item[1]: file_name
        dir_list.sort(key = lambda item:item[1])
        file_list.sort(key = lambda item:item[1])

        # ------------------------------------------
        # traversal by post-order
        # ------------------------------------------
        for full_file_path, file_name in dir_list:
            # recursively traversal
            self.__gather_tagger_list__by_postorder(
                full_file_path, 
                module + '.' + file_name, 
                tagger_list)
        # end-of-for
        
        for full_file_path, file_name in file_list:
            
            # - the file should be a python file (ends with '.py')
            # - but not include '__xxx.py', 'xxx__.py', or '__xxx__.py',
            #   like '__init__.py'
            if file_name.endswith('.py') == False \
                    or file_name.endswith('__.py') \
                    or file_name.startswith('__'):
                continue
            # end-of-if
            
            # dynamically gets the class reference from string-based 
            # components
            klass = self.__get_class_by_file_name(
                full_file_path, file_name, module)
            
            if klass.__name__.startswith('_'):
                # A class name starts with a underline '_' means that
                # it is an abstract class (like @abstract annotation).
                # It cannot be instantiated, so lets ignore it.
                continue
            else:
                tagger_list.append(klass)
            # end-of-if
        # end-of-for
    # end-of-def
    
    def __get_class_by_file_name(
            self, full_file_path, file_name, parent_module_name):
        '''
        Dynamically gets the class reference from string-based 
        components.
        
        For example,
         - file: '<your_app_path>/tagger/math/real_number.py'
         - parent_module_name: 'tagger.math'
         - module_name: 'tagger.math.real_number'
           - class[0]: <class 'concept.Concept'>
           - class[1]: <class 'tagger.math.integer_number.IntegerNumber'>
           - class[2]: <class 'tagger.math.real_number.RealNumber'>
        '''
        file_name_without_extension = file_name.split('.')[0]
        module_name = parent_module_name + '.' + file_name_without_extension

        # loads 'real_number.py'
        # @see https://goo.gl/DPZZ9U
        #      How to find the list of all the class name in a file in python?
        file_py = __import__(module_name, fromlist=['*'])
        
        for attr_name in dir(file_py):
            attr = getattr(file_py, attr_name)
            if isclass(attr):
                
                # normalizes the attribute name and file name
                # so that we can compare them
                normalized_attr_name = attr_name.replace('_', '').lower()
                normalized_file_name = file_name_without_extension.replace('_', '')
                
                if normalized_attr_name == normalized_file_name:
                    return attr
                # end-of-if
            # end-of-if
        # end-of-for
        
        # error handling
        error = "cannot find any class declaration on '{}'".format(full_file_path)
        error += '\n - parent_module_name: ' + parent_module_name
        error += '\n - file_name: ' + file_name
        error += '\n - classes in file: '
        for attr_name in dir(file_py):
            attr = getattr(file_py, attr_name)
            if isclass(attr):
                error += '\n   - {} ({})'.format(attr_name, str(attr))
            # end-of-if
        # end-of-for
        error += '\n'
        error += "\n - rule: file_name_without_extension.replace('_', '') == class_name.replace('_', '').lower()"
        raise AssertionError(error)
    # end-of-def
    
    def sort_by_precedence(self, tagger_list):
        tagger_list.sort(
            key = lambda klass: klass.get_precedence(), 
            reverse=True)
    # end-of-def
    
# end-of-class
