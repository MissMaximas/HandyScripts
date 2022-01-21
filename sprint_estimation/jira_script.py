from jira import JIRA

from utils.jira_config import JiraConfig

# Hardcoded Bullshit
JIRA_CONF_PATH = "/Users/chloeparkes/missmaximas/HandyScripts/sprint_estimation/conf/prod.ini"
# Don't Judge me


class JiraCon:

    def __init__(self):
        self.JIRA_CONF = JiraConfig(JIRA_CONF_PATH)
        self._conn = self._make_jira_con()

    def _make_jira_con(self):
        return JIRA(options={'server': self.JIRA_CONF.get_jira_server()},
                    basic_auth=(self.JIRA_CONF.get_email(), self.JIRA_CONF.get_api_token())
                    )

    def display_issue_details(self, issue):
        single_issue = self._conn.issue(issue)
        print('{}: {}:{}'.format(single_issue.key,
                                 single_issue.fields.summary,
                                 single_issue.fields.reporter.displayName)
              )


JiraCon().display_issue_details("INIT-1942")