
import requests, argparse, json
from urllib.parse import unquote

#command line tool that Takes an url of a file and a clickup task id and uploads the file as attachment to the clickup task

parser = argparse.ArgumentParser()

parser.add_argument("-u", "--url", help="Enter the attachment url")

parser.add_argument("-id", "--task", help="enter clickup task id")

args = parser.parse_args()

clickup_token = '<-your-token->'

headers = {
  "Authorization": clickup_token
}

if args.url is not None and args.task is not None:
    attachment_url = args.url
    task_id = args.task
    res = requests.get(attachment_url)
    clickup_url = "https://api.clickup.com/api/v2/task/" + task_id + "/attachment"

    if res.status_code == 200:
        s = res.headers['content-disposition']
        a = s[22:]
        name = a.split(';')[0]
        name = unquote(name)
        files = {"attachment": (name, res.content)}
        response = requests.post(clickup_url, headers=headers, files = files)

        if response.status_code == 200:
          print({'status': 'success'})
        else:
          print({"status": "response.content"})
    
    else:
      print({"status": "download failed"})

