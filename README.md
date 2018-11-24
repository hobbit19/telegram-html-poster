# Installation

```
git clone https://github.com/yevhenii-nepsha/telegram-html-poster.git
cd telegram-html-poster
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

create `config.py` based on `config_sample_py`

```
channel = "@channelname"
bot_token = "y0urb0tt0ken"
chat_report = 1234567890 <- chat id for reporting
```

# Posting

* Edit your `general_post.html` file
* Run `python post.py -post` -> you will receive message to your chat from `chat_report` variable in config:

```
Successfully posted in channel: @channelname
    title: Post Title
    link:  t.me/channelname/<post id>
```

# Updating the posts

* Edit your `general_post.html` file
* Run `python post.py -edit -id=<post id>`
