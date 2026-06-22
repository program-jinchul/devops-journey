import requests
import os
from dotenv import load_dotenv
from datetime import date

today = str(date.today())
load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"bearer {TOKEN}"}

def get_contribution_stats(username):
    query = """
    query($username: String!) {
        user(login: $username) {
            contributionsCollection {
                totalCommitContributions
                totalPullRequestContributions
                totalIssueContributions
                contributionCalendar {
                    totalContributions
                    weeks {
                        contributionDays {
                            contributionCount
                            date
                        }
                    }
                }
            }
        }
    }
    """
    
    try:
        response = requests.post(
            "https://api.github.com/graphql",
            json={"query": query, "variables": {"username": username}},
            headers=HEADERS
        )
        data = response.json()
        stats = data["data"]["user"]["contributionsCollection"]
        calendar = stats["contributionCalendar"]
        
        print(f"🌱 총 잔디: {calendar['totalContributions']}개")
        print(f"💻 커밋: {stats['totalCommitContributions']}개")
        print(f"🔀 PR: {stats['totalPullRequestContributions']}개")
        print(f"🐛 이슈: {stats['totalIssueContributions']}개")

        for week in calendar["weeks"]:
            for day in week["contributionDays"]:
                if day["date"] == today:
                    print(f"오늘의 잔디: {day["contributionCount"]}")
        
    except:
        print("오류가 발생했어요.")

username = input("GitHub 유저명 입력: ")
get_contribution_stats(username)