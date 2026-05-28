import requests

def get_github_stats(username):
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"👤 유저명: {data['login']}")
            print(f"📦 퍼블릭 레포 수: {data['public_repos']}")
            print(f"👥 팔로워: {data['followers']}")
            print(f"👣 팔로잉: {data['following']}")
            print("자기소개 없음") if data['bio'] is None else print(f"{data['bio']}")

            if data['followers'] == 0:
                print("아직 팔로워가 없어요!")
            else:
                print(f"팔로워가 {data['followers']}명 있어요.")

        else:
            print("유저를 찾을 수 없어.")
    except:
        print("네트워크 오류!")
        
username = input("GitHub 유저명 입력: ")
get_github_stats(username)