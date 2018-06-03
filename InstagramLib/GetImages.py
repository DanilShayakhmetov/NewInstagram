from InstagramLib import instagram
import requests

# https://instagram.com/graphql/query/?query_id=17888483320059182&id=43232350&first=12&after=20

# Добавить получение по юзернейму

def GetHashImages(username, count):
    userStr = str(username)
    agent=instagram.Agent()
    account=instagram.Account(userStr)
    numberOfPict = int(count)
    agent.update(account)

    media=agent.getMedia(account, count=numberOfPict)
    publishHashArray = []
    for m in media:
        publishHashArray.append(m)
        # print(m)

    response = publishHashArray[0]

    return response



# GetHashImages()

def GetEmbeded(username, count):
    userStr = str(username)
    endpointEmbeded = 'https://api.instagram.com/oembed?url=http://instagr.am/p/'
    postsHash = GetHashImages(userStr, count)
    embededArray = []
    for post in postsHash:
        postStr = str(post)
        transitString = endpointEmbeded+postStr+'/'
        embededArray.append(transitString)

    return embededArray


# GetImages()


def GetImageJson(username, count):
    userStr = str(username)
    EmbededUrlsArray = GetEmbeded(userStr, count)
    imageArray = []
    for urls in EmbededUrlsArray:
        urlsStr = str(urls)
        response = requests.get(urlsStr)
        data = response.json()
        imageArray.append(data['thumbnail_url'])

    return imageArray


# GetImageJson('loginovskikh.a')