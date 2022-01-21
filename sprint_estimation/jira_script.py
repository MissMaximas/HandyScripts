from jira import JIRA

from utils.jira_config import JiraConfig

# Hardcoded Bullshit
JIRA_CONF_PATH = "/Users/chloeparkes/missmaximas/HandyScripts/sprint_estimation/conf/prod.ini"
# Don't Judge me


class JiraCon:

    RLP1_BOARD_ID = 578

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

    def get_project(self, project="RLP1"):
        return self._conn.project(project)

    def show_boards(self, project="RLP1"):
        print(self._conn.boards(projectKeyOrID=project))

    def get_latest_sprint(self):
        sprints = self._conn.sprints(board_id=self.RLP1_BOARD_ID)
        highest_id = 0
        for sprint in sprints:
            if int(sprint.id) > highest_id:
                highest_id = int(sprint.id)
        return self._conn.sprint_info(board_id=str(self.RLP1_BOARD_ID), sprint_id=str(highest_id))

    def get_active_tickets_in_sprint(self):
        #TODO: 
        return self._conn.search_issues('project=PROJ')

    def testy(self, issue):
        print(self._conn.sprints(board_id=self.RLP1_BOARD_ID))


print(JiraCon().get_latest_sprint())

