
import os

class WorkArea(object):
    def __init__(self, path='') -> None:
        super().__init__()
        if path:
            self.path = path
        else:
            self.path = os.getcwd() + '/sram_gereator_work_directory'
            os.makedirs(self.path, exist_ok=True)
        self.config_file = self.path + '/.sram_generator.config'
        self.techdir_path = self.path + '/techfiles'
        self.libs = {}
        self.create_default_folders()
        self.import_techdir(self.techdir_path)
        self.read_configs(self.config_file)
        
    def create_default_folders(self):
        ''''''
        print('checking files')

        # checking config file
        if not os.path.exists(self.config_file):
            cf = open(self.config_file, 'w')
            cf.close()
            print(self.config_file, 'created')
        
        # cheching techdir
        if not os.path.exists(self.techdir_path):
            os.makedirs(self.techdir_path)
            print(self.techdir_path, 'created')
    
    def read_configs(self, file_path):
        '''
        Reading sram parametrs 
        and output files from config file
        '''
        pass

    def import_techdir(self, techdir_path):
        '''
        Exlpore techdirectory
        Reads techfile, layermap, lib.defs files
        Getting setting from techdir
        '''
        self.layermap_path = techdir_path + '/layermap'
        self.techfile_path = techdir_path + '/techfile.tf'
        self.lib_defs_path = techdir_path + '/lib.defs'

        if not os.path.isfile(self.lib_defs_path):
            lf = open(self.lib_defs_path, 'w')
            lf.close()
        self.read_lib_defs(self.lib_defs_path)
    
    def read_lib_defs(self, lib_defs):
        '''Reading lib.defs file'''
        self.libs_data = {}
        with open(lib_defs) as lf:
            for line in lf:
                line = line.split('#', 1)[0]
                line = line.strip()
                if not line:
                    continue
                if line.startswith('define'):
                    lib_name, lib_path = [i.strip() for i in line.split(' ') if i.strip()][1:3]
                    if self.libs_data.get(lib_name):
                        print(f'Warning: {lib_name} defined multiple times')
                    if os.path.isdir(lib_path):
                        self.libs_data[lib_name] = {}
                        self.libs_data[lib_name]['path'] = lib_path
                        self.libs_data[lib_name]['blocks'] = self.parse_lib(lib_path)
                    else:
                        print(f'Warning: {lib_path} is invalid lib path')
            lf.close()
    
    def parse_lib(self, lib_path):
        ''''''
        data = {}
        for block_dir in os.listdir(lib_path):
            block_path = f'{lib_path}/{block_dir}'
            if not os.path.isdir(block_path):
                continue
            data[block_dir] = {}
            data[block_dir]['path'] = block_path
            data[block_dir]['cells'] = {}
            for cell_dir in os.listdir(block_path):
                cell_path = f'{block_path}/{cell_dir}'
                if not os.path.isdir(block_path):
                    continue
                data[block_dir]['cells'][cell_dir] = {}
                data[block_dir]['cells'][cell_dir]['path'] = cell_path
                if os.path.exists(f'{cell_path}/layout'):
                    data[block_dir]['cells'][cell_dir]['layout'] = {}
                if os.path.exists(f'{cell_path}/netlist'):
                    data[block_dir]['cells'][cell_dir]['netlist'] = {}
                if os.path.exists(f'{cell_path}/lef'):
                    data[block_dir]['cells'][cell_dir]['lef'] = {}
        return data
    
    def add_lib(self, lib_name):
        '''
        Creating library directory and 
        adding to lib.defs file
        '''
        os.makedirs(self.path + f'/{lib_name}')
        lb_df = open(self.lib_defs_path, 'a')
        lb_df.write(f'define {lib_name} {self.path}/{lib_name}\n')
        lb_df.close()
        self.libs_data[lib_name] = {}
        self.libs_data[lib_name]['path'] = f'{self.path}/{lib_name}'
        self.libs_data[lib_name]['blocks'] = {}
    
    def add_block(self, lib_name, block_name):
        '''
        Creating library directory and 
        adding to lib.defs file
        '''
        os.makedirs(self.path + f'/{lib_name}/{block_name}', exist_ok=True)
        self.libs_data[lib_name]['blocks'][block_name] = {}
        self.libs_data[lib_name]['blocks'][block_name]['path'] = f'{self.path}/{lib_name}/{block_name}'
    
    def get_lib_data(self, lib_name):
        '''
        Returns dictionary containing 
        information about libs, blocks, and cells
        '''
        return self.libs_data[lib_name]

    def get_libs(self):
        return self.libs_data.keys()