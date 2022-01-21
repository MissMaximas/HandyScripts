import configparser


class Config:

    def __init__(self, ini_location):
        self.config = configparser.ConfigParser()
        self._load_ini_file(ini_location)

    def _load_ini_file(self, ini_location):
        self.config.read(ini_location)

    def _get_sections(self):
        return self.config.sections()

    def config_section_map(self, section):
        """ Gets config sections from file

        Config sections are:
            [Test1]
            key = 123456

        Using the parameter *section*, it would
        pull the config section from the file
        with that name.

        :param section: str
        :return: dict
        """
        dict1 = {}
        options = self.config.options(section)
        for option in options:
            try:
                dict1[option] = self.config.get(section, option)
                if dict1[option] == -1:
                    print("skip: %s" % option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1