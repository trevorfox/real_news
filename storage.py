from flask import json
import time

class Archive:

    archive_path = "archive.json"

    def __init__(self):
        pass

    def read_story(self,story_id):
        print ('read story')
        with open(self.archive_path, 'r+') as archive_file:
            archive = json.load(archive_file)
            if story_id in archive:
                story = archive[story_id]
                self.upvote(story)
                archive[story['id']] = story

                archive_file.seek(0)
                archive_file.write(json.dumps(archive))
                archive_file.truncate()
                return True, story
            else:
                return False, {}


    def write_story(self,story_form):
        # shortened timestamp string
        story_id = str(time.time()).split('.')[0][4:]

        with open(self.archive_path, 'r+') as archive_file:
            archive = json.load(archive_file)
            complete_story = {
                "id": story_id,
                "title": story_form["title"],
                "description": story_form["description"],
                "image": story_form["image"],
                "votes": 0
            }

            if (story_form["author"]): complete_story["author"] = story_form["author"]

            archive[story_id] = complete_story
            archive_file.seek(0)
            archive_file.write(json.dumps(archive))
            archive_file.truncate()

            return complete_story

    def upvote(self,story):
        story["votes"] += 1

    def get_top_stories():
        with open(self.archive_path, 'r+') as archive_file:
            archive = json.load(archive_file)
            
