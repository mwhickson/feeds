#
# feeds - a news reader for RSS, Atom or other internet news feeds.
#

from configparser import ConfigParser
from os import path as ospath
from pathlib import Path as plpath

APP_NAME = "feeds"
DEFAULT_HOME = "~/.config/feeds/"
DEFAULT_CONFIG_INI = "config.ini"
DEFAULT_SUBSCRIPTION_FILE = "subscriptions.xml"


class Config:
    """Application configuration settings list."""

    def __init__(self, base_folder: str = str(plpath.home())) -> None:
        """Construct a feeds configuration."""
        self.BaseFolder = base_folder
        self.HomeFolder = DEFAULT_HOME.replace("~", self.BaseFolder)
        self.ConfigurationFile = ospath.join(self.HomeFolder, DEFAULT_CONFIG_INI)
        self.SubscriptionFile = ospath.join(self.HomeFolder, DEFAULT_SUBSCRIPTION_FILE)

    def load_configuration(self) -> None:
        """Load the application configuration file from disk."""
        if not ospath.exists(self.ConfigurationFile):
            print(f"configuration file '{self.ConfigurationFile}' does not exist")
        else:
            config = ConfigParser()
            config.read(self.ConfigurationFile)
            if "settings" in config:
                for key in config["settings"]:
                    print(key, config["settings"][key])

    def load_subscriptions(self) -> None:
        """Load the application subscription file from disk."""
        if not ospath.exists(self.SubscriptionFile):
            print(f"subscription file '{self.SubscriptionFile}' does not exist")
        else:
            f = open(self.SubscriptionFile)
            lines = f.readlines()
            f.close()

            # TODO: process subscriptions...
            print(lines)


class Feed:
    """A news feed in RSS, Atom, or other standardized format."""

    def __init__(self, title: str, url: str) -> None:
        """Construct a Feed with a title and a url."""
        self.Title: str = title
        self.Url: str = url
        self.Status: type[FeedStatus] = None
        self.Items: list[type[FeedItem]] = []


class FeedItem:
    """An article in a news feed."""

    def __init__(self, title: str, url: str) -> None:
        """Construct a FeedItem with a title and a url."""
        self.Title: str = title
        self.Url: str = url
        self.Content: str = ""
        self.PublishedOn = None
        self.Status: type[FeedItemStatus] = None


class FeedItemStatus:
    """The status of a FeedItem (article)."""

    def __init__(self, new: bool = False, read: bool = False) -> None:
        """Construct a FeedItemStatus with its state flags (e.g. new, read)."""
        self.IsNew: bool = new
        self.IsRead: bool = read


class FeedStatus:
    """The status of a Feed."""

    def __init__(self, retrievedOn = None) -> None:
        """Construct a FeedStatus with its last retrieved date."""
        self.LastRetrieved = retrievedOn


class Subscriptions:
    """A list of Feeds being monitored."""

    def __init__(self, feeds: list[type[Feed]] = []) -> None:
        """Construct Subscriptions with a list of Feeds to monitor."""
        self.Feeds: list[type[Feed]] = feeds


# main


if __name__ == "__main__":
    print(APP_NAME)

    config = Config()
    config.load_configuration()
    # config.load_subscriptions()
