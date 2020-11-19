# mixins.base_save_mixins.py

"""
Base Mixin Class to use with api modules. 
Mixin classes will implement methods related to saving, retrieving and
reading data from saved datafiles.
"""

class BaseSaveMixin:
    """
    My intention here is to implement a data saving and retrieving
    functionality.
    
    The module assumes that this will used with an api_module with 
    instance variable 'return_data'
    
    It will be calling self.return_data when handling data.
    
    Please specify save(), set_header_from_data() methods which are
    appropriate for handling data for each api modules.
    """
    
    _data_validator_functions = []
    
    def __init__(self, *args, **kwargs):
        """
        Pre setting headers will guide the middleware to look for
        data. Which kind of data shall it retreive or save?
        """
        
        if kwargs.get('header'):
            self.header = kwargs.get('header')
        else:
            raise ValueError('You need to specify header values!')
            
        super(BaseSaveMixin, self).__init__()
            

    def _validate_data(self):
        for function in self._data_validator_functions:
            function(self)
    
    def save(self):
        self._validate_data()
        
        
        
        
            

            
            