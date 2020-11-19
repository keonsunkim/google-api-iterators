# mixins/csv_mixins.py

import csv 



from .base_save_mixins import BaseSaveMixin

class CSVSaveMixin(BaseSaveMixin):
    
    _data_validator_functions = []
    
    def __init__(self, *args, **kwargs):
        """
        Check if file already exists, then we don't need to write headers.
        If file doesn't exist, write headers.
        """

        self.file_directory = kwargs.get('file_directory')
        
        super(CSVSaveMixin, self).__init__(*args, **kwargs)
        
        # This part became unneccessarily repetitive. Work on it later
        try:
            self.data_file = open(f'{self.file_directory}', 'r', encoding = 'utf-8')
            self.data_file.close()
        except:
            self.data_file = open(f'{self.file_directory}', 'w+', encoding = 'utf-8')
            self.csv_dict_writer = csv.DictWriter(self.data_file, fieldnames = self.header)
            self.csv_dict_writer.writeheader()
            self.data_file.close()
        finally:
            self.data_file = open(f'{self.file_directory}', 'a', encoding = 'utf-8')
            self.csv_dict_writer = csv.DictWriter(self.data_file, fieldnames = self.header)
        
        
    def retrieve_header_from_file(self):
        reader = csv.DictReader(self.data_file, skipinitialspace=True)
        return reader.fieldnames
        
    def save(self, *args, **kwargs):
        super().save()
        
        # Convert self.return_data into data only containing values in header!
        list_to_save = self._parser_function(self)
        print(list_to_save)
        self.csv_dict_writer.writerows(list_to_save)
        
    def close_file(self):
        self.data_file.close()

            
        