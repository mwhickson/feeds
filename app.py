#
# feeds - a news reader for RSS, Atom or other internet news feeds.
#
# sample config.ini (~/.config/feeds/)
#
# [settings]
# AppHomeFolder = "~/.config/feeds/"
# SubscriptionFile = "subscriptions.xml"
# DatabaseFile = "feeds.db"
# FeedCheckIntervalMinutes = 60
#

from configparser import ConfigParser
from os import path as ospath
from pathlib import Path as plpath

APP_NAME = "feeds"
DEFAULT_HOME = "~/.config/feeds/"
DEFAULT_CONFIG_INI = "config.ini"
DEFAULT_SUBSCRIPTION_FILE = "subscriptions.xml"
DEFAULT_DATABASE_FILE = "feeds.db"
DEFAULT_CHECK_INTERVAL = 60 # minutes

class Config:
    """Represent application configuration settings."""

    def __init__(self, base_folder: str = str(plpath.home())) -> None:
        """Construct a 'feeds' application configuration."""
        self.BaseFolder = base_folder

        self.HomeFolder = DEFAULT_HOME.replace("~", self.BaseFolder)

        self.ConfigurationFile = ospath.join(self.HomeFolder, DEFAULT_CONFIG_INI)
        self.SubscriptionFile = DEFAULT_SUBSCRIPTION_FILE
        self.DatabaseFile = DEFAULT_DATABASE_FILE
        self.FeedCheckInterval = DEFAULT_CHECK_INTERVAL

    def does_configuration_exist(self) -> bool:
        """Check to see if the current configuration file exists."""
        return ospath.exists(self.ConfigurationFile)

    def load_configuration(self) -> None:
        """Load the application configuration file from disk."""
        if not self.does_configuration_exist():
            print(f"configuration file '{self.ConfigurationFile}' does not exist")
        else:
            config = ConfigParser()
            config.read(self.ConfigurationFile)
            if "settings" in config:
                if "subscriptionfile" in config["settings"]:
                    self.SubscriptionFile = config["settings"]["subscriptionfile"]
                if "databasefile" in config["settings"]:
                    self.DatabaseFile = config["settings"]["databasefile"]
                if "feedcheckintervalminutes" in config["settings"]:
                    self.FeedCheckInterval = config["settings"]["feedcheckintervalminutes"]

    def does_subscriptions_exist(self) -> bool:
        """Check to see if the currently configured subscription file exists."""
        return ospath.exists(ospath.join(self.HomeFolder, self.SubscriptionFile))

    def load_subscriptions(self) -> None:
        """Load the application subscription file from disk."""
        if not self.does_subscriptions_exist():
            print(f"subscription file '{self.SubscriptionFile}' does not exist")
        else:
            f = open(ospath.join(self.HomeFolder, self.SubscriptionFile))
            lines = f.readlines()
            f.close()

            # TODO: process subscriptions...
            print(lines)

    def does_database_exist(self) -> bool:
        """Check to see if the currently configured database file exists."""
        return ospath.exists(ospath.join(self.HomeFolder, self.DatabaseFile))

    def load_database(self) -> None:
        """Load the application database file from disk."""
        pass # TODO: sqlite database


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
