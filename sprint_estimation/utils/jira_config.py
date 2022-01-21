from utils.config_parse import Config


class JiraConfig(Config):

    def __init__(self, ini_location):
        super().__init__(ini_location)

    def get_api_token(self):
        return self.config_section_map("Jira")["api_token"]

    def get_jira_server(self):
        return self.config_section_map("Jira")["server"]

    def get_email(self):
        return self.config_section_map("Jira")["email"]
