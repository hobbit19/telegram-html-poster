import argparse
import config
import telebot
import sys
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-edit", action="store_true", help="edit message")
parser.add_argument("-post", action="store_true", help="post message")
parser.add_argument("-id", type=int, help="message id for edit")
parser.add_argument("-path", type=str, help="message id for edit")
args = parser.parse_args()


class Post(object):
    def __init__(self, channel, markdown_file):
        self.channel = channel
        self.markdown_file = markdown_file or "general_post.html"
        self.bot = telebot.TeleBot(token=config.bot_token)

    def prepare_content(self):
        with open(self.markdown_file, 'r') as content:
            return content.read()

    def get_post_title(self):
        with open(self.markdown_file, 'r') as content:
            post = content.read()
            soup = BeautifulSoup(post, 'html.parser')
            return soup.find("b", id="title").string

    def post_to_channel(self):
        content = self.prepare_content()
        message = self.bot.send_message(self.channel, content, parse_mode="HTML")
        return message.message_id

    def post_and_get_report(self):
        title = self.get_post_title()
        message_id = self.post_to_channel()
        message = """
            <b>Successfully posted in channel:</b> {}
            <b>title:</b> {}
            <b>link: </b> t.me/{}/{}
            """.format(self.channel, title, self.channel.split("@")[1], message_id)
        self.bot.send_message(
            config.chat_report, message, parse_mode="HTML", disable_web_page_preview=True
        )

    def update_message(self, _id):
        self.bot.edit_message_text(self.prepare_content(), self.channel, message_id=_id, parse_mode="HTML")


if __name__ == "__main__":

    poster = Post(config.channel, args.path)

    if args.post:
        poster.post_and_get_report()
    elif args.edit and args.id:
        poster.update_message(args.id)
    else:
        print("Error.")
        sys.exit()
