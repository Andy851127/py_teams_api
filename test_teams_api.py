import pymsteams

class TeamsAPI:
    def __init__(self):
        # 建立 Teams 連接器後，掛載 Webhook URL
        self.teams_channel_webook_url = "example_webhook_url"

    def create_teams_card(self):
        # 建立 connectorcard object 並給予 Webhook URL
        self.myTeamsMessage = pymsteams.connectorcard(self.teams_channel_webook_url)

    def create_card_contents(self,title,content):
        # 建立 Title
        self.myTeamsMessage.title(title)
        # 建立 Text
        self.myTeamsMessage.text(content)

    def send_to_teams_channel(self):
        # 傳輸給 Teams channel
        self.myTeamsMessage.send()

    def teams_process(self,title,content):
        self.create_teams_card()
        self.create_card_contents(title,content)
        self.send_to_teams_channel()

if __name__ == "__main__":
    title = "TEST API"
    content = "Test teams api!!!!!! "
    teams_api = TeamsAPI()
    teams_api.teams_process(title,content)

